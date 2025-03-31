from itertools import product

alph = sorted(set('ЛУНАТИК'))

cnt = 0
for i in product(alph, repeat=6):
    i = ''.join(i)
    cnt += 1
    if i[0] == 'Н' and i.count('У') + i.count('А') + i.count('И') == 1:
        print(cnt, i)