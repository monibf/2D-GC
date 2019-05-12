Set args = WScript.Arguments
 
'// you can get url via parameter like line below
'//Url = args.Item(0)
Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")
Dim fullpath
fullpath = fso.GetAbsolutePathName(".")
Set fso = Nothing

Url = args.Item(0)

dim xHttp: Set xHttp = createobject("Microsoft.XMLHTTP")
dim bStrm: Set bStrm = createobject("Adodb.Stream")
xHttp.Open "GET", Url, False
xHttp.Send
 
with bStrm
    .type = 1 '//binary
    .open
    .write xHttp.responseBody
    .savetofile fullpath & "\python-installer.exe", 2 '//overwrite
end with