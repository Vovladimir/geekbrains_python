from itertools import cycle, count

c = 8
gen_cycle = cycle(['i', 'am', 'Groot'])
gen_count = count(3)
while c:
    print(f'{next(gen_count)} - {next(gen_cycle)}')
    c -= 1
