from itertools import product, permutations


def f(x, y, z):
    return not (x == (y <= z))


table = [(0, 0, 1), (0, 1, 1)]
for p in permutations('xyz'):
    u = [f(**dict(zip(p, t))) for t in table]
    if u == [1, 0]:
        print(*p)
