ans = []
for i in range(10_000, 100_000):
    s1 = (int(max(str(i))) + int(min(str(i)))) ** 2
    s2 = 1
    for j in str(i):
        if int(j) % 2 == 0:
            s2 *= int(j)
    s = str(max(s1, s2)) + str(min(s1, s2))
    if s == '12116':
            ans.append(i)

print(min(ans))

