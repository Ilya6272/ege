def f(x, y, s):
    if x + y > 46: return s % 2 == 0
    if s == 0: return False
    h = [f(max(x, y) + 1, min(x, y), s - 1),
         f(max(x, y) + 2, min(x, y), s - 1),
         f(max(x, y) + 3, min(x, y), s - 1),]
    if x != y:
        h.append(f(max(x, y), min(x, y) * 2, s - 1))
    return any(h) if (s - 1) % 2 == 0 else all(h)

ans = []
for s1 in range(1, 100):
    for s2 in range(1, 100):
        if f(s1, s2, 1):
            ans.append(s1 + s2)

print(min(ans))
print('20)',[s for s in range(1, 42) if f(5, s, 3) and not f(5, s, 1)])
print('20)',[s for s in range(1, 25) if f(22, s, 4) and not f(22, s, 2)])




