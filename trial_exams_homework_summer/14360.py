from ipaddress import ip_network, ip_address

ip = ip_address('153.202.16.37')

for mask in range(10,31):
    net = ip_network(f'153.202.16.37/{mask}', False)
    if net.network_address == ip_address('153.202.16.32') and ip_address('153.202.16.32') not in net.hosts() :
        print(net.netmask)
