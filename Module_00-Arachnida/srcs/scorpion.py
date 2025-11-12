# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: macarval <macarval@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/12 12:31:36 by macarval          #+#    #+#              #
#    Updated: 2025/11/12 17:42:18 by macarval         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import argparse

from colors import CYAN, BPURPLE, BYELLOW, BRED, RESET

def valid_extentions(files):
	valid_exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}

	return all(any(file.lower().endswith(ext)
				for ext in valid_exts)
				for	file in files)


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

def info():
	print(f"\n{BYELLOW}{'-'*90}{RESET}")
	print(f"{BPURPLE}{'🦂 Scorpion Module - Arachnida':^90}{RESET}")
	print(f"{CYAN}{'This module extracts, modifies, or deletes metadata from image files.':^90}{RESET}")
	print(f"{BYELLOW}{'-'*90}{RESET}\n")

def main():
	info()
	args = parse_args()

	if not valid_extentions(args.files):
		return print(f"{BRED}No valid image files provided. Supported "
			   		 f"extensions are .jpg, .jpeg, .png, .gif, .bmp.{RESET}")

	print(f'Arguments received: \
		\n m={args.m},\
		\n d={args.d}')

	for i, file in enumerate(args.files, start=1):
		print(f' file{i}={file}')

if __name__ == "__main__":
	main()
