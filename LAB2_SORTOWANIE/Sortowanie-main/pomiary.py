import time
import gc
import matplotlib.pyplot as plt
from sortowanie import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

# Wczytujemy dane; wczytywanie pliku odbywa się wyłącznie raz na początku, a więc nie wpływa na pomiary czasów sortowania
with open("pan-tadeusz.txt", "r", encoding="utf-8") as f:
    words = f.read().split()

words = [w.lower() for w in words]  # konwersja na małe litery w razie czego dla spójności

# lista rozmiarów testowych
sizes = list(range(1000, 10001, 1000))

# wszystkie funkcje, jakie mam przetestować. Spróbuję to zrobić żeby było jak najmniej kodu, jak najmniejsza złożoność zgodnie z uwagami od pana
#  a jak nie, to rozbiję to sobie na osobne pliki jak wcześniej chciałem
algorithms = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
}

# pętla pomiarowa po wszystkich algorytmach dla różnych rozmiarów danych
for name, func in algorithms.items():       # algorithms to słownik, więc rozpakowuję klucze i wartości przez .items()
    times = []                              # pusta lista na czasy wykonywania dla danego algorytmu

    print(f"Testuję: {name}")               
    for n in sizes:                         # pętla po rozmiarach danych
        sample = words[:n]                  # wycinek danych do posortowania

        gc_old = gc.isenabled()             # wyłączam garbage collector na czas sortowania, żeby na pewno nie wpływał na pomiary
        gc.disable()
        start = time.time()                 # start pomiaru czasu
        func(sample)                        # wywołanie każdego kolejnego skryptu sortowania na próbce danych
        end = time.time()                   # koniec pomiaru czasu
        if gc_old:
            gc.enable()                     # przywracam garbage collector do poprzedniego stanu

        times.append(end - start)           # zapisuję zmierzony czas do listy
        print(f"  n={n}  czas={end - start:.4f}s")      # informacja zwrotna w trakcie działania skryptu no i koniec pętli

    # Kod do generowania wykresów, korzystam sb z biblio matplotlib  
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
