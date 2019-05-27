# GC2D
A visualisation and analysis tool for two dimensional chromatography data.

## Features
 - 1D, 2D and 3D representations of GCxGC data.
 - Integration and convolution support.
 - Importing of pre-formatted, comma separated GCxGC data.

## Launching without installing
**NOTE:** Execution in the manner is heavily dependent on the python environment. Any changes to the source code, the
python installation or the required dependencies could result in unexpected behavior.

Please ensure that you have python3 installed, you can get it from [www.python.org](https://www.python.org/downloads/).
Also insure that you have installed the requirements. To do this, execute the following command from the project root
directory in a terminal or cmd:

Windows: `py -3 -m pip install -r requirements.txt`

OSX/Linux: `pip3 install -r requirements.txt`

You can then execute your operating systems respective launch script.

## Installation

### Prerequisites

For all operating systems the installers require that you have installed:

- python3
- pip3 (This is usually installed with python3)
- git

All the scripts will check that you have the required programs. The Windows installer is capable of downloading and
installing python3 for you, however it is highly recommended that you install it yourself.

**NOTE:** If you already have python3 installed, you may wish to setup a new environment before running the installer to
avoid having all of GC2D's dependencies installed into your current environment. They will not be removed post 
installation.

**NOTE:** The installers can take quite some time to build GC-2D, especially on slower systems. Don't be worried if it
doesn't seem to be doing anything, particularly when it's `Building PKG (CArchive) PKG-000.pkg`.


### Windows
Run the `WINDOWS_INSTALL.bat`. This will walk you through this installation and install
all required dependencies. 

If python3 is not installed the installer can attempt to download and install python 3.7.3.
Alternatively install it yourself from [www.python.org](https://www.python.org/downloads/).
In theory, any version of python3 will work, however development and testing was done with
python 3.7 so if at all possible use that version. 

**NOTE:** If attempting to install on windows XP, you will need to manually install python 3.4.
Newer versions of python3 cannot be installed on XP.

**NOTE:** If the python3 is installed by the installer, it will ask whether you wish to uninstall python3 afterwards.
Doing so will not completely remove python3. The python3 uninstaller will leave `py` installer.
This can be uninstalled from the `ControlPanel -> Uninstall a Program`.
 
**NOTE:** GC2D is installed to `%LOCALAPPDATA%`, and shortcuts are created in the start menu.
The registry is also edited. The uninstaller will completely remove these changes.
User configurations and preferences are saved in `%APPDATA%` and will **NOT** be removed by the uninstaller.

#### Troubleshooting

- If the installer fails to install python3, try installing it yourself from 
[www.python.org](https://www.python.org/downloads/).
- The Installer requires Internet access to install the dependencies for GC2D, if you need to run GC2D on an
un-networked PC, you can create a portable executable on another PC with `WINDOWS_CREATE_PORTABLE.bat` and transfer it.
This will only work between the same Windows version and architecture.

### OSX

If you don't already have python3 installed, install it from [www.python.org](https://www.python.org/downloads/), 
Python 3.7 is prefered, however any version of python3 will probably work.

Run `OSX_INSTALL.command`, either by starting it in a terminal, or by double clicking in Finder.

GC2D will now be installed as an App in your user Applications directory and it should be visible in launcher. 

### Linux/Other
**NOTE:** This may or may not work for you. We have found that praying to the mighty God of Linux, Linus Torvalds, will
increase the chance of success.

For Linux and all other systems with a bash interpreter:
- Install python3 if it isn't installed already. Please refer to your distribution help documentation for how to do 
that.
- Run the `LINUX_INSTALL.sh` script from the project directory. This will create a soft link called `2D-GC` to the 
`LAUNCH_LINUX.sh` script. You can then put this script anywhere on the `PATH` and it will be executable from the 
terminal.

#### Troubleshooting

The `2D-GC` link is dependent on the current location of the 2D-GC source folder. If you move or delete this folder, the
link will no longer work.

## Uninstallation

### Windows

Navigate to `Control Panel -> Uninstall a Program` and select GC2D like you would any other program.
This will remove the files from `%LOCALAPPDATA%`, the start menu shortcuts
and the GC2D entries in the registry. Desktop shortcuts will not be deleted.

Portable executables do not need uninstalling, just delete the executable.

### OSX

Simply delete `GC2D.app` from your local Applications directory like you would any other app.
User preferences will not be removed. To also remove these delete the `$HOME/.gc2d` directory.

### Linux/Other
Remove the `2D-GC` link from your path.
User preferences can be found in `$HOME/.gc2d`, delete this folder to completely uninstall.

## Custom Color Palettes
User defined color palettes can be imported from the `choose palette` dialog. Imported palettes are saved into
`~/.GC-2D/palettes`. Custom Palettes can be defined in a plain text file ending with `.palette`, with each line 
containing the comma separated rgb values defining a color, each component can have a value from 0-255. 
The first line is the color for the lowest value, the last line is the color for the highest value.

For example, the common color palette jet can be defined like so:

### jet.palette:
```
  0,   0, 127
  0,   0, 255
  0, 127, 255
  0, 255, 255
127, 255, 127
255, 255,   0
255, 127,   0
255,   0,   0
127,   0,   0
```
**NOTE:** Spaces and leading zeros are ignored. `0 ,   001,000 == 0,1,0`

# TODO
- Uninstaller asks if user preferences/configurations should be deleted (100% removal).