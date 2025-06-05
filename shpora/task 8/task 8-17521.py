from itertools import product

alph = '01234567'

cnt = 0
for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] in '246' and i[-1] not in '26' and i.count('7') <= 2:
        cnt += 1

print(cnt)