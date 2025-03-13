from itertools import product

cnt = 0
for i in product('АЛГОРИТМ', repeat=6):
    i = ''.join(i)
    if i.count('Л') <= 1 and i[0] != 'Р' and i[-1] in 'АОИ':
        cnt += 1

print(cnt)
