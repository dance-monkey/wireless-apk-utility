import tkinter.filedialog as fd
import urllib.request
import os
import zipfile
import shutil
import subprocess
import tkinter.simpledialog as sd
import tkinter.messagebox as mb
import tkinter.filedialog as fd

__ADK__ = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"


def downloadADK():

    if os.path.isdir("ADK"):
        print("ADK exists")
        os.chdir("ADK")
        return
    else:
        print("ADK does not exist")
        pass

    print("Downloading ADK")
    urllib.request.urlretrieve(__ADK__, "platform-tools-latest-windows.zip")
    print("Downloaded ADK")

    print("Extracting ADK")
    with zipfile.ZipFile("platform-tools-latest-windows.zip", "r") as zip_ref:
        zip_ref.extractall()
    print("Extracted ADK")

    print("Moving ADK")
    shutil.move("platform-tools", "ADK")
    print("Moved ADK")

    print("Deleting ADK Zip")
    os.remove("platform-tools-latest-windows.zip")
    print("Deleted ADK Zip")

    os.chdir("ADK")

    print("Done")


def setupGuide():

    print("Starting Setup Guide")

    view = mb.askyesno("Setup Guide", "Would you like to see the setup guide?")

    if view == True:
        pass
    else:
        return

    mb.showinfo("Continue in device", "Please continue in your device")

    mb.showinfo(
        "Continue in device",
        "Please connect the device to the same network as your computer",
    )

    mb.showinfo(
        "Continue in device",
        "Navigate to settings > Version manager and rapidly tap on “reset to factory setting” until it takes you to the engineering menu.",
    )

    mb.showinfo("Continue in device", "Enable “Wireless adb debug switch”")

    mb.showinfo(
        "Continue in device",
        "In the engineering menu, enable “Debug mode when USB is connected”",
    )


def chooseAPK():
    print("Choosing APK")
    apkDirectory = fd.askopenfile(
        "Select one APK to install", "APK Files (*.apk)|*.apk"
    )

    return apkDirectory


def deviceConnect():
    print("Connecting to device")
    subprocess.call("dir", shell=True)
    subprocess.call(
        "adb.exe connect "
        + sd.askstring("Device IP", "Please enter your device's IP address"),
        shell=True,
    )
    print("Connected to device")


def deviceInstall():
    print("Installing APK")
    subprocess.call("adb.exe install " + chooseAPK(), shell=True)
    print("Installed APK")

    print("Done")


def gracefulExit():
    print("Exiting")
    mb.showwarning(
        "WARNING",
        "Program End. In the engineering menu, disable Debug mode when USB is connected and Wireless adb debug switch",
    )
    print("Exited")
    exit(0)


def main():
    print("Starting")

    downloadADK()

    setupGuide()

    try:
        deviceConnect()
    except:
        mb.showerror("Error", "Could not connect to device")
        gracefulExit()

    try:
        deviceInstall()
    except:
        mb.showerror("Error", "Could not install APK")
        gracefulExit()

    while mb.askyesno("Done", "Would you like to install another APK?") == True:
        deviceInstall()

    gracefulExit()


if __name__ == "__main__":
    main()
