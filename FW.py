from netmiko import ConnectHandler
import getpass
import os

username = input('Username: ')
password = getpass.getpass()

# changes working directory
os.chdir('C:\SwitchBackups')

# Opens the list of Firewalls
with open('FW_ips.txt') as file:
    devices_list_firewall = file.read().splitlines()


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

    hostname = net_connect = ConnectHandler(**panos)
    hostname = net_connect.send_command('show config running | match hostname')
    hostname.split(" ")
    hostname,device = hostname.split(" ")
    print ("Backing up " + device)

    showrun = net_connect.send_command('show run')
    log_file = open(filename, "a")   # in append mode
    log_file.write(showrun)

# Finally close the connection
net_connect.disconnect()
