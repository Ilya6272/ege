from itertools import product

cnt = 0
for i in product('01234', repeat=6):
    i = ''.join(i)
    if i[-1] not in '34' and i[0] not in '01':
        cnt += 1
print(cnt)
