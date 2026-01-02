## Algorytmy i struktury danych – zadanie z drzew

### Implementacja drzew

Przygotuj implementacje następujących drzew:

* drzewo BST (ang. *Binary Search Tree*),

* drzewo AVL.

Wymagane operacje:

* wstawianie elementu do drzewa,

* wyszukiwanie elementu w drzewie,

* usuwanie elementu z drzewa (tylko dla drzewa BST),

* wyświetlanie drzewa na ekranie (tak, aby widoczna była jego struktura).

### Porównanie drzew

Wygeneruj wejściową listę liczb (np. 10000 losowych liczb z zakresu od 1 do 30000), która posłuży dalej do badania wydajności.

Dla każdego z drzew:

* sprawdź, czy funkcje wstawiania i wyszukiwania działają poprawnie,

* zmierz czas tworzenia drzewa na podstawie *n* pierwszych liczb listy wejściowej (np. *n* = 1000, 2000, ..., 10000),

* zmierz czasy wyszukiwania *n* pierwszych liczb listy wejściowej (np. *n* = 1000, 2000, ..., 10000) w drzewie, które dla każdego *n* zostało utworzone na podstawie całej listy wejściowej,

Wygeneruj zbiorcze wykresy (jeden wykres dla obu typów drzew) pokazujące uzyskane wyniki.

Dla drzewa BST:

* sprawdź, czy funkcja usuwania działa poprawnie,

* zmierz czasy usuwania *n* pierwszych liczb listy wejściowej (np. *n* = 1000, 2000, ..., 10000) w drzewie, które dla każdego *n* zostało utworzone na podstawie całej listy wejściowej.

Wygeneruj wykres pokazujący uzyskane wyniki.

### Wyniki

Rezultatem powinny być:

* kod źródłowy z zaimplementowanymi drzewami,

* kod źródłowy przeprowadzający komplet pomiarów wydajności i generujący trzy pliki z wykresami,

* wygenerowane pliki z wykresami,

* dwa zrzuty ekranu z przykładami wyświetlania drzew (po jednym dla każdego typu drzewa).

### Ocena

Zadanie oceniane jest w skali 0-6 pkt.