set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "2D-GC.lnk"
set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "%PROGRAMFILES%\2D-GC\2D-GC.exe"
oLink.WorkingDirectory ="%PROGRAMFILES%\2D-GC"
oLink.Description = "2D_GC"
oLink.IconLocation = "%PROGRAMFILES%\2D-GC\2D-GC.exe"
oLink.Save
