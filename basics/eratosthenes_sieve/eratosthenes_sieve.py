def eratosthenes_sieve(n):
    a = []
    r = []
    for i in range(2, n):
        if i not in a:
            r.append(i)
            for j in range(i * i, n + 1, i):
                a.append(j)
    return r


if __name__ == '__main__':
    print('Первые 100 простых чисел:', *eratosthenes_sieve(100))
