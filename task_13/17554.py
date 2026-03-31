from ipaddress import ip_network

net = ip_network('112.160.0.0/12')

cnt = 0
for ip in net:
    ip= f'{int(ip):032b}'
    if ip.count('1') % 3 != 0:
        cnt += 1
print(cnt)