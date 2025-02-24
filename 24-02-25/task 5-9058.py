ans = []
for N in range(1, 10_000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '1' + R + str(R.count('1') % 2)
    else:
        R = R + '0' + str(R.count('1') % 2)
    R = int(R, 2)
    if R > 100:
        ans.append([R, N])

print(min(ans))
