# inp = '4 8 0 3 4 2 0 3'.split(' ') * 10**5
inp = input().split(' ')

[[inp.remove(j) for j in inp if inp.count(j) < 2] for i in range(len(inp))]
[[inp.remove(j) for j in inp if inp.count(j) > 1] for i in range(len(inp))]
[print(i, end=' ') for i in inp]
