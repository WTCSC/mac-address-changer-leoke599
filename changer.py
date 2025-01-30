import subprocess
import optparse
import re
import sys

interface = sys.argv[1]

def getmac(interface):
    ifconfig_result = subprocess.call(["read", "MAC", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")

def changemac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(['sudo', "ifconfig", interface, "down"])
    subprocess.call(['sudo', "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(['sudo', "ifconfig", interface, "up"])

current_mac = getmac(interface)
print("Current MAC = " + str(current_mac))

