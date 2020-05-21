#!usr/bin/env python3

import subprocess

interface = input("INTERFACE > ")
new_mac = input(" NEW MAC ADDRESS > ")

print("[+] Changing MAC Address For "+interface+" to "+new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

