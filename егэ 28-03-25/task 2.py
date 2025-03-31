print('w, x, y, z')
for w in range(2):
    for x in range(0, 1):
        for y in range(0, 1):
            for z in range(0, 1):
                f = x or (z <= y == w)
                if not f:
                    print(w, x, y, z)