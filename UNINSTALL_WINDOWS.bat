@echo off
echo Uninstalling 2D-GC...
cd ..
rmdir /s /q "%LOCALAPPDATA%\Programs\2D-GC"
rmdir /s /q "%APPDATA%\Microsoft\Windows\Start Menu\Programs\2D-GC"

echo Done!
pause
exit


