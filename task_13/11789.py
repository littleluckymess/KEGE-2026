from ipaddress import ip_network

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('1') <= ip[16:].count('1')

for mask in range(16,25):
    net = ip_network(f'99.8.254.232/{mask}', False)
    if all(f(ip) for ip in net):
        print(net.netmask)
        break