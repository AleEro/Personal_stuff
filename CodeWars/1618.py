def add(a, b):
    a = rev(','.join(str(a)).split(','))
    b = rev(','.join(str(b)).split(','))
    if len(a) > len(b):
        z = it(a, b)
    else:
        z = it(b, a)
    return int(z)


def rev(v):
    z = []
    for i in range(len(v), 0, -1):
        z.append(int(v[i]))
    return z


def it(c, d):
    z = []
    for i in range(len(c)):
        if i >= len(d):
            z.append(int(c[i]))
        else:
            z.append(int(d[i]) + int(c[i]))
    d = ''
    for i in z:
       d += str(i)
    return d
print(add(122, 81) == 1103)
