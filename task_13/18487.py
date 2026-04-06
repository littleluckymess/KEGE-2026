from ipaddress import ip_network

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('1') > 15

for A in range(256):
    net = ip_network(f'192.214.{A}.184/27', False)
    if all(f(ip) for ip in net):
        print(A)
        break