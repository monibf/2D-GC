set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = WScript.Arguments(1) & ".lnk"
set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath =  WScript.Arguments(0) & "\" &  WScript.Arguments(1) & "\" &  WScript.Arguments(1) & ".exe"
oLink.WorkingDirectory ="%USERPROFILE%"
oLink.Description = WScript.Arguments(1)
oLink.IconLocation = WScript.Arguments(0) & "\" &  WScript.Arguments(1) & "\" &  WScript.Arguments(1) & ".exe"
oLink.Save
