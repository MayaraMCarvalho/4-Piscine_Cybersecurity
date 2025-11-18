# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: macarval <macarval@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/12 12:31:36 by macarval          #+#    #+#              #
#    Updated: 2025/11/18 15:14:25 by macarval         ###   ########.fr        #
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

	valid_extensions(args.files)
	get_metadata(args)

	print(f"\n{BBLUE}Metadata processing completed!{RESET}\n")

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

def valid_extensions(files):
	valid_exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}

	for file in files:
		if not file.lower().endswith(tuple(valid_exts)):
			print (f"{YELLOW}Warning: File '{file}' does not have a "
				f"valid image extension.{RESET}\n")

def get_metadata(args):
	"""
	Process each image file to extract, modify, or delete metadata.
	"""
	for name in args.files:
		try:
			img = Image.open(name)
			data = img.getexif()

			if (args.d):
				delete_metadata(img, name, data)
				continue

			if (args.m):
				modify_metadata(img, name, data, args)
				data = update_image(img, name)

			display_metadata(name, data)

		except FileNotFoundError:
			print(f"{BRED}Error: File '{name}' not found.{RESET}")

		except UnidentifiedImageError:
			print(f"{BRED}Error: File '{name}' is not a valid image.{RESET}")

		except Exception as e:
			print(f"{BRED}Error: Unexpected error while processing "
		 			f"'{name}': {e}{RESET}")
		finally:
			if img:
				img.close()

def delete_metadata(img, name, data):
	print(f"{BRED}\n--- Deleting metadata from {name}---{RESET}")
	data.clear()
	img.save(name, exif=data.tobytes())

def modify_metadata(img, name, data, args):
	"""
	Modify specified metadata tag in the image.
	"""
	print(f"{BYELLOW}\n--- Modifying metadata of {name} ---{RESET}")

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
		return True
	except Exception:
		print(f"{BRED}Error: Incompatible data type for the tag '{tag}'.{RESET}")
		return False

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
	"""
	Display the metadata of the image in a readable format.
	"""
	if not data:
		print(f"{WHITE}No EXIF metadata found for {name}.{RESET}")
		return

	dictionary = create_dictionary(data)
	if not dictionary:
		print(f"{WHITE}Image {name} does not contain known EXIF tags."
			f"{RESET}")
	else:
		print_metadata(name, dictionary)

def create_dictionary(data):
	"""
	Create a dictionary of EXIF tags and their values.
	"""
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
