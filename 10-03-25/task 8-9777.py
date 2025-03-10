from itertools import product

alph = sorted('КОМПЬЮТЕР')

cnt = 0
for i in product(alph, repeat=5):
    cnt += 1
    i = ''.join(i)
    if cnt % 2 != 0 and i[0] != 'Ь' and i.count('К') == 2:
        print(cnt, i)