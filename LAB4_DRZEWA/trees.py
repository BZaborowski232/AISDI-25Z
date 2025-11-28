# trees.py
# Implementacja BST (z insert, search, delete, pretty print)
# oraz AVL (z insert, search, pretty print).
# Display: prosty "sideways" print oraz print by levels.

from collections import deque

class BSTNode:
    __slots__ = ("key", "left", "right")
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # wstawianie (iteracyjnie)
    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left is None:
                    cur.left = BSTNode(key)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = BSTNode(key)
                    return
                cur = cur.right

    # wyszukiwanie (zwraca True/False)
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

    # usuwanie elementu (standardowy algorytm)
    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_rec(node.left, key)
        elif key > node.key:
            node.right = self._delete_rec(node.right, key)
        else:
            # node to delete
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # two children: find successor (min in right subtree)
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key
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
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    # helper height
    def _height(self, n):
        return n.height if n else 0

    # rotations
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _balance_factor(self, n):
        return self._height(n.left) - self._height(n.right) if n else 0

    # recursive insert with balancing
    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        else:
            node.right = self._insert_rec(node.right, key)

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        bf = self._balance_factor(node)

        # Left Left
        if bf > 1 and key < node.left.key:
            return self._rotate_right(node)
        # Right Right
        if bf < -1 and key > node.right.key:
            return self._rotate_left(node)
        # Left Right
        if bf > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # Right Left
        if bf < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # search
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


