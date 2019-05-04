@echo off
if "%INSTALL_LOCATION%"=="" set INSTALL_LOCATION=%LOCALAPPDATA%
set NAME=2D-GC
set VERSION=0.1
set PUBLISHER=RUG
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

echo Installing %NAME%...
pyinstaller --noconfirm --name="%NAME%" --noconsole --distpath="%INSTALL_LOCATION%" gc2d\__main__.py

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

echo Done!
pause
exit

:npython
echo Error^: please install python3.
pause
exit
n

:npip
echo Error^: please install pip3.
pause
exit


