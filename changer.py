import subprocess
import optparse
import re
import sys

interface = sys.argv[1]

old = subprocess.run(['cat', f'/sys/class/net/{interface}/address'], capture_output=True, text=True)
print(f"old: {old.stdout}")

new = sys.argv[2]
if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", new.lower()):
    print("Valid MAC address. Changing...")
    subprocess.run(['ip', 'link', 'set', 'dev', interface, 'address', new])
    new = subprocess.run(['cat', f'/sys/class/net/{interface}/address'], capture_output=True, text=True)
    print(f"new: {new.stdout}")
else:
    print("Invalid MAC address")