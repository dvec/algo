def to_gray_code(n):
    return n ^ (n >> 1)


def from_gray_code(g):
    n = 0
    while g:
        n ^= g
        g >>= 1
    return n

if __name__ == '__main__':
    print('Число 132 в коде Грея:', bin(to_gray_code(132))[2:])
    print('Число, восстановленное из кода {}:'.format(bin(to_gray_code(132))[2:]), from_gray_code(to_gray_code(132)))
