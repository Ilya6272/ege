def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

num = 2*729**1021 - 2*243**1022 + 81**1023 - 2*27**1024 - 1025
ans = convert(num,3)
print(ans.count('0'))

