from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase
cnt = 0
for i in product(alph[:25], repeat=4):
    i = ''.join(i)
    if i[0] != '0':
        count_nech = 0
        for j in alph[1::2]:
            count_nech += i.count(j)

        count_5 = 0
        for j in alph[:6]:
            count_5 += i.count(j)

        if count_nech == 1 and count_5 <=2:
            cnt += 1

print(cnt)
