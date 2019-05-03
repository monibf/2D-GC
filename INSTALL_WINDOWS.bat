@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------    

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
pyinstaller --name=2D-GC --noconsole --distpath="%PROGRAMFILES%" gc2d\__main__.py

mkdir "%PROGRAMFILES%\2D-GC\gc2d"
mkdir "%PROGRAMFILES%\2D-GC\exampledata"
copy exampledata "%PROGRAMFILES%\2D-GC\exampledata\"
copy UNINSTALL_WINDOWS.bat "%PROGRAMFILES%\2D-GC\UNINSTALL.bat"
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


