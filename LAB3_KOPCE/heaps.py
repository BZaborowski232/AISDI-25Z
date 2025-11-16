# Klasa bazowa implementująca ogólny kopiec k-arny.
# Wszystkie inne kopce (2-, 5-, 7-arny) będą po niej dziedziczyć.

class KHeap:
    def __init__(self, k):
        # k określa ile dzieci ma każdy węzeł (np. 2, 5, 7)
        self.k = k
        # data to lista, w której przechowujemy elementy kopca
        self.data = []

    def parent(self, i):
        # Zwraca indeks rodzica elementu na indeksie i
        # Wzór dla k-arnego kopca: (i - 1) // k
        return (i - 1) // self.k

    def children(self, i):
        # Zwraca zakres indeksów dzieci węzła i
        # Dzieci są na pozycjach: k*i + 1, ..., k*i + k
        start = self.k * i + 1
        end = start + self.k
        # range nie tworzy listy, ale jest wystarczający
        return range(start, end)

    def insert(self, value):
        # Dodajemy nowy element na koniec tablicy
        self.data.append(value)
        # Następnie przesuwamy go w górę, aby zachować własność kopca
        self._sift_up(len(self.data) - 1)

    def _sift_up(self, i):
        # Funkcja przesuwa element o indeksie i w górę drzewa
        # dopóki nie znajdzie poprawnej pozycji.
        while i > 0:  # dopóki element nie jest korzeniem
            parent_index = self.parent(i)
            # Jeśli element jest mniejszy niż rodzic – zamieniamy (kopiec minimalny)
            if self.data[i] < self.data[parent_index]:
                # Zamiana miejscami
                self.data[i], self.data[parent_index] = self.data[parent_index], self.data[i]
                # Przesuwamy się do rodzica
                i = parent_index
            else:
                # Jeśli element nie jest mniejszy od rodzica, własność kopca jest zachowana
                break

    def pop(self):
        # Usunięcie szczytu kopca (korzenia)
        if not self.data:  # jeśli kopiec pusty → nic nie usuwamy
            return None

        # Zapisujemy korzeń (który zwrócimy)
        root_value = self.data[0]

        # Bierzemy ostatni element i przesuwamy go na miejsce korzenia
        last_value = self.data.pop()

        # Jeśli kopiec stał się pusty PO usunięciu ostatniego elementu
        if not self.data:
            return root_value

        # Umieszczamy ostatni element na szczycie
        self.data[0] = last_value

        # Przesuwamy go w dół, aby przywrócić własność kopca
        self._sift_down(0)

        # Zwracamy poprzedni korzeń
        return root_value

    def _sift_down(self, i):
        # Funkcja przesuwa element o indeksie i w dół drzewa
        # wybierając mniejsze dziecko (dla kopca minimalnego)
        n = len(self.data)  # aktualna liczba elementów

        while True:
            # Pobieramy listę rzeczywistych istniejących dzieci
            child_indices = [c for c in self.children(i) if c < n]

            # Jeśli brak dzieci → kończymy
            if not child_indices:
                break

            # Szukamy najmniejszego dziecka
            min_child = min(child_indices, key=lambda c: self.data[c])

            # Jeśli dziecko jest mniejsze niż element → zamieniamy
            if self.data[min_child] < self.data[i]:
                self.data[min_child], self.data[i] = self.data[i], self.data[min_child]
                i = min_child  # schodzimy niżej
            else:
                # Własność kopca nie wymaga dalszych zamian
                break

    def show(self):
        # Funkcja wyświetla kopiec poziomami (dla czytelności)
        # Można zrobić to różnie, ale taka wersja jest prosta.
        level = 0      # aktualny poziom drzewa
        index = 0      # indeks elementu w tablicy

        # Dopóki nie wyświetliliśmy wszystkich elementów:
        while index < len(self.data):
            # Liczba elementów na danym poziomie: k^level
            count = self.k ** level

            # Wyświetlamy elementy tego poziomu
            print(self.data[index:index + count])

            # Przechodzimy do następnego poziomu
            index += count
            level += 1


# Poniżej mamy trzy klasy kopców dziedziczące po KHeap,
# każda z nich ustawia tylko wartość k.


class BinaryHeap(KHeap):
    def __init__(self):
        # Kopiec 2-arny
        super().__init__(2)


class FiveHeap(KHeap):
    def __init__(self):
        # Kopiec 5-arny
        super().__init__(5)


class SevenHeap(KHeap):
    def __init__(self):
        # Kopiec 7-arny
        super().__init__(7)


# Sekcja testowa — uruchomi się tylko jeśli plik odpalasz ręcznie
# (np. "python3 heaps.py")
# Nie będzie się uruchamiać przy imporcie w benchmark.py

if __name__ == "__main__":
    # Testowy kopiec binarny
    h = BinaryHeap()

    # Wstawiamy kilka elementów
    h.insert(5)
    h.insert(2)
    h.insert(8)
    h.insert(1)
    h.insert(3)

    print("Kopiec po wstawieniach:")
    h.show()

    # Usuwamy korzeń
    print("\nUsunięty korzeń:", h.pop())

    print("\nKopiec po usunięciu:")
    h.show()
