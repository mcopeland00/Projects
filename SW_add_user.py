from netmiko import ConnectHandler
import getpass
import os

username = input('Username: ')
password = getpass.getpass()

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
# Add account with priv 15
    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_config_set('username USERNAME privilege 15 secret 0 PASSWORD')
    output += net_connect.save_config()
    print(output)
    print()
