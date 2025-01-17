#!/bin/bash

# takes the first input which should be the network interface and puts it into the interface variable
interface=$1

# displays the current MAC address of the network interface
read MAC </sys/class/net/$interface/address 
echo "old: $interface $MAC"

# takes the second input and puts it into the mac variable and will check if the mac address given is valid or not
mac=$2
[[ "$mac" =~ ^([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}$ ]] && echo "valid MAC address" || echo "invalid MAC Address"

# 
sudo ip link set dev $interface address $mac

# displays the new MAC address of the network interface
read MAC </sys/class/net/$interface/address
echo "new: $interface $MAC"