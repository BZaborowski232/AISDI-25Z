# benchmark_trees.py
import random
import time
import gc
import matplotlib.pyplot as plt
from trees import BST, AVL

# Generator danych: 10000 liczb 1..30000
TOTAL = 10000
numbers = [random.randint(1, 30000) for _ in range(TOTAL)]

# rozmiary testowe n = 1000,2000,...,10000
Ns = [1000 * i for i in range(1, 11)]

# tablice wyników
build_bst = []
build_avl = []
search_bst = []
search_avl = []
delete_bst = []

# ---------------------
# POMIAR CZASU BUDOWY
# ---------------------
print("Measuring build times...")
for n in Ns:
    print("n =", n)
    # BST build (inserts first n)
    bst = BST()
    start = time.time()
    for x in numbers[:n]:
        bst.insert(x)
    build_bst.append(time.time() - start)

    # AVL build
    avl = AVL()
    start = time.time()
    for x in numbers[:n]:
        avl.insert(x)
    build_avl.append(time.time() - start)

# ---------------------
# POMIAR CZASU WYSZUKIWANIA
# ---------------------
print("Measuring search times (search first n keys) on tree built from full list...")
# build full trees once from whole numbers (TOTAL)
bst_full = BST()
avl_full = AVL()
for x in numbers:
    bst_full.insert(x)
    avl_full.insert(x)

for n in Ns:
    to_search = numbers[:n]
    # BST search
    gc_old = gc.isenabled()
    gc.disable()
    start = time.time()
    for key in to_search:
        bst_full.search(key)
    end = time.time()
    if gc_old:
        gc.enable()
    search_bst.append(end - start)

    # AVL search
    gc_old = gc.isenabled()
    gc.disable()
    start = time.time()
    for key in to_search:
        avl_full.search(key)
    end = time.time()
    if gc_old:
        gc.enable()
    search_avl.append(end - start)

# ---------------------
# POMIAR CZASU USUWANIA (TYLKO BST)
# ---------------------
print("Measuring delete times on BST (pop first n keys) - tree built from full list each time...")
for n in Ns:
    # build BST from full numbers
    bst_tmp = BST()
    for x in numbers:
        bst_tmp.insert(x)

    gc_old = gc.isenabled()
    gc.disable()
    start = time.time()
    for key in numbers[:n]:
        bst_tmp.delete(key)
    end = time.time()
    if gc_old:
        gc.enable()
    delete_bst.append(end - start)

# ---------------------
# RYSOWANIE WYKRESÓW
# ---------------------
# 1) build times (BST vs AVL)
plt.figure(figsize=(8,6))
plt.plot(Ns, build_bst, marker='o', label='BST (build)')
plt.plot(Ns, build_avl, marker='o', label='AVL (build)')
plt.xlabel("n (liczba elementów)")
plt.ylabel("Czas budowy (s)")
plt.title("Czas budowy: BST vs AVL")
plt.legend()
plt.grid(True)
plt.savefig("charts/build_trees.png", dpi=200)
plt.clf()

# 2) search times (BST vs AVL)
plt.figure(figsize=(8,6))
plt.plot(Ns, search_bst, marker='o', label='BST (search)')
plt.plot(Ns, search_avl, marker='o', label='AVL (search)')
plt.xlabel("n (liczba wyszukiwań)")
plt.ylabel("Czas wyszukiwania (s)")
plt.title("Czas wyszukiwania: BST vs AVL")
plt.legend()
plt.grid(True)
plt.savefig("charts/search_trees.png", dpi=200)
plt.clf()

# 3) delete times (BST)
plt.figure(figsize=(8,6))
plt.plot(Ns, delete_bst, marker='o', label='BST (delete)')
plt.xlabel("n (liczba usunięć)")
plt.ylabel("Czas usuwania (s)")
plt.title("Czas usuwania n elementów (BST)")
plt.legend()
plt.grid(True)
plt.savefig("charts/delete_bst.png", dpi=200)
plt.clf()

print("Koniec skryptu, wygenerowano: build_trees.png, search_trees.png, delete_bst.png")
