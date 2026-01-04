import sys
from collections import deque

# Funkcja wczytująca funkcję przejścia maszyny Turinga z pliku
def read_transitions(file_path):
    # Słownik:
    # klucz: (stan, czytany_symbol)
    # wartość: lista możliwych przejść (niedeterminizm)
    transitions = {}

    with open(file_path) as f:
        for line in f:
            # Usuwamy białe znaki i dzielimy linię na elementy
            parts = line.strip().split()

            # Pomijamy puste linie
            if not parts:
                continue

            # Rozpakowanie elementów zgodnie z formatem zadania
            state, symbol, new_symbol, direction, new_state = parts

            # Dodajemy przejście do słownika
            # setdefault pozwala obsłużyć wiele przejść dla jednego (stan, symbol)
            transitions.setdefault((state, symbol), []).append(
                (new_symbol, direction, new_state)
            )

    return transitions


# Funkcja wypisująca aktualną konfigurację maszyny:
# - zawartość taśmy
# - aktualny stan
# - pozycję głowicy (^)
def print_tape(tape, head, state):
    # Wypisujemy taśmę jako ciąg znaków oraz nazwę stanu
    print(''.join(tape), state)

    # W drugiej linii zaznaczamy pozycję głowicy
    print(' ' * head + '^')


# Główna funkcja symulująca niedeterministyczną maszynę Turinga
def run_turing_machine(tape_str, transitions, transitions_file_name):
    # Taśma jako lista znaków (łatwiejsza modyfikacja)
    tape = list(tape_str)

    # Stan początkowy zgodnie z treścią zadania
    initial_state = 'init'

    # Kolejka do BFS – obsługa niedeterminizmu
    # Każdy element to:
    # (aktualna_taśma, pozycja_głowicy, stan, historia_konfiguracji)
    queue = deque()
    queue.append((tape, 0, initial_state, []))

    # Przeszukiwanie przestrzeni konfiguracji
    while queue:
        tape, head, state, history = queue.popleft()

        # Dodajemy bieżącą konfigurację do historii ścieżki
        history = history + [(list(tape), head, state)]

        # Sprawdzenie warunku zakończenia:
        # każdy stan zaczynający się od "halt" jest końcowy
        if state.startswith('halt'):
            # Wypisujemy całą sekwencję konfiguracji prowadzącą do halt
            for t, h, s in history:
                print_tape(t, h, s)

            # Dodatkowa funkcjonalność:
            # jeśli nazwa pliku zawiera "count1", liczymy jedynki na taśmie
            if "count1" in transitions_file_name:
                ones_count = tape.count('1')
                print(f"Liczba jedynek na taśmie: {ones_count}")

            return  # kończymy program po znalezieniu poprawnej ścieżki

        # Odczyt symbolu spod głowicy
        # Jeśli wychodzimy poza taśmę – traktujemy to jako '_'
        symbol = tape[head] if 0 <= head < len(tape) else '_'
        key = (state, symbol)

        # Jeśli nie ma żadnego przejścia – ta ścieżka obliczeń ginie
        if key not in transitions:
            continue

        # Iterujemy po wszystkich możliwych przejściach
        # (niedeterminizm)
        for new_symbol, direction, new_state in transitions[key]:
            # Tworzymy kopię taśmy, aby nie modyfikować innych ścieżek
            new_tape = tape.copy()
            new_head = head

            # Rozszerzanie taśmy w lewo, jeśli głowica wyszła poza zakres
            if new_head < 0:
                new_tape = ['_'] * (-new_head) + new_tape
                new_head = 0

            # Rozszerzanie taśmy w prawo
            if new_head >= len(new_tape):
                new_tape += ['_'] * (new_head - len(new_tape) + 1)

            # Zapis nowego symbolu na taśmie
            new_tape[new_head] = new_symbol

            # Ruch głowicy
            if direction == 'L':
                new_head -= 1
            elif direction == 'R':
                new_head += 1
            # '*' oznacza brak ruchu

            # Dodajemy nową konfigurację do kolejki BFS
            queue.append((new_tape, new_head, new_state, history))

    # Jeśli żadna ścieżka nie doprowadziła do halt
    print("Maszyna nie osiągnęła stanu halt")


# Punkt wejścia programu
if __name__ == "__main__":
    # Sprawdzamy poprawność liczby argumentów
    if len(sys.argv) != 3:
        print("Użycie: python program.py <tape> <transitions_file>")
        sys.exit(1)

    # Pobranie argumentów z linii poleceń
    tape_str = sys.argv[1]
    transitions_file = sys.argv[2]

    # Wczytanie funkcji przejścia
    transitions = read_transitions(transitions_file)

    # Uruchomienie symulacji maszyny Turinga
    run_turing_machine(tape_str, transitions, transitions_file)
