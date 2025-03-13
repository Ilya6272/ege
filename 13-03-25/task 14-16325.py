from string import digits, ascii_uppercase

def convert(num, sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

num = 2*729**2014 + 2*243**2016 - 2*81**2018 + 2*27**2020 - 2*9**2022 - 2024
ans = convert(num,27)
cnt = 0
for i in ans:
    if i >= 'A':
        cnt += 1

print(cnt)

