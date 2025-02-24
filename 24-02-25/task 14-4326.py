from string import digits, ascii_uppercase
def convert(num, sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
         res += alph[num % sys]
         num //= sys
    return res[::-1]

num = 3 * 15 ** 1140 + 2 * 15 ** 1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74
num = convert(num,15)
print(num.count('E'))

alph = digits + ascii_uppercase
ans = 0
for i in alph[:15]:
    cnt = 1
    while i * cnt in num:
        cnt += 1
    ans = max(ans, cnt - 1)
print(ans)
