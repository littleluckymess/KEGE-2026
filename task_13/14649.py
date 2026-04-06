from ipaddress import ip_network

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('1') >= ip[16:].count('1')

for A in range(256)[::-1]:
    net = ip_network(f'116.242.{A}.26/255.255.255.224', False)
    if all(f(ip) for ip in net):
        print(A)
        break