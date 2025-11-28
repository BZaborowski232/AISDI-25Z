from trees import BST
from trees import AVL

print("BST EXAMPLE")
bst = BST()
for x in [10, 5, 20, 3, 7, 15, 30]:
    bst.insert(x)
bst.display_sideways()   # screenshot tego

print("\nAVL EXAMPLE")
avl = AVL()
for x in [10, 5, 20, 3, 7, 15, 30]:
    avl.insert(x)
avl.display_sideways()    # screenshot tego
