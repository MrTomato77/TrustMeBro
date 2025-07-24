import subprocess
import sys
import os
import ctypes
import pystray
import atexit
import keyboard
import threading

from pystray import MenuItem as item
from PIL import Image
from pathlib import Path

rule_name = "TrustMeBro"
remote_ip = "0.0.0.0"
is_blocked = False
icon = None

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(Path(__file__).parent, relative_path)

icon_on = Image.open(resource_path("icon/power-on.ico"))
icon_off = Image.open(resource_path("icon/power-off.ico"))

def block_ip():
    if remote_ip and remote_ip != "0.0.0.0" and remote_ip != "x.x.x.x":
        subprocess.run([
            "netsh", "advfirewall", "firewall", "add", "rule",
            f"name={rule_name}", "dir=out", "action=block", f"remoteip={remote_ip}"
        ], shell=True)
    else:
        print("Invalid or placeholder IP. Skipping firewall rule creation.")

def unblock_ip():
    subprocess.run([
        "netsh", "advfirewall", "firewall", "delete", "rule",
        f"name={rule_name}"
    ], shell=True)

def toggle_block(icon_ref=None, item=None):
    global is_blocked, icon
    if not is_blocked:
        block_ip()
        icon.icon = icon_on
        icon.title = "Blocking [ON]"
        is_blocked = True
    else:
        unblock_ip()
        icon.icon = icon_off
        icon.title = "Blocking [OFF]"
        is_blocked = False

def quit_app(icon, item):
    unblock_ip()
    icon.stop()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def keyboard_listener():
    keyboard.add_hotkey('ctrl+f12', toggle_block)
    keyboard.wait()

def main():
    global icon_off, icon
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        return

    atexit.register(unblock_ip)
    threading.Thread(target=keyboard_listener, daemon=True).start()

    menu = (item('Toggle Block', toggle_block), item('Exit', quit_app))
    icon = pystray.Icon("TrustMeBro", icon_off, "Blocking [OFF]", menu)
    icon.run()

if __name__ == "__main__":
    main()