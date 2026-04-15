from ipaddress import*

ip_1 = ip_address('157.127.182.76')
ip_2 = ip_address('157.127.190.80')

for mask in range(10, 31):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_2 not in net and ip_1 in net.hosts():
        print(mask)
        break