# Importujemy moduł sys – pozwala odczytać argumenty
# przekazane przy uruchomieniu programu (np. nazwę pliku)
import sys

# Importujemy heapq – moduł do obsługi kolejki priorytetowej
# Jest niezbędny do algorytmu Dijkstry
import heapq

# -----------------------------
# Funkcja wczytująca planszę z pliku
# -----------------------------
def wczytaj_plansze(nazwa_pliku):
    # Otwieramy plik w trybie do odczytu
    with open(nazwa_pliku, "r") as f:
        # Każdą linię:
        # - usuwamy znak nowej linii
        # - zamieniamy na listę znaków
        plansza = [list(line.strip()) for line in f]

    # Zwracamy planszę jako listę list
    return plansza


# -----------------------------
# Funkcja wyszukująca dwa pola X
# -----------------------------
def znajdz_x(plansza):
    xs = []  # lista na współrzędne X

    # Iterujemy po wierszach
    for i in range(len(plansza)):
        # Iterujemy po kolumnach
        for j in range(len(plansza[0])):
            # Jeśli znajdziemy znak X
            if plansza[i][j] == 'X':
                # zapisujemy jego współrzędne
                xs.append((i, j))

    # Zwracamy pierwszy i drugi znaleziony X
    return xs[0], xs[1]


# -----------------------------
# Funkcja obliczająca koszt przejścia
# z pola "z" na pole "do"
# -----------------------------
def koszt_wejscia(z, do, plansza):
    # Znak na polu docelowym
    znak_do = plansza[do[0]][do[1]]

    # Znak na polu, z którego wychodzimy
    znak_z = plansza[z[0]][z[1]]

    # Jeśli wchodzimy na pole J → koszt 0
    if znak_do == 'J':
        return 0

    # Jeśli wychodzimy z pola J → koszt 0
    if znak_z == 'J':
        return 0

    # Jeśli pole docelowe jest cyfrą → koszt tej cyfry
    if znak_do.isdigit():
        return int(znak_do)

    # W pozostałych przypadkach (np. X) koszt 0
    return 0


# -----------------------------
# Algorytm Dijkstry
# -----------------------------
def dijkstra(plansza, start, meta):
    # Wysokość i szerokość planszy
    h = len(plansza)
    w = len(plansza[0])

    # Kolejka priorytetowa (koszt, pozycja)
    pq = []

    # Dodajemy punkt startowy z kosztem 0
    heapq.heappush(pq, (0, start))

    # Słownik minimalnych kosztów dojścia do pól
    dist = {start: 0}

    # Słownik poprzedników (do odtworzenia ścieżki)
    prev = {}

    # Dopóki są elementy w kolejce
    while pq:
        # Pobieramy pole o najmniejszym koszcie
        koszt, (x, y) = heapq.heappop(pq)

        # Jeśli dotarliśmy do mety – kończymy
        if (x, y) == meta:
            break

        # Sprawdzamy czterech sąsiadów
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx = x + dx
            ny = y + dy

            # Sprawdzamy, czy sąsiad mieści się w planszy
            if 0 <= nx < h and 0 <= ny < w:
                # Obliczamy koszt wejścia na sąsiada
                nowy_koszt = koszt + koszt_wejscia(
                    (x, y), (nx, ny), plansza
                )

                # Jeśli pole nie było odwiedzone
                # albo znaleźliśmy tańszą drogę
                if (nx, ny) not in dist or nowy_koszt < dist[(nx, ny)]:
                    # Aktualizujemy koszt
                    dist[(nx, ny)] = nowy_koszt

                    # Zapamiętujemy poprzednie pole
                    prev[(nx, ny)] = (x, y)

                    # Dodajemy sąsiada do kolejki
                    heapq.heappush(
                        pq, (nowy_koszt, (nx, ny))
                    )

    # -----------------------------
    # Odtwarzanie ścieżki
    # -----------------------------
    sciezka = []
    p = meta

    # Cofamy się od mety do startu
    while p != start:
        sciezka.append(p)
        p = prev[p]

    # Dodajemy punkt startowy
    sciezka.append(start)

    # Odwracamy listę (od startu do mety)
    sciezka.reverse()

    # Zwracamy ścieżkę i koszt
    return sciezka, dist[meta]


# -----------------------------
# Wypisywanie tylko pól ścieżki
# -----------------------------
def wypisz_sciezke(plansza, sciezka):
    # Zamieniamy listę ścieżki na zbiór
    # (szybsze sprawdzanie czy pole jest na trasie)
    zbior = set(sciezka)

    # Iterujemy po planszy
    for i in range(len(plansza)):
        linia = ""

        for j in range(len(plansza[0])):
            # Jeśli pole należy do ścieżki
            if (i, j) in zbior:
                # dodajemy znak do wypisania
                linia += plansza[i][j]

        # Wypisujemy tylko niepuste linie
        if linia:
            print(linia)


# -----------------------------
# Funkcja główna programu
# -----------------------------
def main():
    # Sprawdzamy, czy podano nazwę pliku
    if len(sys.argv) != 2:
        print("Użycie: python program.py plansza.txt")
        return

    # Wczytujemy planszę
    plansza = wczytaj_plansze(sys.argv[1])

    # Znajdujemy punkt startowy i końcowy
    start, meta = znajdz_x(plansza)

    # Uruchamiamy Dijkstrę
    sciezka, koszt = dijkstra(plansza, start, meta)

    # Wypisujemy planszę z ukrytą resztą pól
    wypisz_sciezke(plansza, sciezka)

    # Wypisujemy całkowity koszt
    print(f"\nKoszt: {koszt}")


# -----------------------------
# Uruchomienie programu
# -----------------------------
if __name__ == "__main__":
    main()
