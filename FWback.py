from netmiko import ConnectHandler
import getpass
import os

username = input('Username: ')
password = getpass.getpass()

# changes working directory
os.chdir('C:\SwitchBackups')

# Opens the list of Firewalls
with open('FW_ips.txt') as file:
    devices_list = file.read().splitlines()


#connecting to Firewall
for devices in devices_list:
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