from ipaddress import ip_network

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('0') <= ip[16:].count('0')
for A in range(256)[::-1]:
    net = ip_network(f'217.109.{A}.94/255.255.254.0', False)
    if all(f(ip) for ip in net):
        print(A)
        break