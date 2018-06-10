A = [1, 2, 4, 5, 6, 8, 9, 10, 11, 16]


def heapify(h, i):
    left = 2 * i
    right = 2 * i + 1
    largest = i

    if left <= len(h) and h[left-1] > h[largest-1]:
        largest = left
    if right <= len(h) and h[right-1] > h[largest-1]:
        largest = right
    if largest != i:
        h[i-1], h[largest-1] = h[largest-1], h[i-1]
        heapify(h, largest)


def build_heap(a):
    h = a[::]
    for i in range(len(a) // 2, 0, -1):
        heapify(h, i)
    return h


def increase_item_in_heap(h, i, v):
    h[i] += v
    while i > 1 and h[i // 2] < h[i]:
        h[i-1], h[(i-1) // 2] = h[(i-1) // 2], h[i-1]
        i //= 2


def del_root_item_in_heap(h):
    if not h:
        raise RuntimeError('Куча пуста!')
    root = h[0]
    h[0] = h[-1]
    del h[-1]
    heapify(h, 1)
    return root


if __name__ == '__main__':
    print('Изначальный массив:', A)
    H = build_heap(A)
    print('Двоичная куча:', H)
    print('Увеличиваю наименьшее значение в куче на 10...')
    increase_item_in_heap(H, len(H) - 1, 10)
    print('Новая двоичная куча:', H)
    print('Удаляю корень...')
    del_root_item_in_heap(H)
    print('Финальная двоичная куча:', H)
