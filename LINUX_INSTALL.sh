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

./CHECK_DEPENDS.sh

if [[ $? != 0 ]]; then
    exit 1
elif [[ -d "python3" ]]; then
    # maybe one day I'll get this to work.
    pass
else
    PYTHON=$(command -v python3)
fi

echo "Installing $NAME..."
"$PYTHON" -m PyInstaller --noconfirm --onefile --windowed \
 --distpath="INSTALL_LOCATION" \
 --name="$NAME" gc2d/__main__.py

echo "Install Complete!"