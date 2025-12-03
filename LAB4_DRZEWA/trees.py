# -------------------
# Węzeł drzewa BST
# -------------------
class BSTNode:
    __slots__ = ("key", "left", "right")  
    def __init__(self, key):
        self.key = key      # wartość węzła
        self.left = None    # lewe dziecko
        self.right = None   # prawe dziecko

# -------------------
# BST (Binary Search Tree)
# -------------------
class BST:
    def __init__(self):
        self.root = None  # korzeń drzewa

    # Wstawianie klucza do drzewa (iteracyjnie)
    def insert(self, key):
        if self.root is None:  # jeśli drzewo jest puste
            self.root = BSTNode(key)
            return
        cur = self.root
        while True:
            if key < cur.key:          # jeśli klucz mniejszy od bieżącego
                if cur.left is None:   # jeśli nie ma lewego dziecka, wstaw tutaj
                    cur.left = BSTNode(key)
                    return
                cur = cur.left         # idź w lewo
            else:
                if cur.right is None:  # jeśli nie ma prawego dziecka, wstaw tutaj
                    cur.right = BSTNode(key)
                    return
                cur = cur.right        # idź w prawo

    # Wyszukiwanie klucza w drzewie, zwraca True/False
    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key:  # znaleziono
                return True
            elif key < cur.key:  # idź w lewo
                cur = cur.left
            else:               # idź w prawo
                cur = cur.right
        return False

    # Usuwanie klucza z drzewa (standardowy algorytm BST)
    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node, key):
        if node is None:  # nic do usunięcia
            return None
        if key < node.key:       # szukaj w lewym poddrzewie
            node.left = self._delete_rec(node.left, key)
        elif key > node.key:     # szukaj w prawym poddrzewie
            node.right = self._delete_rec(node.right, key)
        else:  # znaleziono węzeł do usunięcia
            if node.left is None and node.right is None:
                return None  # węzeł liść → usuń
            if node.left is None:
                return node.right  # tylko prawe dziecko → podnieś w górę
            if node.right is None:
                return node.left   # tylko lewe dziecko → podnieś w górę
            # węzeł ma dwoje dzieci → znajdź sukcesora (min w prawym poddrzewie)
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key
            node.right = self._delete_rec(node.right, succ.key)
        return node

# -------------------
# Węzeł drzewa AVL
# -------------------
class AVLNode:
    __slots__ = ("key", "left", "right", "height")
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # wysokość węzła (potrzebna do balansowania)

# -------------------
# AVL (zbalansowane BST)
# -------------------
class AVL:
    def __init__(self):
        self.root = None  # korzeń drzewa

    # Pomocnicza funkcja do odczytu wysokości węzła
    def _height(self, n):
        return n.height if n else 0

    # Rotacja w prawo (bezpieczna)
    def _rotate_right(self, y):
        if y is None or y.left is None:  # nic do rotacji
            return y
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        # Aktualizacja wysokości
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x

    # Rotacja w lewo (bezpieczna)
    def _rotate_left(self, x):
        if x is None or x.right is None:
            return x
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        # Aktualizacja wysokości
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    # Obliczanie współczynnika balansowania
    def _balance_factor(self, n):
        return self._height(n.left) - self._height(n.right) if n else 0

    # Wstawianie klucza z rekurencyjnym balansowaniem
    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:  # jeśli pusty węzeł → stwórz
            return AVLNode(key)

        # Pomijamy duplikaty
        if key == node.key:
            return node

        # Idź w lewo/prawo
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        else:
            node.right = self._insert_rec(node.right, key)

        # Aktualizacja wysokości i współczynnika balansowania
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        bf = self._balance_factor(node)

        # Balansowanie drzewa jeśli współczynnik poza zakresem [-1,1]
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

    # Wyszukiwanie klucza w AVL, zwraca True/False
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
