import subprocess
import optparse
import re
import sys

# Takes the argument for the interface from the command line
interface = sys.argv[1]

# Get the current MAC address and displays it
old = subprocess.run(['cat', f'/sys/class/net/{interface}/address'], capture_output=True, text=True)
print(f"old: {old.stdout}")

# Takes the argument for the new MAC address from the command line
new = sys.argv[2]

# Checks if the new MAC address is valid and changes it if it is
if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", new.lower()):
    print("Valid MAC address. Changing...")

    subprocess.run(['ip', 'link', 'set', 'dev', interface, 'address', new]) # Changes the MAC address

    new = subprocess.run(['cat', f'/sys/class/net/{interface}/address'], capture_output=True, text=True) # Gets the new MAC address
    print(f"new: {new.stdout}") # Displays the new MAC address

# If the new MAC address is invalid, it will display an error message
else:
    print("Invalid MAC address")