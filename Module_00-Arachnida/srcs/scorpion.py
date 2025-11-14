# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: macarval <macarval@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/12 12:31:36 by macarval          #+#    #+#              #
#    Updated: 2025/11/14 00:42:43 by macarval         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import argparse

from PIL import Image, UnidentifiedImageError, ExifTags
from colors import YELLOW, CYAN, WHITE
from colors import BRED, BGREEN, BYELLOW, BBLUE, BPURPLE, BCYAN, RESET

def main():
	info()
	args = parse_args()

	if not valid_extentions(args.files):
		error_quick_exit("No valid image files provided. Supported "
						"extensions are .jpg, .jpeg, .png, .gif, .bmp.")

	get_metadata(args)

def info():
	print(f"\n{BYELLOW}{'-'*90}{RESET}")
	print(f"{BPURPLE}{'🦂 Scorpion Module - Arachnida':^90}{RESET}")
	print(f"{CYAN}{'This module extracts, modifies, or deletes metadata from image files.':^90}{RESET}")
	print(f"{BYELLOW}{'-'*90}{RESET}\n")

def	 parse_args():
	parser = argparse.ArgumentParser(description="Scorpion Module - Arachnida")
	group = parser.add_mutually_exclusive_group()

	group.add_argument('-m',
						default=False, #mudar para padrão
						action='store_true', # retirar quando entender o que receber
						help='Enable metadata modify from images.')

	group.add_argument('-d',
						default=False,
						action='store_true',
						help='Enable metadata delete from images.')

	parser.add_argument('files',
						nargs='+',
						help= 'Path to the file to extract metadata.')

	return parser.parse_args()

def valid_extentions(files):
	valid_exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}

	return all(any(file.lower().endswith(ext)
				for ext in valid_exts)
				for	file in files)

def error_quick_exit(message):
	print(f"{BRED}{message}{RESET}")

	exit(1)

def get_metadata(args):
	for image in args.files:
		try:
			img = Image.open(image)
			data = img.getexif()

			# if (args.m):
				#implementar

			if (args.d):
				delete_metadata(img, image, data)
				img.close()
				continue

			if data:
				dictionary = create_dictionary(data)
				if not dictionary:
					print(f"{CYAN}Image {image} does not contain known EXIF ​​tags.{RESET}\n")
				else:
					print_metadata(image, dictionary)
			else:
				print(f"{WHITE}No EXIF metadata found for {image}.{RESET}")
			img.close()

		except FileNotFoundError:
			print(f"{BRED}Error: File '{image}' not found.{RESET}")

		except UnidentifiedImageError:
			print(f"{BRED}Error: File '{image}' is not a valid image.{RESET}")

		except Exception as e:
			print(f"{BRED}Unexpected error while processing "
		 			f"'{image}': {e}{RESET}")

def create_dictionary(data):
	dictionary = {}

	if data:
		for id, value in data.items():
			tag_name = ExifTags.TAGS.get(id)
			if tag_name:
				dictionary[tag_name] = value

	return dictionary

def print_metadata(image, dict):
	print(f"{BGREEN}\n--- Metadados de {BBLUE}{image} "
		 			f"{BGREEN}---{RESET}")

	for tag, value in dict.items():
		value_format = value
		if isinstance(value, bytes):
			value_format = value.decode('utf-8', errors='ignore')
		print (f"{BCYAN}{tag: <20}: {BPURPLE}{value_format}{RESET}")
	print("\n")

def	delete_metadata(img, name, data):
	print(f"{BRED}--- Deleting metadata from {name}---{RESET}")
	data.clear()
	img.save(name, exif=data)


if __name__ == "__main__":
	main()
