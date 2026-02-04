# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tests.sh                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: macarval <macarval@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/30 11:03:02 by macarval          #+#    #+#              #
#    Updated: 2026/02/04 17:45:51 by macarval         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

# Run tests for OPP-01 -ex00
# Usage: make test -OU- make && ./test.sh

# Colors
red='\033[31;1m'
blue='\033[36;1m'
green='\033[32;1m'
yellow='\033[33;1m'
purple='\033[35;1m'
gray='\033[37;1m'
reset='\033[0m'

PROGRAM="./ft_otp.py"

KEY="000102030405060708090a0b0c0d0e0f000102030405060708090a0b0c0d0e0f"
FILE_HEX="key.hex"
FILE_KEY="ft_otp.key"
BAD_FILE="bad_key.hex"
TIMEOUT=1

cleanup() {
	rm -f $FILE_HEX $FILE_ENC $BAD_FILE .env
}

total_tests=0
successful_tests=0

comp="make re"

$comp
clear

echo
echo -e "${blue}-------------------------------------------------------------------------"
echo -e "************************* STARTING FT_OTP TESTS *************************"
echo -e "-------------------------------------------------------------------------"
echo -e  "${blue}1. Creating a temporary key file ($FILE_HEX)..."
echo -e "-------------------------------------------------------------------------${reset}"

echo -n $KEY > $FILE_HEX
echo -e "${green}Success: Temporary key file ($FILE_HEX) created.${reset}"


echo -e "${blue}\n-------------------------------------------------------------------------"
echo -e "2. Running registration (-g)..."
echo -e "-------------------------------------------------------------------------${reset}"

${PROGRAM} -g $FILE_HEX > /dev/null 2>&1

if [ ! -f "$FILE_KEY" ]; then
	echo -e "${red}Error: Key file ($FILE_KEY) was not created.${reset}"
	exit 1
else
	echo -e "${green}Success: Key file ($FILE_KEY) created successfully.${reset}"
fi


echo -e "${blue}\n-------------------------------------------------------------------------"
echo -e "3. Comparing generation (-k) with Oathtool (5 rounds)..."
echo -e "-------------------------------------------------------------------------${reset}"

for i in {1..5}
do
	((total_tests++))
	MY_OTP=$(${PROGRAM} -k $FILE_KEY | grep -o '[0-9]\{6\}' | tail -n 1)
	REF_OTP=$(oathtool --totp $KEY)

	echo -en "${yellow}Test ${purple}#$i: ${yellow}My OTP: ${purple}$MY_OTP ${reset}| ${yellow}Oathtool OTP: ${purple}$REF_OTP -> ${reset}"

	if [ "$MY_OTP" == "$REF_OTP" ]; then
		echo -e "${green}✅ Passed${reset}"
		((successful_tests++))
	else
		echo -e "${red}❌ Failed${reset}"
	fi

	sleep ${TIMEOUT}
done

echo -e "${blue}\n-------------------------------------------------------------------------"
echo -e "4. Testing short key..."
echo -e "-------------------------------------------------------------------------${reset}"

(( total_tests++ ))
echo -n "000102030405060708090a0b0c0d0e" > $BAD_FILE

ERROR_MSG=$(${PROGRAM} -g $BAD_FILE | tail -n 2 2>&1)

echo -en "${yellow}Test ${purple}#$total_tests: \n${red}${ERROR_MSG}\n${reset}"

if [[ $ERROR_MSG == *"error: key must be at least 64 hexadecimal characters."* ]]; then
	echo -e "${green}✅ Passed${reset}"
	((successful_tests++))
else
	echo -e "${red}❌ Failed${reset}"
fi


echo -e "${blue}\n-------------------------------------------------------------------------"
echo -e "5. Testing odd size..."
echo -e "-------------------------------------------------------------------------${reset}"

(( total_tests++ ))
echo -n "${KEY}1" > $BAD_FILE

ERROR_MSG=$(${PROGRAM} -g $BAD_FILE | tail -n 2 2>&1)

echo -en "${yellow}Test ${purple}#$total_tests: \n${red}${ERROR_MSG}\n${reset}"

if [[ $ERROR_MSG == *"error: key must have an even number of characters."* ]]; then
	echo -e "${green}✅ Passed${reset}"
	((successful_tests++))
else
	echo -e "${red}❌ Failed${reset}"
fi


echo -e "${blue}\n-------------------------------------------------------------------------"
echo -e "6. Testing for invalid characters..."
echo -e "-------------------------------------------------------------------------${reset}"

(( total_tests++ ))
echo -n "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ" > $BAD_FILE

ERROR_MSG=$(${PROGRAM} -g $BAD_FILE | tail -n 2 2>&1)

echo -en "${yellow}Test ${purple}#$total_tests: \n${red}${ERROR_MSG}\n${reset}"

if [[ $ERROR_MSG == *'error: key must contain only hexadecimal characters (0-9, a-f).'* ]]; then
	echo -e "${green}✅ Passed${reset}"
	((successful_tests++))
else
	echo -e "${red}❌ Failed${reset}"
fi


echo -e "${blue}\n-------------------------------------------------------------------------"
echo -e "7. Testing for a non-existent file..."
echo -e "-------------------------------------------------------------------------${reset}"

(( total_tests++ ))
ERROR_MSG=$(${PROGRAM} -g non_existent_file | tail -n 2 2>&1)

echo -en "${yellow}Test ${purple}#$total_tests: \n${red}${ERROR_MSG}\n${reset}"

if [[ $ERROR_MSG == *"error: the file 'non_existent_file' does not exist."* ]]; then
	echo -e "${green}✅ Passed${reset}"
	((successful_tests++))
else
	echo -e "${red}❌ Failed${reset}"
fi

echo -e "${blue}\n-------------------------------------------------------------------------"
echo -e "Tests finished..."
echo -e "-------------------------------------------------------------------------${reset}"

echo -e "\n${yellow}Cleaning up temporary files...${reset}"
cleanup
echo -e "${green}Cleanup completed.${reset}"

# Calculate percentage of hits
percentage=$(echo "scale=4; $successful_tests / $total_tests * 100" | bc)

# Print results with color
echo -en "\n\e[33mTotal number of tests performed: \e[94m$total_tests"
echo -en "\n\e[33mTests OK: \e[94m$successful_tests"
echo -e "\n\e[33mPercentage of hits: \e[94m$(printf "%.2f" "$percentage")%\n"

if [ "$(printf "%.2f" "$percentage")" = "100.00" ]; then
	echo -e "${green}------------------------ 𝙲𝚘𝚗𝚐𝚛𝚊𝚝𝚞𝚕𝚊𝚝𝚒𝚘𝚗𝚜!!!🎉🎊 ------------------------\n"
else
	echo -e "${red}------------------------- 𝚄𝚗𝚏𝚘𝚛𝚝𝚞𝚗𝚊𝚝𝚎𝚕𝚢!!!⛔😩 --------------------------\n"
fi
