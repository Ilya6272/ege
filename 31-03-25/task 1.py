from itertools import permutations

graph = 'BF FD DC CH HG GE EB BA GA DA CA'.split()
matrix = '36 478 178 258 46 158 23 2346'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)