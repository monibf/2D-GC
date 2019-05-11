@echo off
if not defined INSTALL_LOCATION set INSTALL_LOCATION=%LOCALAPPDATA%
set PYTHON_URL=https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe
set NAME=2D-GC
set VERSION=0.1
set PUBLISHER=RUG

::----------------
:begining
echo Checking if python3 is installed...
py -3 --version >NUL
if errorlevel 1 goto ipython

echo Checking if pip is installed...
py -3 -m pip -v >NUL
if errorlevel 1 goto ipip

echo Checking if pyinstaller is installed...
py -3 -m PyInstaller -v >NUL
if errorlevel 1 py -3 -m pip install git+https://github.com/pyinstaller/pyinstaller.git

echo Installing dependencies...
py -3 -m pip install -r requirements.txt

echo Installing %NAME%...
py -3 -m PyInstaller --noconfirm --name="%NAME%" --noconsole --distpath="%INSTALL_LOCATION%" gc2d\__main__.py

:: This is required until the program opens without the example data.
mkdir "%INSTALL_LOCATION%\%NAME%\gc2d"
mkdir "%INSTALL_LOCATION%\%NAME%\exampledata"
copy /Y exampledata "%INSTALL_LOCATION%\%NAME%\exampledata\" >NUL

:: create uninstall script in install directory
echo @echo off>"%INSTALL_LOCATION%\%NAME%\UNINSTALL.bat"
echo set INSTALL_LOCATION=%INSTALL_LOCATION%>>"%INSTALL_LOCATION%\%NAME%\UNINSTALL.bat"
echo set NAME=%NAME%>>"%INSTALL_LOCATION%\%NAME%\UNINSTALL.bat"
type WINDOWS_UNINSTALL.txt>>"%INSTALL_LOCATION%\%NAME%\UNINSTALL.bat"

:: add the uninstall script to the registry
echo registering uninstaller...
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%NAME%" /v DisplayName /t REG_SZ /d %NAME% /f >NUL
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%NAME%" /v DisplayVersion /t REG_SZ /d "%VERSION%" /f >NUL
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%NAME%" /v InstallLocation /t REG_SZ /d "%INSTALL_LOCATION%\%NAME%" /f >NUL
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%NAME%" /v NoModify /t REG_DWORD /d 1 /f >NUL
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%NAME%" /v Publisher /t REG_SZ /d "%PUBLISHER%" /f >NUL
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%NAME%" /v UninstallPath /t REG_SZ /d "%INSTALL_LOCATION%\%NAME%\UNINSTALL.bat" /f >NUL
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%NAME%" /v UninstallString /t REG_SZ /d "%INSTALL_LOCATION%\%NAME%\UNINSTALL.bat" /f >NUL

:: Create start menu and desktop shortcuts.
echo Creating shortcuts...
cscript WINDOWS_GENERATE_LINK.vbs "%INSTALL_LOCATION%" "%NAME%" >NUL
mkdir "%APPDATA%\Microsoft\Windows\Start Menu\Programs\%NAME%"
copy /Y "%NAME%.lnk" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\%NAME%" >NUL
copy /Y "%NAME%.lnk" "%USERPROFILE%\Desktop" >NUL

:: Offer to uninstall python if we installed it.
if defined INSTALLED_PYTHON goto upython

::----------------
:complete
echo Installation complete!
pause
exit
::---------------
:ipython
set /p yn=Download and install python ^(y/N^)^? 
if /I not "%yn%"=="y" goto npython
:: Download python if it hasn't been already...
echo downloading python...
if not exist python-installer.exe cscript WINDOWS_DOWNLOAD_PYTHON.vbs "%PYTHON_URL%" >NUL

:: Prompt user to install python3.
echo installing python3...
python-installer.exe PrependPath=1 SimpleInstall=1 SimpleInstallDescription="Install the complete python suite and add python to the PATH."
set INSTALLED_PYTHON=1
start "" "%0"
exit
::----------------
:upython
set /p yn=The installation is now complete and python3 is no longer required, would you like to uninstall it ^(y/N^)? 
if /I "%yn%"=="y" echo Uninstalling python3... & python-installer.exe /uninstall
goto :complete
::----------------
:npython
echo Error^: please install python3.
pause
exit
::----------------
:ipip
echo Your current install of python3 does not include pip. 
echo You can either install pip yourself, or this script can download and reinstall python%PYTHON_VERSION% for you.
:goto ipython
::----------------
