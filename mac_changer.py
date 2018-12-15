#!/usr/bin/env python


import subprocess
#module allows you to run system commands
import optparse
import re

def argument():
    # handing command - line arguments
    paser = optparse.OptionParser()
    paser.add_option("-i", "--interface", dest="interface", help="interface for device ")
    paser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    (options, arguments) = paser.parse_args()
    #handing error
    if not options.interface:
        paser.error("[*] enter an interface, use --help for more information. ")
    elif not options.new_mac:
        paser.error("[*]enter new mac address for interfacw, use --help for more information.")
    return options
def change_mac(interface,new_mac):
    print("[!] changing Mac address to " + interface + " to [=] " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    # putting wlan0 connection down

    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    # changeing wlan0 mac address

    subprocess.call(["ifconfig", interface, "up"])
    # bring the new mac address up

def get_current_mac(interface):
    ifconfig_results = subprocess.check_output(["ifconfig", interface])
    # search and print the new mac address
    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)
    # handing errors
    if mac_address_search:
        return mac_address_search.group(0)

    else:
        print("[-] couldn't find any Mac Address")




options = argument()
#printing your current mac address
current_mac = get_current_mac(options.interface)
print("current = " + str(current_mac))


 #device interface
 #new Mac address
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("Mac Address was successfully changed. " + current_mac)
else:
    print("Mac Address was not successful")