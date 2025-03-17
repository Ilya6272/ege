from itertools import product

alph = sorted(set('ПАВСИКАКИЙ'))
cnt = 0
for i in product(alph, repeat=6):
    i = ''.join(i)
    if 'АИ' in i or 'ИА' in i or 'ИИ' in i or 'АА' in i:
        cnt += 1
        if i == 'КАКААА':
            print(cnt)



