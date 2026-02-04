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
import base64
import string
import os
import time
import hmac
import hashlib
import qrcode # type: ignore

from colorama import Fore, Style
from cryptography.fernet import Fernet
from dotenv import load_dotenv # type: ignore

def main():
	info()
	args = parser_args()

	try:
		if args.g:
			content = read_file(args.g)
			validate_key(content)

			make_qr(content)
			print(f"{Fore.GREEN}{Style.BRIGHT}QR code saved as ft_otp_qr.png!{Style.RESET_ALL}")

			store_key(content)
			print(f"{Fore.GREEN}{Style.BRIGHT}Key was successfully saved in ft_otp.key!{Style.RESET_ALL}\n")

		elif args.k:
			content = read_file(args.k)
			otp_code = generate_otp(content)
			print(otp_code)

	except Exception as e:
		error_quick_exit(str(e))

def info():
	print(f"{Fore.YELLOW}{'-'*90}{Style.RESET_ALL}")
	print(f"{Fore.MAGENTA}{Style.BRIGHT}{'🔐 ft_otp Module - One-Time Password Generator':^90}{Style.RESET_ALL}")
	message = 'This module generates secure one-time passwords (OTPs) for authentication purposes.'
	print(f"{Fore.CYAN}{message:^90}{Style.RESET_ALL}")
	print(f"{Fore.YELLOW}{'-'*90}{Style.RESET_ALL}\n")

def parser_args():
	'''
	Parse command-line arguments for the ft_otp module.
	Returns:
		argparse.Namespace: Parsed arguments.
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

def read_file(file_path):
	'''
	Read the content of a file.
	Args:
		file_path (str): The path to the file.
	Returns:
		str: The content of the file.
	'''
	try:
		with open(file_path, 'r', encoding="utf-8") as f:
			content = f.read().strip()
	except FileNotFoundError:
		error_quick_exit(f"the file '{file_path}' does not exist.")
	except PermissionError:
		error_quick_exit(f"permission denied to read the file '{file_path}'.")
	except Exception as e:
		error_quick_exit(f"an error reading the file '{file_path}': {e}")

	return content

def validate_key(key):
	'''
	Validate the provided key for OTP generation.
	Args:
		key (str): The key to validate.
	'''
	if len(key) < 64:
		raise ValueError("key must be at least 64 hexadecimal characters.")

	if len(key) % 2 != 0:
		raise ValueError("key must have an even number of characters.")

	if not all(c in string.hexdigits for c in key):
		raise ValueError("key must contain only hexadecimal characters (0-9, a-f).")

def make_qr(key):
	'''
	Generate a QR code for the provided key.
	Args:
		key (str): The key to encode in the QR code.
	'''
	key_bytes = bytes.fromhex(key)
	key_base32 = base64.b32encode(key_bytes).decode('utf-8').replace('=', '')

	otp_uri = f"otpauth://totp/ft_otp:macarval?secret={key_base32}&issuer=ft_otp"
	qr = qrcode.QRCode(version=1, box_size=10, border=5)
	qr.add_data(otp_uri)
	qr.make(fit=True)

	img = qr.make_image(fill='black', back_color='white')
	img.save("ft_otp_qr.png")

def store_key(key):
	'''
	Store the provided key into a secure file.
	Args:
		key (str): The key to store.
	Returns:
		bool: True if the key was stored successfully.
	'''
	crypt = save_fernet_key()

	f = Fernet(crypt)
	token = f.encrypt(key.encode('utf-8'))

	fd = os.open("ft_otp.key", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
	with os.fdopen(fd, 'w', encoding="utf-8") as f:
		f.write(token.decode('utf-8'))

def save_fernet_key():
	'''
	Save the Fernet key used for encryption/decryption.
	'''
	crypt = Fernet.generate_key().decode('utf-8')

	fd = os.open(".env", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
	with os.fdopen(fd, 'w', encoding="utf-8") as f:
		f.write(f"FERNET_KEY={crypt}\n")

	return crypt

def generate_otp(key):
	'''
	Generate a one-time password using the provided key file.
	Args:
		key (str): The key used for OTP generation.
	Returns:
		str: The generated OTP.
	'''
	key = decrypt_key(key)
	key_bytes = bytes.fromhex(key)

	now = time.time() // 30
	time_bytes = int(now).to_bytes(8, byteorder='big')

	hash = hmac.new(key_bytes, time_bytes, hashlib.sha1).digest()
	offset = hash[-1] & 0x0F
	binary = hash[offset:offset + 4]
	number = int.from_bytes(binary, byteorder='big') & 0x7FFFFFFF
	otp = number % 1000000
	otp = f"{otp:06d}"

	return otp

def decrypt_key(content):
	'''
	Load and decrypt the Fernet key from environment variables.
	Args:
		key (str): The encrypted key to decrypt.
	Returns:
		str: The decrypted key.
	'''
	load_dotenv()

	crypt = os.environ.get('FERNET_KEY')
	if not crypt:
		error_quick_exit("Fernet key not found in environment variables.")

	try:
		f = Fernet(crypt)
		key = f.decrypt(content.encode('utf-8')).decode('utf-8')
	except Exception:
		error_quick_exit("invalid token. Unable to decrypt the key.")

	return key

def error_quick_exit(message):
	'''
	Print an error message and exit the program.
	Args:
		message (str): The error message to display.
	'''
	print(f"{Fore.RED}{Style.BRIGHT}ft_otp: error: {message}\n{Fore.RESET}")
	exit(1)

if __name__ == "__main__":
	main()
