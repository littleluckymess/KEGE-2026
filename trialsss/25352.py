from ipaddress import ip_network

net = ip_network('190.202.83.62/255.255.252.0', False)
print(max(net.hosts()))