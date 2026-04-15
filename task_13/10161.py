from ipaddress import*

ip_1 = ip_address('211.115.61.154')
ip_2 = ip_address('211.115.59.137')

for mask in range(16, 25)[::-1]:
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_1 in net.hosts() and ip_2 in net.hosts():
        print(net.netmask)
        break