from random import Random


class _TreapNode:
    def __init__(self, key, value, heap_id,
                 parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.heap_id = heap_id
        self.parent = parent
        self.left = left
        self.right = right
    def __repr__(self):
        return str((self.key, self.value, self.heap_id))


class Treap:
    def __init__(self, seed=0, max_heap_id=1 << 64):
        self.random = Random(seed)
        self.max_heap_id = max_heap_id
        self.root = None

    def __setitem__(self, key, value):
        node, parent = self._find_node(key, self.root)
        if node is None:
            heap_id = self.random.randrange(self.max_heap_id)
            node = _TreapNode(key, value, heap_id)
            if parent is None:
                self.root = node
            elif node.key < parent.key:
                parent.left = node
            else:
                parent.right = node
            node.parent = parent
            self._prioritize(node)
        else:
            node.value = value

    def _find_node(self, key, node, parent=None):
        while True:
            if node is None or key == node.key:
                return node, parent
            elif key < node.key:
                node, parent = node.left, node
            else:
                node, parent = node.right, node

    def _pivot_up(self, node):
        parent = node.parent
        if parent is None: return

        if parent.left == node:
            node.right, parent.left = parent, node.right
            if parent.left: parent.left.parent = parent
        else:
            node.left, parent.right = parent, node.left
            if parent.right: parent.right.parent = parent

        grandparent = parent.parent
        node.parent, parent.parent = grandparent, node
        if grandparent:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node
        else:
            self.root = node

    def _prioritize(self, node):
        while node.parent and node.parent.heap_id < node.heap_id:
            self._pivot_up(node)

    def __contains__(self, key):
        node = self._find_node(key, self.root)[0]
        return node is not None

    def __getitem__(self, key):
        node = self._find_node(key, self.root)[0]
        if node is None:
            raise KeyError(key)
        else:
            return node.value

    def __delitem__(self, key):
        node, parent = self._find_node(key, self.root)

        if node is None:
            raise KeyError(key)
        elif parent is None and not (node.left and node.right):
            self.root = node.left or node.right
            if self.root: self.root.parent = None
        else:
            while node.left and node.right:
                if node.left.heap_id > node.right.heap_id:
                    self._pivot_up(node.left)
                else:
                    self._pivot_up(node.right)

            child = node.left or node.right
            if node.parent.left == node:
                node.parent.left = child
                if child: child.parent = node.parent
            else:
                node.parent.right = child
                if child: child.parent = node.parent

        node.parent = None
        node.left = None
        node.right = None


if __name__ == '__main__':
    t = Treap()
    t['a'] = 1
    print(t['a'])
    t['a'] = 2
    print(t['a'])
    del t['a']
    try:
        print(t['a'])
    except Exception as e:
        print(e)
