## Algorytmy i struktury danych – zadanie z kopców

### Implementacja kopców

Zaimplementuj trzy kopce zupełne: 2-arny, 5-arny i 7-arny. Każdy z kopców zaimplementuj w tablicy (liście w Pythonie). Wymagane operacje:

* wstawianie elementu do kopca,

* usuwanie szczytu kopca,

* wyświetlanie kopca na ekranie (w dowolny, ale czytelny sposób).

### Porównanie kopców

Wygeneruj wejściową listę liczb (np. 100000 losowych liczb z zakresu od 1 do 300000), która posłuży dalej do badania wydajności.

Dla każdego z kopców:

* sprawdź, czy funkcje wstawiania i usuwania działają poprawnie,

* zmierz czas tworzenia kopca na podstawie *n* pierwszych liczb listy wejściowej (np. *n* = 10000, 20000, ..., 100000),

* zmierz czas wykonania *n* operacji usunięcia szczytu kopca (np. *n* = 10000, 20000, ..., 100000) w kopcu, który dla każdego *n* został utworzony na podstawie całej listy wejściowej.

Dla każdej z operacji wygeneruj zbiorcze wykresy (jeden wykres dla trzech typów kopców) pokazujące zależność czasu wykonania operacji od liczby elementów/wykonań.

### Wyniki

Rezultatem powinny być:

* kod źródłowy z zaimplementowanymi kopcami,

* kod źródłowy przeprowadzający komplet pomiarów wydajności i generujący dwa pliki z wykresami,

* wygenerowane pliki z wykresami,

* trzy zrzuty ekranu z przykładami wyświetlania kopca (po jednym dla każdego typu kopca).

### Ocena

Zadanie oceniane jest w skali 0-6 pkt.
