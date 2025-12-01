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

from colorama import Fore, Style

def main():
	info()
	args = parser_args()
	validate_args(args)

	if args.g:
		generate_otp(args.g)
	elif args.k:
		generate_key()

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
	parser = argparse.ArgumentParser(description="ft_otp Module - One-Time Password Generator")
	group = parser.add_mutually_exclusive_group()

	group.add_argument('-g',
						type=str,
						nargs=1,
						metavar=('FILE_KEY'),
						help='Enable OTP generation using the provided KEY.')

	group.add_argument('-k',
						default=False,
						action='store_true',
						help='Enable key generation for OTP.')

	return parser.parse_args()

def validate_args(args):
	'''
	Validate the parsed command-line arguments.
	Args: argparse.Namespace: Parsed arguments.
	'''
	if not args.g and not args.k:
		print(f"{Fore.RED}{Style.BRIGHT}Error: You must provide either the -g or -k option.{Style.RESET_ALL}")
		exit(1)

def generate_otp(file_key):
	'''
	Generate a one-time password using the provided key file.
	Args:
		file_key (str): Path to the key file.
	'''
	
	print(f"{Fore.GREEN}Generating OTP using key: {file_key}{Style.RESET_ALL}\n")
	# Here you would implement the actual OTP generation algorithm

def generate_key():
	# Placeholder for key generation logic
	print(f"{Fore.GREEN}Generating a new secure key for OTP.{Style.RESET_ALL}\n")
	# Here you would implement the actual key generation algorithm

if __name__ == "__main__":
	main()
