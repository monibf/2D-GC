#!/usr/bin/env bash

NC='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
printf "Checking Dependencies...\n"

printf "curl: "
if ! [[ -x "$(command -v curl)" ]]; then
    printf "${RED}NO${NC}\n"
    printf "Please install curl to continue\n"
    exit
fi
printf "${GREEN}YES${NC}\n"

printf "python3: "
if ! [[ -x "$(command -v python3)" ]]; then
    printf "${RED}NO${NC}\n"
    printf "Please install python3 to continue\n"
    exit
fi
printf "${GREEN}YES${NC}\n"

printf "pip3: "
if ! [[ -x "$(command -v pip3)" ]]; then
    printf "${RED}NO${NC}\n"
    printf "Please install pip3 to continue\n"
    exit
fi
printf "${GREEN}YES${NC}\n"
printf "Installing GC-2D...\n"
pip3 install .