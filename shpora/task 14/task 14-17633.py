def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(1, 2031):
    num = 6**260 + 6**160 + 6**60 - x
    num_6 = convert(num, 6)
    if num_6.count('0') == 202:
        print(x)
