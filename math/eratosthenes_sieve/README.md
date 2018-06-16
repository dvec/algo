# Решето эратосфена

### Что это?
Это алгоритм, позволяющий очень быстро рассчитывать простые числа. Это работает как-то так:

![демо](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/New_Animation_Sieve_of_Eratosthenes.gif/400px-New_Animation_Sieve_of_Eratosthenes.gif)

Где используется?
 - Учеными, которые рассчитывают простые числа

## Реализация
**Асимптотика: O(n log(log n))**
###### Входные данные:
 - n - ограничение
###### Выходные данные:
 - r - массив, содежащий все простые числа до n
```python3
def eratosthenes_sieve(n):
    a = []
    r = []
    for i in range(2, n):
        if i not in a:
            r.append(i)
            for j in range(i * i, n + 1, i):
                a.append(j)
    return r
```