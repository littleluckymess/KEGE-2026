from ipaddress import ip_network

net = ip_network('214.187.224.0/255.255.224.0')

cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 6 != 0 and int(ip) % 10000 == 1000:
       cnt += 1
print(cnt)
