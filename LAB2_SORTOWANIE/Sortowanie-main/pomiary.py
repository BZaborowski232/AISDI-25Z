import time
import gc
import matplotlib.pyplot as plt
from sortowanie import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

# Wczytujemy dane
with open("pan-tadeusz.txt", "r", encoding="utf-8") as f:
    words = f.read().split()

words = [w.lower() for w in words]

# W tym punkcie lista rozmiarów testowych
sizes = list(range(1000, 10001, 1000))

# wszystkie funkcje, jakie mam przetestować. Spróbuję to zrobić żeby było jak najmniej kodu, jak najmniejsza złożoność zgodnie z uwagami prowadzącego
#  jak nie, to rozbiję na osobne pliki jak wcześniej
algorithms = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
}

for name, func in algorithms.items():
    times = []

    print(f"Testuję: {name}")
    for n in sizes:
        sample = words[:n]

        gc_old = gc.isenabled()
        gc.disable()
        start = time.time()
        func(sample)
        end = time.time()
        if gc_old:
            gc.enable()

        times.append(end - start)
        print(f"  n={n}  czas={end - start:.4f}s")

    # Kod do generowania wykresów, korzystam z biblio matplotlib  
    plt.style.use('dark_background')
    plt.figure()	
    plt.plot(sizes, times, marker='h', color = 'yellow')
    plt.xlabel("Liczba elementów")
    plt.ylabel("Czas [s]")
    plt.title(f"Czas sortowania - {name}")
    plt.grid(True, color='gray', linestyle='--', linewidth=1.5)
    plt.savefig(f"Wykresy_wynikowe/{name}.png")
    plt.close()

# Info zwrotne na koniec, opcjonalnie ale dzięki temu widzę, że skrypt się zakończył, a wcześniej nie generował wykresów i idk czy 
# się w ogóle kończył po wywołaniu
print("Zakończono testy. Wykresy zapisane w folderze /Wykresy_wynikowe/")
