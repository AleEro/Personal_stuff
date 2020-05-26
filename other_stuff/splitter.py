def assert_equals(a, b):
    if a == b:
        print('correct')
    else:
        print(f'Incorrect {a, type(a)} expected {b, type(b)}')


def square_digits(num):
    a = list(str(num))
    for x in range(len(a)):
        a[x] = int(a[x])*int(a[x])
    return int(''.join([str(i) for i in a]))


assert_equals(square_digits(9119), 811181)
