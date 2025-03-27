from itertools import product, permutations

def f(w, x, y, z):
    return (y <= x) or not z or w
cnt = 0
for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(1, 0, a1, a2), (1, 1, a3, a4), (a5, 1, 1, a6)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            u = [f(**(dict(zip(p, t)))) for t in table]
            if u == [1, 1, 1]:
                cnt += 1
                print(*p)