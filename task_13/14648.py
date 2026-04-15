from ipaddress import*

ip_host = ip_address('218.48.192.56')
ip_net = ip_address('218.48.192.0')

cnt = 0
for mask in range(16, 25):
    net = ip_network(f'{ip_net}/{mask}',False)
    if net.num_addresses - 2 >= 500:
        if ip_host in net.hosts() and ip_net == net.network_address:
         cnt += 1
print(cnt)
