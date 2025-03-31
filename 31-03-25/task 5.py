def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10_000):
    R = convert(N, 4)
    summ = sum(map(int, R))
    if summ % 2 == 0:
        R += R[-2:]
    else:
        R = '2' + R + '0'
    R = int(R, 4)
    if R > 120:
        ans.append(R)

print(min(ans))



