# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: macarval <macarval@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/12 12:31:36 by macarval          #+#    #+#              #
#    Updated: 2025/11/13 22:16:46 by macarval         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import os
import argparse
import requests

from bs4 import BeautifulSoup # type: ignore
from colors import CYAN, BRED, BGREEN, BYELLOW, BBLUE, BPURPLE, BCYAN, RESET
from urllib import robotparser
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

USER_AGENT = "macarval_42_Sao_Paulo"
valid_exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}
cache = {}

def main():
	info()
	args = parse_args()
	validate_args(args)
	os.makedirs(args.p, exist_ok=True)

	visited_urls = set()
	get_images(args.url, args.r, args.l, args.p, visited_urls)

	print(f"\n{BBLUE}Download completed! Images saved to: \
		{BPURPLE}{args.p}{RESET}\n")

def info():
	print(f"\n{BYELLOW}{'-'*90}{RESET}")
	print(f"{BPURPLE}{'🕷️ Spider Module - Arachnida':^90}{RESET}")
	print(f"\n{CYAN}{'This module downloads images from a given URL.':^90}{RESET}")
	print(f"{BYELLOW}{'-'*90}{RESET}\n")

def parse_args():
	parser = argparse.ArgumentParser(description="Spider Module - Arachnida")

	parser.add_argument('-r',
						default=False,
						action='store_true',
						help='Command to enable recursively downloads the '
						'images in a URL received as a parameter.')

	parser.add_argument('-l',
						type=int,
						default=5,
						help='IMaximum depth level of the recursive download.')

	parser.add_argument('-p',
						type=str,
						default='./data/',
						help='The path where the images will be saved.')

	parser.add_argument('url',
						type=str,
						metavar='URL',
						help='URL to download images from.')

	return parser.parse_args()

def validate_args(args):
	if args.l < 1 or args.l > 10:
		error_quick_exit("Error: Level must be between 1 and 10.")

	if not args.p.endswith('/'):
		args.p = args.p + '/'

	if not args.url.startswith('https://') and \
		not args.url.startswith('http://'):
		args.url = 'https://' + args.url

	if not args.url.endswith('/'):
		args.url = args.url + '/'

def error_quick_exit(message):
	print(f"{BRED}{message}{RESET}\n")

	exit(1)

def get_url(url):
	try:
		response = requests.get(url, headers={'User-Agent': USER_AGENT},
					timeout=10)
		response.raise_for_status()
		return response

	except requests.exceptions.RequestException as e:
		print(f"{BRED}Failed to access the URL: {url}\n\nError: {e}{RESET}\n")
		return None

def get_images(page_url, recursive, depth, path, visited_urls):
	if depth < 1 or page_url in visited_urls:
		return

	if not is_allowed(page_url):
		print(f"{BRED}Ignoring (forbidden by robots.txt): {page_url}{RESET}")

	print(f"{BYELLOW}Processando ({BCYAN}Depth {depth}{BYELLOW}): \
			{BGREEN}{page_url}{RESET}")

	visited_urls.add(page_url)
	response = get_url(page_url)

	if response is None:
		return

	list_images = get_list_images(response.text, page_url)
	download_images(list_images, path)

	if recursive:
		list_subpages = get_list_subpages(response.text, page_url)
		for url in list_subpages:
			if is_allowed(url):
				get_images(url, recursive, depth - 1, path, visited_urls)
			else:
				print(f"{BRED}Ignoring subpage (forbidden by robots.txt): \
					{url}{RESET}")

def get_list_images(content, url):
	content = BeautifulSoup(content, 'html.parser')
	images_source = []

	for img in content.find_all('img'):
		src = img.get('src')
		if src and any(src.lower().endswith(ext) for ext in valid_exts):
			images_source.append((urljoin(url, src)))

	return images_source

def get_list_subpages(content, url):
	content = BeautifulSoup(content, 'html.parser')
	subpages_source = []

	for links in content.find_all('a', href=True):
		href = links.get('href')
		full_url = urljoin(url, href)
		parsed = urlparse(full_url)

		if parsed.netloc == urlparse(url).netloc:
			if not any(parsed.path.endswith(ext)
				for ext in valid_exts) and not parsed.fragment:
				subpages_source.append(full_url)

	return list(set(subpages_source))

def download_images(images, path):
	with ThreadPoolExecutor(max_workers=10) as executor:
		futures = []

		for img_url in images:
			futures.append(executor.submit(download_one_image, img_url, path))

		for future in as_completed(futures):
			future.result()

def download_one_image(img_url, path):
	try:
		if not is_allowed(img_url):
			print(f"{BRED}Ignoring image (forbidden by robots.txt): \
		 			{img_url}{RESET}")
			return False

		img_data = requests.get(img_url, headers={'User-Agent': USER_AGENT})
		img_data.raise_for_status()
		img_name = os.path.basename(img_url.split("?")[0])

		with open(os.path.join(path, img_name), 'wb') as img_file:
			img_file.write(img_data.content)

		return True

	except requests.exceptions.RequestException as e:
		print(f"{BRED}Failed to download image: {img_url}\nError: {e}{RESET}\n")
		return False

def get_robot(url):
	parsed_url = urlparse(url)
	domain = parsed_url.netloc

	if domain in cache:
		return cache[domain]

	robots_url = f"{parsed_url.scheme}: //{domain}/robots.txt"
	print(f"{BCYAN}Buscando {robots_url}{RESET}")

	rp = robotparser.RobotFileParser()
	response = get_url(robots_url)

	if response and response.status_code == 200:
		try:
			rp.parse(response.text.splitlines())
			print(f"{BGREEN}robots.txt from {domain} read successfully.{RESET}")
		except Exception as e:
			print(f"{BRED}Failed to parse the robots.txt file from \
		 			{domain}: {e}{RESET}")
			cache[domain] = None
			return None
	else:
		print (f"{BRED}Could not read robots.txt from {domain} \
		 	(status: {response.status_code if response else 'N/A'}).{RESET}\n")
		cache[domain] = None
		return None

	cache[domain] = rp
	return rp

def is_allowed(url):
	try:
		rp = get_robot(url)
		if rp:
			return rp.can_fetch(USER_AGENT, url)

		return True
	except Exception:
		return True

if __name__ == "__main__":
	main()
