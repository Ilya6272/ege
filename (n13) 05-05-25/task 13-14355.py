from ipaddress import ip_address, ip_network

for mask in range(16, 25):
    net = ip_network(f'127.63.67.1/{mask}', False)
    cnt = 0
    if ip_address(f'127.63.67.1') in net.hosts():
        for i in net:
            i = f'{int(i):032b}'
            if i[:16].count('1') >= i[16:].count('1'):
                cnt += 1
    if cnt == net.num_addresses:
        print(net.netmask)
