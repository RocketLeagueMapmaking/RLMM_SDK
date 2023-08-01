; example1.nsi
;
; This script is perhaps one of the simplest NSIs you can make. All of the
; optional settings are left to their default settings. The installer simply 
; prompts the user asking them where to install, and drops a copy of example1.nsi
; there. 
;
; example2.nsi expands on this by adding a uninstaller and start menu shortcuts.

;--------------------------------

; The name of the installer
Name "RLMM SDK Installer"

; The file to write
OutFile "RLMM_SDK_Installer.exe"

; Request application privileges for Windows Vista
RequestExecutionLevel user

; Build Unicode installer
Unicode True

; The default installation directory
InstallDir $DESKTOP\RLMM_SDK

;--------------------------------

; Pages

Page directory
Page instfiles

;--------------------------------

; These are the programs that are needed by ACME Suite.
Section -Prerequisites
  SetOutPath $INSTDIR
  MessageBox MB_YESNO "Install UDK?" /SD IDYES IDNO endUDKInstall
    File "UDKInstall-2015-02.exe"
    ExecWait "UDKInstall-2015-02.exe"
    Goto endUDKInstall
  endUDKInstall:
SectionEnd
