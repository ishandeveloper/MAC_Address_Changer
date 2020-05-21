#!usr/bin/env python3

import subprocess
import optparse


def mac_changer(interface, new_mac):
    print("[+] Changing MAC Address For " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print('[✓] MAC ADDRESS SUCCESSFULLY CHANGED TO ' + new_mac + ' FOR ' + interface)


parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface whose MAC Address you want to change")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
(options, arguments) = parser.parse_args()

mac_changer(options.interface, options.new_mac)

