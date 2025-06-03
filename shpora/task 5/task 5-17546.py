ans = []
for N in range(1, 10_000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '10' + R
    if N % 2 != 0:
        R = '1' + R + '01'
    R = int(R, 2)
    if N <= 12:
        ans.append(R)
print(max(ans))



