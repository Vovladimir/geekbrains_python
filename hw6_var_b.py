from itertools import cycle

c = 0
for el in cycle(['i', 'am', 'Groot']):
    print(el)
    c += 1
    if c > 10:
        break

# --------------------------- решение 2 ----------------------
c = 10
g = cycle([1, 2, 4, 8])
while c:
    print(next(g))
    c -= 1
