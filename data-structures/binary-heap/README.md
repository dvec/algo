# Бинарная куча
### Что это?
Это структура данных, представляющая собой полное бинарное дерево, для которого выполняется основное свойство кучи: приоритет каждой вершины должен быть выше приоритетов каждого из потомков. В большинстве случаев приоритетом является значением. Такая структура называется **max-heap**. Ее пример изображен на рисунке:
![Бинарная куча](https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D1%83%D1%8E%D1%89%D0%B5%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE.svg/300px-%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D1%83%D1%8E%D1%89%D0%B5%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE.svg.png)
### Где используется?
 - В [heap sort](https://ru.wikipedia.org/wiki/%D0%9F%D0%B8%D1%80%D0%B0%D0%BC%D0%B8%D0%B4%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0)
 - Для ускорения [алгоритма дейкстры](https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%94%D0%B5%D0%B9%D0%BA%D1%81%D1%82%D1%80%D1%8B)
## Реализация
### Структура данных
Удобная структура данных для хранения бинарной кучи - обычный массив.
Тогда куча, изображенная на картинке выше, превратится в такой массив:
![Структура данных для хранения бинарнйо кучи](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D1%83%D1%8E%D1%89%D0%B5%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE_%D1%80%D0%B0%D0%B7%D0%B2%D0%B5%D1%80%D0%BD%D1%83%D1%82%D0%BE%D0%B5_%D0%B2_%D0%BC%D0%B0%D1%81%D1%81%D0%B8%D0%B2.svg/400px-%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D1%83%D1%8E%D1%89%D0%B5%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE_%D1%80%D0%B0%D0%B7%D0%B2%D0%B5%D1%80%D0%BD%D1%83%D1%82%D0%BE%D0%B5_%D0%B2_%D0%BC%D0%B0%D1%81%D1%81%D0%B8%D0%B2.svg.png)
### Базовые процедуры
##### Восстановление свойств кучи
**Асимптотика: O(log n)**
###### Входные данные:
 - h - массив, представлюящий бинарную кучу
 - i - индекс в массиве h представляющий значение, которое нужно изменить
```python
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
```
##### Построение кучи
**Асимптотика: O(n)**
###### Входные данные:
 - a - массив
###### Выходные данные:
 - h - массив, представлюящий бинарную кучу
```python
def build_heap(a):
    h = a[::]
    for i in range(len(a) // 2, 0, -1):
        heapify(h, i)
    return h

```
##### Увеличение элемента
**Асимптотика: O(log n)**
###### Входные данные:
 - h - массив, представлюящий бинарную кучу
 - i - индекс значения, представляющего вершину, значение которой надо увеличить
 - v - значение, на которое нужно увеличить вершину кучи
```python
def increase_item_in_heap(h, i, v):
    h[i-1] += v
    while i-1 > 1 and h[(i-1) // 2] < h[i-1]:
        h[i-1], h[(i-1) // 2] = h[(i-1) // 2], h[i-1]
        i //= 2
```
##### Удаление корневого элемента
**Асимптотика: O(log n)**
###### Входные данные:
 - h - массив, представлюящий бинарную кучу
```python
def del_root_item_in_heap(h):
    if not h:
        raise RuntimeError('Куча пуста!')
    root = h[0]
    h[0] = h[-1]
    del h[-1]
    heapify(h, 1)
    return root
```
