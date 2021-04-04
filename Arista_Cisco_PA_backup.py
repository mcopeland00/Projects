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
    hostname = net_connect = ConnectHandler(**iosv_l2)
    hostname = net_connect.send_command('show run | i hostname')
    hostname.split(" ")
    hostname,device = hostname.split(" ")
    print ("Backing up " + device)
    
    filename = device +'.txt'
    # filename = device + '.txt' 
 
    showrun = net_connect.send_command('show run')
    showvlan = net_connect.send_command('show vlan')
    showver = net_connect.send_command('show ver')
    log_file = open(filename, "a")   # in append mode
    log_file.write(showrun)
    log_file.write("\n")
    log_file.write(showvlan)
    log_file.write("\n")
    log_file.write(showver)
    log_file.write("\n")
 
# Finally close the connection
net_connect.disconnect()

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
    print("Backup for %s done" % devices)