## Algorytmy i struktury danych – zadanie z grafów

### Problem

Dana jest prostokątna plansza o dowolnych wymiarach. Na planszy znajdują się dwie litery `X`. Na pozostałych polach planszy znajdują się cyfry z przedziału od 0 do 9 lub litery `J`. Na przykład:

    J112J
    12X21
    J041J
    12X11
    J111J

Przyjmijmy teraz, że po polach można się przemieszczać w kierunkach prawo-lewo i góra-dół (lecz nie na skos). Niech cyfry oznaczają koszt wejścia na dane pole, za wyjątkiem sytuacji, gdy wchodzimy na nie z pola z literą `J`. Koszt wejścia na pole z literą `J` (od ang. *joker*, żartowniś), a także koszt opuszczenia pola z literą `J`, wynoszą 0. Zadanie polega na napisaniu programu, który:

1. wczyta planszę z pliku (nazwa pliku przekazana jako argument wywołania programu);

2. korzystając z algorytmu Dijkstry, znajdzie dowolną z najmniej kosztownych tras przejścia pomiędzy pierwszą (licząc od początku pliku) literą `X` a drugą;

3. ukryje pola planszy, które nie leżą na znalezionej trasie oraz poda całkowity koszt znalezionej trasy.

Przykładowo, zakładając, że plik `graf1.txt` zawiera pokazaną wcześniej planszę, wynikiem działania programu może być:

    $ python program.py graf1.txt
    J11
    1 X
    J
    1 X
    J11

    Koszt: 3

*Uwaga:* Można założyć poprawność wejściowego pliku.

### Wyniki

Rezultatem powinny być:

* kod źródłowy programu;

* 3 pliki tekstowe z przykładowymi planszami (innymi niż plansza z treści zadania) o różnych wymiarach;

* trzy zrzuty ekranu z wynikami działania programu dla przykładowych plansz.

### Ocena

Zadanie oceniane jest w skali 0-6 pkt.