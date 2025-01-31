# MAC Address Changer
This program is a simple shell script that can change your MAC address. It can take any network interface and you pick your new MAC address. Your MAC address won't change if the address you provide is invalid

## Installation

If you want to use the .sh file do the following:

1. Clone the repository onto your machine

2. If on windows, use a vm or the vagrant file to get into Linux (the only commands you need with vagrant is "vagrant up", "vagrant ssh", and "cd /vagrant" in that order)

3. Run the command with "chmod -x changer.sh" then run the command "./changer.sh (interface) (new MAC address)"

If you want to use the .py file do the following:

1. Clone the repository onto your machine

2. If on windows, use a vm or the vagrant file to get into Linux (the only commands you need with vagrant is "vagrant up", "vagrant ssh", and "cd /vagrant" in that order)

3. Run the command with "sudo python3 changer.py (interface) (new MAC address)" (Make sure you use sudo as you need root permissions to change your MAC address)

## Troubleshooting
If the program returns this error: "-bash: ./changer.sh: cannot execute: required file not found" then do the following on ubuntu or debian: 
1. sudo apt-get update
2. sudo apt-get install dos2unix
3. dos2unix changer.sh

You can also try the following if you're on vs code:
1. find "CRLF" in the bottom right corner next to "Markdown"
2. Click it and change it to LF

This has been the only error I have encountered so far.
