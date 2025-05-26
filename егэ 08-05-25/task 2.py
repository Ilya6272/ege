print('w, x, y, z')
for w in range(2):
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = y and (x or z) or (not(y or z)) or w
                if not f:
                    print(w, x, y, z)