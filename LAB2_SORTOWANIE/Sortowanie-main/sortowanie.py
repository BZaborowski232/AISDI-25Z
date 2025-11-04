# sortowanie bąbelkowe: 
# Porównujemy sąsiednie elementy i zamieniamy miejscami, jeśli są w złej kolejności.
# Największe elementy „wypływają” na koniec jak bąbelki w wodzie stąd nazwa

def bubble_sort(lst):
    a = lst.copy()                                  # Tworzymy kopię listy, żeby nie modyfikować oryginału przekazanego przez użytkownika.
    n = len(a)                                      # Zmienna n to długość listy.
    for i in range(n):                              # Zewnętrzna pętla - wykonuje się n razy (każde "przejście" listy).
        for j in range(0, n - i - 1):               # Wewnętrzna pętla - za każdym razem krótsza o 1, bo ostatni element już posortowany.
            if a[j] > a[j + 1]:                     # Jeśli bieżący element większy od następnego:
                a[j], a[j + 1] = a[j + 1], a[j]     # Zamiana miejscami - „bąbelek” idzie w górę.
    return a                                        # Zwracamy posortowaną listę.


# sortowanie przez wybieranie:
# Dla każdej pozycji i:
# znajdź najmniejszy element w reszcie listy (od i+1 do końca),
# zamień go z elementem i.
#Czyli „wybierasz” najmniejszy i ustawiasz go na początku

def selection_sort(lst):
    a = lst.copy()                              # Kopia wejściowej listy.
    n = len(a)
    for i in range(n):                          # Iterujemy po wszystkich indeksach.
        min_idx = i                             # Zakładamy, że bieżący element jest najmniejszy.
        for j in range(i + 1, n):               # Szukamy faktycznie najmniejszego w dalszej części listy.
            if a[j] < a[min_idx]:               # Jeśli znajdziemy mniejszy element:
                min_idx = j                     # Zapisujemy jego indeks.
        a[i], a[min_idx] = a[min_idx], a[i]     # Zamiana miejscami: najmniejszy idzie na początek.
    return a


# sortowanie przez wstawianie: 
# Budujemy posortowaną listę od lewej strony.
# Każdy kolejny element „wstawiamy” w odpowiednie miejsce w już posortowanej części.
# Jak w grze w karty wkładana jest nowa karta w odpowiednie miejsce między poprzednimi (coś jak pasjans czy coś).

def insertion_sort(lst):
    a = lst.copy()                          # Kopia oryginalnej listy.
    for i in range(1, len(a)):              # Zaczynamy od drugiego elementu (indeks 1), bo pierwszy uznajemy za „posortowany”.
        key = a[i]                          # Element, który chcemy wstawić w odpowiednie miejsce.
        j = i - 1                           # Indeks elementu po lewej.
        while j >= 0 and a[j] > key:        # Przesuwamy elementy w prawo, dopóki są większe od klucza.
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key                      # Wstawiamy klucz w odpowiednie miejsce.
    return a


# sortowanie przez scalanie:
# To rekurencyjny algorytm dziel i zwyciężaj (divide and conquer):
# Dzielimy listę na pół.
# Sortujemy każdą połowę rekurencyjnie.
# Scalamy dwie posortowane listy w jedną.

def merge_sort(lst):
    a = lst.copy()              # Kopia listy - zachowujemy oryginał.
    if len(a) <= 1:             # Jeśli lista ma 0 lub 1 element, to jest już posortowana.
        return a

    mid = len(a) // 2           # Znajdujemy środek listy.
    left = merge_sort(a[:mid])  # Rekurencyjnie sortujemy lewą połowę.
    right = merge_sort(a[mid:]) # Rekurencyjnie sortujemy prawą połowę.

    return merge(left, right)   # Scalanie dwóch posortowanych połówek w jedną listę.


# funkcja pomocnicza do scalania
def merge(left, right):
    result = []                                 # Lista wynikowa.
    i = j = 0                                   # Wskaźniki na aktualny element lewej i prawej listy.
    while i < len(left) and j < len(right):     # Dopóki nie wyczerpaliśmy żadnej z list:
        if left[i] <= right[j]:                 # Jeśli element z lewej jest mniejszy lub równy:
            result.append(left[i])              # Dodajemy go do wyniku.
            i += 1
        else:
            result.append(right[j])             # W przeciwnym razie dodajemy element z prawej listy.
            j += 1
    result.extend(left[i:])                 # Dodajemy pozostałe elementy z lewej (jeśli jakieś zostały).
    result.extend(right[j:])                # Dodajemy pozostałe elementy z prawej.
    return result                           # Zwracamy scaloną i posortowaną listę.


# sortowanie szybkie:
# Kolejny algorytm dziel i zwyciężaj:
# Wybierz pivot (np. środkowy element),
# Podziel dane na:
# mniejsze niż pivot (left)
# równe pivotowi (middle)
# większe niż pivot (right)
# Posortuj left i right rekurencyjnie.
# Połącz: left + middle + right.

def quick_sort(lst):
    a = lst.copy()                              # Kopia wejściowej listy.
    if len(a) <= 1:                             # Jeśli lista ma 0 lub 1 element - jest już posortowana.
        return a
    pivot = a[len(a) // 2]                      # Wybieramy pivot - środkowy element listy.
    left = [x for x in a if x < pivot]          # Wszystkie mniejsze od pivot.
    middle = [x for x in a if x == pivot]       # Wszystkie równe pivotowi.
    right = [x for x in a if x > pivot]         # Wszystkie większe od pivot.
    return quick_sort(left) + middle + quick_sort(right)  # Rekurencyjne sortowanie i łączenie.
