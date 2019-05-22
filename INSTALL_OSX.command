#!/usr/bin/env bash
cd `dirname $0`
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
    exit 1
fi

printf "Checking PyInstaller is installed: "
if [[ $("$PIP" --disable-pip-version-check list | grep PyInstaller) ]]; then
    printf "YES\n"
else
    printf "NO\n"
    printf "Installing PyInstaller...\n"
    "$PIP" install PyInstaller
fi

printf "Installing Dependencies...\n"
"$PIP" install -r requirements.txt

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
 --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' \
 --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' \
 --name="$NAME" gc2d/__main__.py

# make it HDPI Compatible.
plutil -replace NSHighResolutionCapable -bool true "dist/$NAME.app/Contents/Info.plist"

# move it to user Applications.
cp -r "dist/$NAME.app" "$INSTALL_LOCATION/$NAME.app"

echo "Install Complete!"