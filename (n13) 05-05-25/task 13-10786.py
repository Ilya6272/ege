from ipaddress import ip_address, ip_network

ip1 = ip_address('151.172.115.121')
ip2 = ip_address('151.172.115.156')

for mask in range(1, 31):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1 != net2 and ip1 in net1.hosts() and ip2 in net2.hosts():
        print(mask)
