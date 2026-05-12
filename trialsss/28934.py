from ipaddress import ip_network
net = ip_network('191.89.109.206/255.255.224.0',False)
print(max(net.hosts()))
print(191+89+127+254)