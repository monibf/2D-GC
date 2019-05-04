#!/usr/bin/env bash
if [[ -z "$INSTALL_LOCATION" ]]; then
 INSTALL_LOCATION="$HOME/Applications"
fi
if [[ -z "$NAME" ]]; then
    NAME="2D-GC"
fi

if [[ $OSTYPE != "darwin"* ]]; then
    echo "This install script is only for OSX! Please use the other."
    exit 1
fi

./CHECK_DEPENDS.sh

if [[ $? != 0 ]]; then
    exit 1
elif [[ -d "python" ]]; then
    PYTHON=python3/bin
    pass
else
    PYTHON=$(command -v python3)
fi

echo "Installing $NAME..."
"$PYTHON" -m PyInstaller --noconfirm --onefile --windowed \
 --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' \
 --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' \
 --name="$NAME" gc2d/__main__.py

# make it HDPI Compatible.
plutil -replace NSHighResolutionCapable -bool true "dist/$NAME.app/Contents/Info.plist"

# move it to user Applications.
cp -r "dist/$NAME.app" "$HOME/Applications/$NAME.app"

echo "Install Complete!"