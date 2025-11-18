# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: macarval <macarval@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/12 12:31:36 by macarval          #+#    #+#              #
#    Updated: 2025/11/18 12:09:10 by macarval         ###   ########.fr        #
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
		print(args.files)
		error_quick_exit("No valid image files provided. Supported "
						"extensions are .jpg, .jpeg, .png, .gif, .bmp.")

	get_metadata(args)

def info():
	print(f"{BYELLOW}{'-'*90}{RESET}")
	print(f"{BPURPLE}{'🦂 Scorpion Module - Arachnida':^90}{RESET}")
	message = 'This module extracts, modifies, or ' \
	'deletes metadata from image files.'
	print(f"{CYAN}{message:^90}{RESET}")
	print(f"{BYELLOW}{'-'*90}{RESET}\n")

def	 parse_args():
	parser = argparse.ArgumentParser(description="Scorpion Module - Arachnida")
	group = parser.add_mutually_exclusive_group()

	group.add_argument('-m',
						type=str,
						nargs=2,
						metavar=('TAG', 'VALUE'),
						help='Enable metadata modify from images.')

	group.add_argument('-d',
						default=False,
						action='store_true',
						help='Enable metadata delete from images.')

	parser.add_argument('files',
						type=str,
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
	for name in args.files:
		try:
			img = Image.open(name)
			data = img.getexif()

			if (args.d):
				delete_metadata(img, name, data)
				img.close()
				continue

			if (args.m):
				modify_metadata(img, name, data, args)
				data = update_image(img, name)

			display_metadata(name, data)
			img.close()

		except FileNotFoundError:
			print(f"{BRED}Error: File '{name}' not found.{RESET}")

		except UnidentifiedImageError:
			print(f"{BRED}Error: File '{name}' is not a valid image.{RESET}")

		except Exception as e:
			print(f"{BRED}Unexpected error while processing "
		 			f"'{name}': {e}{RESET}")

def delete_metadata(img, name, data):
	print(f"{BRED}--- Deleting metadata from {name}---{RESET}")
	data.clear()
	img.save(name, exif=data.tobytes())

def modify_metadata(img, name, data, args):
	print(f"{BYELLOW}--- Modifying metadata of {name} ---{RESET}")

	tag, value = args.m
	if tag not in ExifTags.TAGS.values():
		print(f"{BRED}Error: Tag '{tag}' is not a recognized EXIF tag.{RESET}")
		return

	tag_id	= next((k for k, v in ExifTags.TAGS.items() if v == tag), None)
	if tag_id is None:
		print(f"{BRED}Error: Tag '{tag}' could not be found {RESET}")
		return

	value = convert_value(value)
	data[tag_id] = value

	try:
		img.save(name, exif=data.tobytes())
		print(f"{BGREEN}Successfully modified '{tag}' to '{value}' in {name}.{RESET}")
	except Exception:
		print(f"{BRED}Error: Incompatible data type for the tag '{tag}'.{RESET}")

def convert_value(value):
	try:
		return int(value)
	except ValueError:
		pass

	try:
		return float(value)
	except ValueError:
		pass

	return value

def update_image(img, name):
	img.close()
	img	= Image.open(name)
	return img.getexif()

def display_metadata(name, data):
	if data:
		dictionary = create_dictionary(data)

		if not dictionary:
			print(f"{CYAN}Image {name} does not contain known EXIF tags.\
		 		{RESET}\n")
		else:
			print_metadata(name, dictionary)
	else:
		print(f"{WHITE}No EXIF metadata found for {name}.{RESET}")


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

if __name__ == "__main__":
	main()
