from ipaddress import ip_network, ip_address

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('0') <= ip[16:].count('0')


for A in range(0, 256)[::-1]:
    ip_1 = ip_address(f'223.167.{A}.167')
    net = ip_network(f'{ip_1}/255.255.255.192', False)
    if all(f(ip) for ip in net) and ip_1 in net.hosts():
        print(A)
        break
