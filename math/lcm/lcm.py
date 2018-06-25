from math import gcd  # Можно использовать функцию из math/gcd/gcd.py


A = 345
B = 162


def lcm(a, b):
    return (a * b) / gcd(a, b)


if __name__ == '__main__':
    print('НОК', A, 'и', B, ':', lcm(A, B))
