#!/usr/bin/env bash

printf "Checking python3 is installed: "
if [[ -x $(command -v python3) ]]; then
    printf "YES\n"
else
    printf "NO\n"
    printf "Please install python3...\n"
    exit 1
fi

printf "Checking pip3 is installed: "
if [[ -x $(command -v pip3) ]]; then
    printf "YES\n"
else
    printf "NO\n"
    printf "Please install pip3...\n"
    exit 1
fi

printf "Checking PyInstaller is installed: "
if [[ $(pip3 --disable-pip-version-check list | grep PyInstaller) ]]; then
    printf "YES\n"
else
    printf "NO\n"
    printf "Installing PyInstaller...\n"
    pip3 install PyInstaller
fi

printf "Installing Dependencies..."
pip3 install -r requirements.txt
