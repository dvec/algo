A = 345
B = 162

def gcd(a, b):
    while (b):
        a %= b
        a, b = b, a
    return a


if __name__ == '__main__':
    print('НОД', A, 'и', B, ':', gcd(345, 162))
