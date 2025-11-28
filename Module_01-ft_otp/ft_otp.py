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

def info():
	print(f"{Fore.YELLOW}{'-'*90}{Style.RESET_ALL}")
	print(f"{Fore.MAGENTA}{'🔐 ft_otp Module - One-Time Password Generator':^90}{Style.RESET_ALL}")
	message = 'This module generates secure one-time passwords (OTPs) for authentication purposes.'
	print(f"{Fore.CYAN}{message:^90}{Style.RESET_ALL}")
	print(f"{Fore.YELLOW}{'-'*90}{Style.RESET_ALL}\n")

def parser_args():
	parser = argparse.ArgumentParser(description="ft_otp Module - One-Time Password Generator")
	group = parser.add_mutually_exclusive_group()

	group.add_argument('-g',
						type=str,
						nargs=1,
						metavar=('KEY'),
						help='Enable OTP generation using the provided KEY.')

	group.add_argument('-k',
						default=False,
						action='store_true',
						help='Enable key generation for OTP.')
	
	return parser.parse_args()


if __name__ == "__main__":
	main()
