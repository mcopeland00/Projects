from netmiko import ConnectHandler
import getpass
import os

username = input('Username: ')
password = getpass.getpass()

# changes working directory
os.chdir('C:\SwitchBackups')

# Opens the list of switches
with open('Switch_ips.txt') as file:
    devices_list = file.read().splitlines()


#connecting to Switchs
for devices in devices_list:
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