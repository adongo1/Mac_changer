#!/usr/bin/env python


import subprocess
#module allows you to run system commands
import optparse

def change_mac(interface,new_mac):
    print("[!] changing Mac address to " + interface + " to [=] " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    # putting wlan0 connection down

    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    # changeing wlan0 mac address

    subprocess.call(["ifconfig", interface, "up"])
    # bring the new mac address up


#handing command - line arguments
paser = optparse.OptionParser()
paser.add_option("-i", "--interface", dest="interface", help="interface for device ")
paser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
(options, arguments) = paser.parse_args()

 #device interface
 #new Mac address
change_mac(options.interface, options.new_mac)
