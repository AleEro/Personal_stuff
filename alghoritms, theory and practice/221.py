from math import sqrt
f_list = [0, 1]


# N-value Fibonacchi
def fib(n):
    i = 0
    while True:
        i += 1
        f_list.append(int(f_list[-1]+f_list[-2]))
        if i >= n:
            break
    return f_list[n-1]


def fib_digit(n):
    return int(1/sqrt(5)*(((1+sqrt(5))/2)**n-((1-sqrt(5))/2)**n))


def main():
    n = int(input())
    print(fib(n))
    print(f_list)
    print(fib_digit(n))


if __name__ == "__main__":
    main()
