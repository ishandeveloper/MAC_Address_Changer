#!usr/bin/env python3

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface whose MAC Address you want to change")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        print('[!] Please Select An Interface Using -i \n\tFor Example : -i eth0')
        exit(-1)
    elif not options.new_mac:
        print('[!] Please Type New Mac Address Using -m \n\tFor Example : -m 00:11:22:33:44:55')
    else:
        mac_changer(options.interface, options.new_mac)
        ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
        mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
        print('[✓] MAC ADDRESS SUCCESSFULLY CHANGED TO ' + mac_address_search.group(0) + ' FOR ' + options.interface)


def mac_changer(interface, new_mac):
    print("[+] Changing MAC Address For " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


get_arguments()
