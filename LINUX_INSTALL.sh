#!/usr/bin/env bash
if [[ -z "$INSTALL_LOCATION" ]]; then
 INSTALL_LOCATION=.
fi
if [[ -z "$NAME" ]]; then
    NAME="2D-GC"
fi

if [[ $OSTYPE != "linux"* ]]; then
    echo "This install script is intended only for Linux! Please use another!"
    exit 1
fi

printf "Checking python3 is installed: "
if [[ -x $(command -v python3) ]]; then
    printf "YES\n"
    PYTHON=$(command -v python3)
else
    printf "NO\n"
    printf "Please install the latest version of python3 see the README.md for help."
    exit 1
fi

printf "Checking pip3 is installed: "
if [[ -x $(command -v pip3 --disable-pip-version-check) ]]; then
    printf "YES\n"
    PIP=$(command -v pip3 --disable-pip-version-check)
else
    printf "NO\n"
    printf "Please install the latest version of pip see the README.md for help."
    exit 1
fi

printf "Checking PyInstaller is installed: "
if [[ $("$PIP" --disable-pip-version-check list | grep PyInstaller) ]]; then
    printf "YES\n"
else
    printf "NO\n"
    printf "Installing PyInstaller...\n"
    "$PIP" install --user PyInstaller
fi

printf "Installing Dependencies...\n"

"$PIP" install --user -r requirements.txt

echo "Installing $NAME..."
"$PYTHON" -m PyInstaller --noconfirm --windowed \
 --distpath="$INSTALL_LOCATION" \
 --name="$NAME" gc2d/__main__.py
if [[ $? != 0 ]]; then
    exit 1
fi
echo "Install Complete!"