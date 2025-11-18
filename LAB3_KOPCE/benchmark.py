import random
import time
import matplotlib.pyplot as plt

# Importujemy nasze trzy implementacje kopców
from heaps import BinaryHeap, FiveHeap, SevenHeap


# ===============================
# GENEROWANIE LISTY WEJŚCIOWEJ
# ===============================

# Tworzymy listę 100000 losowych liczb z zakresu 1..300000
numbers = [random.randint(1, 300000) for _ in range(100000)]

# Lista wartości n, dla których będziemy robić pomiary
Ns = [10000 * i for i in range(1, 11)]  # czyli 10000, 20000, ..., 100000


# ===============================
# TABLICE NA WYNIKI CZASÓW
# ===============================

# czasy budowania kopca
build_times_2 = []
build_times_5 = []
build_times_7 = []

# czasy usuwania n elementów
pop_times_2 = []
pop_times_5 = []
pop_times_7 = []


# ===============================
# POMIAR CZASU BUDOWANIA KOPCÓW
# ===============================

print("⏳ Trwa pomiar budowania kopców...")

for n in Ns:
    print(f"  - n = {n}")

    # --- BinaryHeap ---
    h2 = BinaryHeap()                           # Tworzymy nowy kopiec binarny (2-arny)
    start = time.time()                         # Zapisujemy aktualny czas przed rozpoczęciem wstawiania
    for x in numbers[:n]:                       # Wstawiamy pierwsze n elementów z listy numbers do kopca
        h2.insert(x)                            # Każde wywołanie h2.insert(x) zachowuje własność kopca (min-heap)
    build_times_2.append(time.time() - start)   # Obliczamy czas wstawiania wszystkich n elementów i zapisujemy go do listy build_times_2 dla późniejszego wykresu


    # --- FiveHeap ---
    h5 = FiveHeap()
    start = time.time()
    for x in numbers[:n]:
        h5.insert(x)
    build_times_5.append(time.time() - start)

    # --- SevenHeap ---
    h7 = SevenHeap()
    start = time.time()
    for x in numbers[:n]:
        h7.insert(x)
    build_times_7.append(time.time() - start)


# ===============================
# POMIAR CZASU USUWANIA ELEMENTÓW
# ===============================

print("\n Trwa pomiar usuwania elementów...")

for n in Ns:
    print(f"  - n = {n}")

    # --- BinaryHeap ---
    h2 = BinaryHeap()
    # Najpierw tworzymy kopiec z CAŁEJ listy 100000
    for x in numbers:
        h2.insert(x)

    start = time.time()
    for _ in range(n):
        h2.pop()
    pop_times_2.append(time.time() - start)

    # --- FiveHeap ---
    h5 = FiveHeap()
    for x in numbers:
        h5.insert(x)

    start = time.time()
    for _ in range(n):
        h5.pop()
    pop_times_5.append(time.time() - start)

    # --- SevenHeap ---
    h7 = SevenHeap()
    for x in numbers:
        h7.insert(x)

    start = time.time()
    for _ in range(n):
        h7.pop()
    pop_times_7.append(time.time() - start)


# ===============================
# WYKRES 1 — CZAS BUDOWANIA
# ===============================

plt.figure(figsize=(10, 6))  # większy wykres

plt.plot(Ns, build_times_2, label="Kopiec 2-arny")
plt.plot(Ns, build_times_5, label="Kopiec 5-arny")
plt.plot(Ns, build_times_7, label="Kopiec 7-arny")

plt.xlabel("Liczba elementów n")
plt.ylabel("Czas budowania (s)")
plt.title("Czas tworzenia kopca z n elementów")
plt.legend()
plt.grid(True)

plt.savefig("build_times.png", dpi=200)
plt.clf()  # czyści wykres przed następnym


# ===============================
# WYKRES 2 — CZAS USUWANIA
# ===============================

plt.figure(figsize=(10, 6))

plt.plot(Ns, pop_times_2, label="Kopiec 2-arny")
plt.plot(Ns, pop_times_5, label="Kopiec 5-arny")
plt.plot(Ns, pop_times_7, label="Kopiec 7-arny")

plt.xlabel("Liczba usunięć n")
plt.ylabel("Czas usuwania (s)")
plt.title("Czas wykonania n operacji pop()")
plt.legend()
plt.grid(True)

plt.savefig("pop_times.png", dpi=200)
plt.clf()


print("\n Gotowe, wygenerowano pliki:")
print("   • build_times.png")
print("   • pop_times.png")
