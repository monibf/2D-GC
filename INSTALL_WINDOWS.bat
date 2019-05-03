@echo off

echo Checking if python3 is installed...
py -3 --version >NUL
if errorlevel 1 goto npython

echo Checking if pip3 is installed...
pip3 -v >NUL
if errorlevel 1 goto npip

echo Checking if pyinstaller is installed...
pyinstaller -v >NUL
if errorlevel 1 pip install git+https://github.com/pyinstaller/pyinstaller.git

echo Installing dependencies...
pip3 install -r requirements.txt

echo Installing GC-2D...
pyinstaller --name=2D-GC --noconsole --distpath="%LOCALAPPDATA%\Programs" gc2d\__main__.py

mkdir "%LOCALAPPDATA%\Programs\2D-GC\gc2d"
mkdir "%LOCALAPPDATA%\Programs\2D-GC\exampledata"
copy exampledata "%LOCALAPPDATA%\Programs\2D-GC\exampledata\"
copy UNINSTALL_WINDOWS.bat "%LOCALAPPDATA%\Programs\2D-GC\UNINSTALL.bat"

mkdir "%APPDATA%\Microsoft\Windows\Start Menu\Programs\2D-GC"
cscript GENERATE_LINK_WINDOWS.vbs
copy 2D-GC.lnk "%APPDATA%\Microsoft\Windows\Start Menu\Programs\2D-GC"
copy 2D-GC.lnk "%USERPROFILE%\Desktop"
echo Done!
pause
exit

:npython
echo Error^: please install python3.
pause
exit

:npip
echo Error^: please install pip3.
pause
exit


