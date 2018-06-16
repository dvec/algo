import sys
sys.setrecursionlimit(1000)  # Может упасть из-за переполнения стека


def binpow(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return binpow(a, n - 1) * a
    else:
        return binpow(a, n / 2) ** 2


if __name__ == '__main__':
    print('54 ^ 54 =', binpow(54, 54))
