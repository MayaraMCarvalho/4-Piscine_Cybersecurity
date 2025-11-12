# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: macarval <macarval@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/12 12:31:36 by macarval          #+#    #+#              #
#    Updated: 2025/11/12 17:36:27 by macarval         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import argparse
import os

from colors import CYAN, BPURPLE, BYELLOW, RESET

def valid_extentions():
	valid_exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}

def parse_args():
	parser = argparse.ArgumentParser(description="Spider Module - Arachnida")

	parser.add_argument('-r',
						default=False,
						action='store_true',
						help='Command to enable recursively downloads the images '
						'in a URL received as a parameter.')

	parser.add_argument('-l',
						type=int,
						default=5,
						help='IMaximum depth level of the recursive download.')

	parser.add_argument('-p',
						default='./data/',
						help='The path where the images will be saved.')

	parser.add_argument('url',
						help='URL to download images from.')

	return parser.parse_args()

def info():
	print(f"\n{BYELLOW}{'-'*90}{RESET}")
	print(f"{BPURPLE}{'🕷️ Spider Module - Arachnida':^90}{RESET}")
	print(f"\n{CYAN}{'This module downloads images from a given URL.':^90}{RESET}")
	print(f"{BYELLOW}{'-'*90}{RESET}\n")

def main():
	info()
	args = parse_args()

	os.makedirs(args.p, exist_ok=True)

	print(f'Arguments received: \
		\n r={args.r},\
		\n l={args.l},\
		\n p={args.p},\
		\n url={args.url}')

if __name__ == "__main__":
	main()

