from trees import BST, AVL
from tree_visualizer import display_tree  # zmieniona nazwa modułu

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]


print("===== BST EXAMPLE =====")
bst = BST()
for x in numbers:
    bst.insert(x)

print("\nStruktura drzewa BST:")
display_tree(bst)   # ASCII-art wizualizacja

print("\n===== AVL EXAMPLE =====")
avl = AVL()
for x in numbers:
    avl.insert(x)

print("\nStruktura drzewa AVL:")
display_tree(avl)   # ASCII-art wizualizacja
