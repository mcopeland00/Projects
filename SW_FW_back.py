from netmiko import ConnectHandler
import getpass
import os

username = input('Username: ')
password = getpass.getpass()

# changes working directory
os.chdir('C:\SwitchBackups')

# Opens the list of switches
with open('Switch_ips.txt') as file:
    devices_list_switches = file.read().splitlines()

# Opens the list of Firewalls
with open('FW_ips.txt') as file:
    devices_list_firewall = file.read().splitlines()


#connecting to Switchs
for devices in devices_list_switches:
    print('Connecting to device: ' + devices)
    ip_address_of_device = devices
    iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': ip_address_of_device,
    'username': username,
    'password': password,
}

    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_command('show running-config')
    file = open("%s.txt" % devices, "w")
    file.write(output)
    file.close()
    print("BC for %s done" % devices)

#connecting to Firewall
for devices in devices_list_firewall:
    print('Connecting to device: ' + devices)
    ip_address_of_device = devices
    panos = {
    'device_type': 'paloalto_panos',
    'ip': ip_address_of_device,
    'username': username,
    'password': password,
}

    net_connect = ConnectHandler(**panos)
    output = net_connect.send_command('show config running')
    file = open("%s.txt" % devices, "w")
    file.write(output)
    file.close()
    print("BC for %s done" % devices)