# GC2D USER GUIDE
## INSTALLITION GUIDE

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

### Linux/Other
**NOTE:** This may or may not work for you. We have found that praying to the mighty God of Linux, Linus Torvalds, will
increase the chance of success. If you are familiar with pip, you may prefer the pip installation below.

For Linux and all other systems with a bash interpreter:
- Install python3 if it isn't installed already. Please refer to your distribution help documentation for how to do 
that.
- Run the `LINUX_INSTALL.sh` script from the project directory. This will create a soft link called `2D-GC` to the 
`LAUNCH_LINUX.sh` script. You can then put this script anywhere on the `PATH` and it will be executable from the 
terminal.

#### Troubleshooting

The `2D-GC` link is dependent on the current location of the 2D-GC source folder. If you move or delete this folder, the
link will no longer work.

### Pip

An alternative is to install the application with [Pip](https://pip.pypa.io/en/stable/)
- Install python3 and pip for python3 if those aren't installed already
- On the command line, go to the project root directory (the directory where setup.py and requirements.txt are located)
- Run `pip3 install --user -r requirements.txt`
- Run `pip3 install --user .` (assuming that you're still in the same directory as setup.py)
- To launch the project, run `python3 -m gc2d`

**NOTE:** On mac OSX you need to install the latest pyqtgraph from github rather than from pip. There is a bug for HDPI screens that has been fixed in the later development versions but that is not yet included in the latest release.
If you install it in the order show here everything should work correctly, but if not you may need to uninstall pyqtgraph (`pip3 uninstall pyqtgraph` if it was installed through pip) and `pip3 install --user -r requirements.txt` again.

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

### Pip

Run `pip3 uninstall gc2d-rug`.
This does not uninstall dependencies (pyqtgraph, numpy, etc.). To install dependencies use [pip-autoremove](https://github.com/invl/pip-autoremove).


## USING THE PROGRAM

### Navigating the main window
The GCGC program opens in the main window which consists of the the following elements

- A menu bar containing a file, edit, view, tools and help menu
- A toolbar containing a show transformed data, set transformation, choose palette, draw selection and export option
- A viewport with 3 different docks named 1D, 2D and 3D
- An integration list
- A status bar

#### Switching view
By default the GCGC program has it's 3 view docks in the same location within the main window such that it is required to switch view in order to view another graph. This can be done bly clicking one of the blue bars named either '1D', '2D' or '3D', which will switch the view to the corresponding graph.

#### Editing user interface
The relative position of the 1D view, 2D view, 3D view and the integration list can be changed within the main view if the user so desires. The view docks can be moved by clickking the blue-bar named either 1D, 2D or 3D and drag and dropping it somewhere within the main window which will move the view to this position. Similarly the intregation list can be moved by dragging and dropping the vertical bar name 'integration'. Each individual element can also be taken outside the main window to create a seperate window on it's own by double clicking it's corresponding blue bar, whenever this specific window is then closed it's element is moved back into the main window.


### File menu
The file menu allows for the opening and saving of files, saving preferences and quitting the program. It can be opened by clicking 'file' in the menu bar in the top-left corner.

#### Opening files
Using the 'Open' option (CTRL + O) in the file menu, the user can open previously save .gcgc files. This will load it's corresponding data set, preferences set and integration areas.

#### Import data
Using the 'Import data' option (CTRL + O) in the file menu, the user can import a new chromatogram data set of type .gcgc, .txt or .csv

#### Save file
Using the 'Save' option (CTRL + S) in the file menu, the user can save the current project. In case the project is saved under an existing .gcgc file, 'save' will overwrite this file. In case the project has not been saved previously, 'save' will call the 'save as' option.

#### Save file as
Using the 'Save as' option (CTRL + SHIFT + S) in the file menu, the user can save the current project by creating a new .gcgc save file.

#### Saving integration areas
Using the 'save integration areas' option in the file menu, the user can save the existing integration areas label and values to a new safe file of type .gcgc.

#### Saving preferences
Using the 'save preference' option in the file menu, the user can save the preference, such as set in the current project to a .gcgc file.

#### Saving 3D plot
Using the 'export 2D plot' option in the file menu, the user can save the current 2D view as a .png file. 

#### Saving 2D plot
Using the 'export 3D plot' option in the file menu, the user can save the current 3D view as a .png file

#### Quitting GCGC
Using the 'quit' option (CTRL + Q) in the file menu, the user can terminate the program


### Setting transformations
Using the 'Set tranformation' option in the toolbar or in the tool menu, the user can set certain data transformation affecting integration areas. In order to apply and visualize the transformation set, the 'show transformed data' option in the toolbar needs to be toggled on. Similarly the data transformation can be toggled off by selecting the 'show transformed data' again.

***Note:*** No transformation can be set in case no data has been imported

#### Static cut off
The static cut off transformation of the data transforms the data such that over the entire plot a certain value is deducted from the z-value. In case the deduction is greater than the  original z-value, the z-value is set to 0.

### Dynamic cut off
The dynamic cut off transformation of the data transforms the data such that over the entire plot a certain value based on the given lowest percentile of z-values is deducted from each z-value of the plot. This transformation offers 2 ways of transforming, basing the cutoff on a given lowest percentile or transforming based on the mean of this given lowest percentile. Negative z-values after cut off are set to 0.

### Gaussian convolution
The Gaussian convolution is a transformation of the data based on the process of Gaussian smoothing for which a sigma can be selected.

### Min 1D convolution


### Setting color pallet
Using the 'choose pallet' option in the tooblar or in the view menu (CTRL + SHIFT + C), the user can switch collor pallet which shades the 2D and 3D graphs. By default the GCGC program comes with 3 premade collor pallets to choose from: jet, red-green-blue and viridis. The pallet picker also allows the user to select a an upper and lower bound to the pallet, enabling the user to set the point from which z-value a peak is assigned the minimum or maximum color. The pallet picker als enables the user the import a custom made color pallet from a .pallette file. Imported palettes are saved into
`~/.GC-2D/palettes

***Note:*** No color pallet can be set in case no data has been imported

#### Creating custom collor pallets
Custom Palettes can be defined in a plain text file ending with `.palette`, with each line 
containing the comma separated rgb values defining a color, each component can have a value from 0-255. 
The first line is the color for the lowest value, the last line is the color for the highest value.

For example, the common color palette jet can be defined like so:

#### jet.palette:
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


### Integration areas
Integration areas allow the user to calculate the volume under the 3D graph in the area speciefied by the integration area's dimension. Whenever an integration area is created, the integration area and it's corresponding information, such as the sum of the integration, the mean of the integration and a label, is added to the integration list.

***Note:*** No integration areas can be set in case no data has been imported

#### Adding integration areas
The 'draw selection' option in the toolbar or in the edit menu (CTRL + D), allows the user to create a new integration area in the 2D view

#### Editing integration areas
New handles can be added to an integration area by left-clicking one edge of the integration area, this causes the creation of another handle in the middle of the edge. Handles can be freely moved around in the 2D view by drag and dropping the handles, this willl alter the shape of the integration area. Individual handles can also be deleted by right clicking a handle and selecting the 'remove handle' option in the context menu. Integration areas can also be moved as a whole by left-clicking the 2D view while the cursor is within an integration area.

**NOTE:** In case an integration area only consists of 3 handles, no individual handles can be deleted

#### Relabeling integration areas
The label of an integration area can be edited by double-clicking the label of the specific integration area, after which a new label can be entered.

#### Deleting integration areas
A specific integration area can be deleted by selecting the 'clear' option in the integration list in the row of the integration area to be deleted

#### Highlighting integration areas in the 3D view
The integration list allows the user to highlight existing integration areas in the 3D view. This is done by left clicking the label of the corresponding integration area, the label column of the integration area should now be colored blue and the integration area should be highlighted in the 3D view. The user can unhighlight a certain integration area by clicking the label column of the specific integration area. Multiple integration areas can be highlighted by left-clicking the label column of specific integrations in the integration list while holding the CTRL button, alternatively the user can select multiple integration areas by drag-selecting multiple integration areas in the integration list.




