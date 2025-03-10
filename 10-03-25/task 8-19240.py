from itertools import product

alph = sorted('ЯНВАРЬ')
cnt = 0
for i in product(alph,repeat=5):
    cnt += 1
    i = ''.join(i)
    if i[0] != 'Я' and i.count('Ь') <= 1 and 'ЯЯ' not in i:
        print(cnt, i)

