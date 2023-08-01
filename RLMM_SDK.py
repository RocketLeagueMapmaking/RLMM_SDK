import subprocess
import os
import wmi

#exe_path = r'C:\UDK\RLMM\Binaries'
#print(exe_path)

#subprocess.call([os.path.join(exe_path, "UDKLift.exe"), "editor"])

class InstallerState:
    def __init__(self):
        self.startRL = False
        self.foundRL = False
        self.installUDK = False
        self.foundUDKInstaller = False
        self.foundUDK = False


print("Please launch Rocket League")
print("")

f = wmi.WMI()
foundRL = False
for process in f.Win32_Process():
    if "RocketLeague" in process.Name:
        filePathRL = process.ExecutablePath
        foundRL = True
        process.Terminate()

if not foundRL:
    print(":(")
else:
    input("Press Enter to continue...")
    print("")
    print(f"Got {filePathRL}\n Thanks!")

