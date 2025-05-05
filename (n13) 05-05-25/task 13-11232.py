from ipaddress import ip_address, ip_network

net = ip_network('192.168.31.80/255.255.255.240')

max_sum_1 = 0
for i in net:
    i = f'{int(i):032b}'
    max_sum_1 = max(max_sum_1, i.count('1'))
print(max_sum_1)