from ipaddress import ip_address, ip_network

for A in range(256):
    net = ip_network(f'217.109.{A}.94/255.255.254.0', False)
    cnt = 0
    if ip_address(f'217.109.{A}.94') in net.hosts():
        for i in net:
            i = f'{int(i):032b}'
            if i[:16].count('0') <= i[16:].count('0'):
                cnt += 1
        if cnt == net.num_addresses:
            print(A)
