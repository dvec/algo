# Декартово дерево
### Что это?
Декартово дерево - это структура данных, объединяющая в себе бинарное дерево поиска и бинарную кучу (отсюда и второе её название: treap (tree + heap) и дерамида (дерево + пирамида)).
## Реализация
### Структура данных
Будем хранить пары (`x`, `y`) таким образом, чтобы образовывалось бинарное дерево поиска по `x` и бинарная пирамида по `y`:
```python3
class _TreapNode:
    def __init__(self, key, value, heap_id,
                 parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.heap_id = heap_id
        self.parent = parent
        self.left = left
        self.right = right
```
### Базовые процедуры
Я не буду приводить здесь код так как его слишком много. Его можно посмотреть в treap.py
##### Добавление элемента в дерево
**Асимптотика: O(log n) в среднем**
###### Входные данные:
 - x - `x` из пункта "структура данных"
 - y - `y` из пункта "структура данных"
##### Удаление элемента из дерева
**Асимптотика: O(log n) в среднем**
###### Входные данные:
 - x - `x` из пункта "структура данных"
##### Поиск элемента в дереве
**Асимптотика: O(log n) в среднем**
###### Входные данные:
 - x - `x` из пункта "структура данных"
###### Выходные данные:
 - y - `y` из пункта "структура данных"
