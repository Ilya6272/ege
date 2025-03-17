from itertools import product

cnt = 0
for i in product('ИГРОК',repeat=5):
    i =''.join(i)
    if i[0] != 'К' and 'РОК' not in i and i.count('И') == 1 and i.count('Г') == 1 and i.count('Р') == 1 and i.count('О') == 1 and i.count('К') == 1:
        cnt += 1

print(cnt)
