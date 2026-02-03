#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: macarval <macarval@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/27 22:39:51 by macarval          #+#    #+#              #
#    Updated: 2025/11/27 23:07:44 by macarval         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import string
import os

from colorama import Fore, Style

def main():
	info()
	args = parser_args()

	if args.g:
		args.key = get_key(args.g)
		validate_key(args.key)
		store_key(args.key)
	elif args.k:
		args.key = get_key(args.k)
		generate_otp(args.key)

def info():
	print(f"{Fore.YELLOW}{'-'*90}{Style.RESET_ALL}")
	print(f"{Fore.MAGENTA}{Style.BRIGHT}{'🔐 ft_otp Module - One-Time Password Generator':^90}{Style.RESET_ALL}")
	message = 'This module generates secure one-time passwords (OTPs) for authentication purposes.'
	print(f"{Fore.CYAN}{message:^90}{Style.RESET_ALL}")
	print(f"{Fore.YELLOW}{'-'*90}{Style.RESET_ALL}\n")

def parser_args():
	'''
	Parse command-line arguments for the ft_otp module.
	Returns: argparse.Namespace: Parsed arguments.
	'''
	parser = argparse.ArgumentParser(
		description="ft_otp Module - One-Time Password Generator",
		usage=	f"{Fore.YELLOW}{Style.BRIGHT}python3 %(prog)s [-g ARG_FILE | -k KEY_FILE]{Style.RESET_ALL}"
	)

	group = parser.add_mutually_exclusive_group(required=True)

	group.add_argument('-g',
						type=str,
						metavar=('ARG_FILE'),
						help='Stores the provided hexadecimal key into an encrypted file.')

	group.add_argument('-k',
						type=str,
						metavar=('KEY_FILE'),
						help='Generates a new Time-based One-Time Password using the stored key.')

	return parser.parse_args()

def get_key(file_path):
	'''
	Read and return the content of the specified file.
	'''
	try:
		with open(file_path, 'r', encoding="utf-8") as f:
			key = f.read().strip()
	except FileNotFoundError:
		error_quick_exit(f"the file '{file_path}' does not exist.")
	except PermissionError:
		error_quick_exit(f"permission denied to read the file '{file_path}'.")
	except Exception as e:
		error_quick_exit(f"an error reading the file '{file_path}': {e}")

	return key

def validate_key(key):
	'''
	Validate the provided key for OTP generation.
	Args:
		key (str): The key to validate.
	'''
	if len(key) < 64:
		error_quick_exit("key must be at least 64 hexadecimal characters.")

	if len(key) % 2 != 0:
		error_quick_exit("key must have an even number of characters.")

	if not all(c in string.hexdigits for c in key):
		error_quick_exit("key must contain only hexadecimal characters (0-9, a-f).")

def error_quick_exit(message):
	print(f"{Fore.RED}{Style.BRIGHT}ft_otp: error: {message}\n{Fore.RESET}")
	exit(1)

def store_key(key):
	'''
	Store the provided key into a secure file.
	Args:
		key (str): The key to store.
	'''

	# Criptografar key

	fd = os.open("ft_otp.key", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
	with os.fdopen(fd, 'w', encoding="utf-8") as f:
		f.write(key)

	print(f"{Fore.GREEN}{Style.BRIGHT}Key was successfully saved in ft_otp.key!{Style.RESET_ALL}\n")

def generate_otp(key):
	'''
	Generate a one-time password using the provided key file.
	Args:
		key (str): The key used for OTP generation.
	'''

	hash =  HMAC(key, time)
	ofsset = hash[-1] & 0x0F
	binary = hash[ofsset:ofsset + 4]
	number = int.from_bytes(binary, byteorder='big') & 0x7FFFFFFF
	otp = binary % 1000000
	# otp = f"{otp:06d}"

	print(otp)

if __name__ == "__main__":
	main()
