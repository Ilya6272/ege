from itertools import product

cnt = 0
for i in product(sorted('ЩЭДСР'), repeat=4):
    i = ''.join(i)
    cnt += 1
    if i == 'ЩДЩД':
        print(cnt)
