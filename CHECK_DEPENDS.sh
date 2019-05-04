#!/usr/bin/env bash

printf "Checking python3 is installed: "
if [[ -x $(command -v python3) ]]; then
    printf "YES\n"
    PYTHON=$(command -v python3)
else
    printf "NO\n"
    printf "Please install the latest version of python3 from https://www.python.org/downloads/"
    exit 1
fi

printf "Checking pip3 is installed: "
if [[ -x $(command -v pip3 --disable-pip-version-check) ]]; then
    printf "YES\n"
    PIP=$(command -v pip3 --disable-pip-version-check)
else
    printf "NO\n"
    printf "Please install the latest version of pip from https://pip.pypa.io/en/stable/installing/"
fi

printf "Checking PyInstaller is installed: "
if [[ $("$PIP" --disable-pip-version-check list | grep PyInstaller) ]]; then
    printf "YES\n"
else
    printf "NO\n"
    printf "Installing PyInstaller...\n"
    "$PIP" install --user PyInstaller
fi

printf "Installing Dependencies..."
"$PIP" install --user -r requirements.txt
