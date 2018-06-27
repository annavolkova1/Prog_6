def fibonacci1(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    print(f)


fibonacci1(10)


def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


for n in fibonacci(100):
    print(n)

