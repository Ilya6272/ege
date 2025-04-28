from ipaddress import ip_network, ip_address

for A in range(256):
    net = ip_network(f'248.112.{A}.35/255.255.255.240', False)
    cnt = 0
    if ip_address(f'248.112.{A}.35') in net.hosts():
        for i in net:
            i = f'{int(i):032b}'
            if i[:16].count('0') <= i[16:].count('0'):
                cnt += 1
        if cnt == net.num_addresses:
            print(A)