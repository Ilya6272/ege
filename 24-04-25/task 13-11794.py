from ipaddress import ip_network

for A in range(256):
    net = ip_network(f'223.167.{A}.167/255.255.255.192', False)
    cnt = 0
    for i in net:
        i = f'{int(i):032b}'
        if i[:16].count('0') <= i[16:].count('0'):
            cnt += 1
    if cnt == net.num_addresses:
        print(A)
