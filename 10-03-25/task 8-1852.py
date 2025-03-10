from itertools import product

cnt = 0
for i in product('ГЕПАРД', repeat=5):
    i = ''.join(i)
    if i.count('Г') == 1 and i[0] != 'А' and i[4] != 'Е':
        cnt += 1
print(cnt)



