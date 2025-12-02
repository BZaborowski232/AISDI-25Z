# trees.py
# Implementacja BST (z insert, search, delete, pretty print)
# oraz AVL (z insert, search, pretty print).
# Display: prosty "sideways" print oraz print by levels.

from collections import deque

# ------------------------------
#           B S T   
# ------------------------------

class BSTNode:
    __slots__ = ("key", "left", "right")
    def __init__(self, key):
        self.key = key          # wartość klucza (porównujemy wg niego)
        self.left = None        # wskaźnik na lewe poddrzewo
        self.right = None       # wskaźnik na prawe poddrzewo

class BST:
    def __init__(self):
        self.root = None        # korzeń drzewa

    # wstawianie iteracyjne do BST
    # zasada: mniejsze na lewo, większe/ równe na prawo
    def insert(self, key):
        if self.root is None:   # przypadek gdy drzewo jest puste
            self.root = BSTNode(key)
            return
        cur = self.root
        while True:
            if key < cur.key:   # idziemy w lewo
                if cur.left is None:
                    cur.left = BSTNode(key)
                    return
                cur = cur.left
            else:               # idziemy w prawo (duplikaty też tu)
                if cur.right is None:
                    cur.right = BSTNode(key)
                    return
                cur = cur.right

    # wyszukiwanie wartości w drzewie
    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key:
                return True     # znaleziono!
            elif key < cur.key:
                cur = cur.left  # szukamy w lewym poddrzewie
            else:
                cur = cur.right # szukamy w prawym poddrzewie
        return False            # nie ma klucza w drzewie

    # usuwanie elementu – wywołuje rekurencyjną pomocniczą funkcję
    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    # klasyczny algorytm usuwania z BST
    def _delete_rec(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_rec(node.left, key)
        elif key > node.key:
            node.right = self._delete_rec(node.right, key)
        else:
            # przypadek: znaleziono node do usunięcia
            # 1) brak dzieci
            if node.left is None and node.right is None:
                return None
            # 2) jedno dziecko
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # 3) dwoje dzieci: bierzemy następnika (minimum z prawego poddrzewa)
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key  # podmieniamy klucz na następnika
            node.right = self._delete_rec(node.right, succ.key)
        return node

    # display: sideways (root on left)
    def display_sideways(self, node=None, indent=0):
        if node is None:
            node = self.root
        def _rec(n, level):
            if n is None:
                return
            _rec(n.right, level + 1)
            print("    " * level + str(n.key))
            _rec(n.left, level + 1)
        _rec(node, indent)

    # display: level-order list of lists
    def display_levels(self):
        res = []
        if not self.root:
            print("Empty")
            return
        q = deque([self.root])
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                n = q.popleft()
                level.append(n.key)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(level)
        for lvl in res:
            print(lvl)


class AVLNode:
    __slots__ = ("key", "left", "right", "height")
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1          # każdy node startuje z wysokością 1

class AVL:
    def __init__(self):
        self.root = None

    # pomocnicza: zwraca wysokość node (lub 0 gdy None)
    def _height(self, n):
        return n.height if n else 0

    # safe rotations (guarded)
    def _rotate_right(self, y):
        # guard: cannot rotate right if y or y.left is None
        if y is None or y.left is None:
            return y
        x = y.left
        T2 = x.right
        # obrót
        x.right = y
        y.left = T2
        # update heights
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x                # NOWY KORZEŃ PODDRZEWA

    # ROTACJA LEWOSTRONNA (RR case)
    def _rotate_left(self, x):
        # guard: cannot rotate left if x or x.right is None
        if x is None or x.right is None:
            return x
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        # update heights
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    # obliczanie współczynnika zbalansowania:
    # wysokość lewe - wysokość prawe
    def _balance_factor(self, n):
        return self._height(n.left) - self._height(n.right) if n else 0

    # recursive insert with balancing; IGNORE duplicate keys
    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:
            return AVLNode(key)

        # handle duplicates explicitly: ignore them
        if key == node.key:
            return node

        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        else:
            node.right = self._insert_rec(node.right, key)

        # update height and balance
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # sprawdzamy balans
        bf = self._balance_factor(node)

        # Rebalance if necessary.
        # Left Left
        if bf > 1 and node.left is not None and key < node.left.key:
            return self._rotate_right(node)
        # Left Right
        if bf > 1 and node.left is not None and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # Right Right
        if bf < -1 and node.right is not None and key > node.right.key:
            return self._rotate_left(node)
        # Right Left
        if bf < -1 and node.right is not None and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # wyszukiwanie identycznie jak w BST
    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key:
                return True
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return False

    # display: similar to BST
    def display_sideways(self, node=None, indent=0):
        if node is None:
            node = self.root
        def _rec(n, level):
            if n is None:
                return
            _rec(n.right, level + 1)
            print("    " * level + f"{n.key} (h={n.height})")
            _rec(n.left, level + 1)
        _rec(node, indent)

    def display_levels(self):
        res = []
        if not self.root:
            print("Empty")
            return
        q = deque([self.root])
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                n = q.popleft()
                level.append((n.key, n.height))
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(level)
        for lvl in res:
            print(lvl)
