Name "AutoDiag Pro Ultimate"

OutFile "AutoDiagPro_Setup.exe"

InstallDir "$PROGRAMFILES\AutoDiagPro"


Section

SetOutPath $INSTDIR

File "dist\AutoDiagPro.exe"


CreateShortcut "$DESKTOP\AutoDiag Pro.lnk" "$INSTDIR\AutoDiagPro.exe"


SectionEnd
