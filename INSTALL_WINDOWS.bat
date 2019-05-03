@echo off

echo checking if python3 is installed...
py -3 --version >NUL
if errorlevel 1 goto npython

echo checking if pip3 is installed...
pip3 -v >NUL
if errorlevel 1 goto npip

echo installing GC-2D...
pip3 install .
pause
goto:eof

:npython
echo Error^: please install python3.
pause
goto:eof

:npip
echo Error^: please install pip3.
pause
goto:eof


