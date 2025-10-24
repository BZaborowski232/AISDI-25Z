## Algorytmy i struktury danych – zadanie wstępne

### Kodowanie Morse'a

Napisz program `morse.py`, który odczytuje zawartość podanego pliku tekstowego i wyświetla na ekranie jego treść zakodowaną alfabetem Morse'a.

Alfabet ogranicz do następujących znaków (wielkość liter nie ma znaczenia):

| Litera | Kod Morse'a | Litera | Kod Morse'a | Litera | Kod Morse'a |
| ------ | ----------- | ------ | ----------- | ------ | ----------- |
| `A`    | `.-`        | `J`    | `.---`      | `S`    | `...`       |
| `B`    | `-...`      | `K`    | `-.-`       | `T`    | `-`         |
| `C`    | `-.-.`      | `L`    | `.-..`      | `U`    | `..-`       |
| `D`    | `-..`       | `M`    | `--`        | `V`    | `...-`      |
| `E`    | `.`         | `N`    | `-.`        | `W`    | `.--`       |
| `F`    | `..-.`      | `O`    | `---`       | `X`    | `-..-`      |
| `G`    | `--.`       | `P`    | `.--.`      | `Y`    | `-.--`      |
| `H`    | `....`      | `Q`    | `--.-`      | `Z`    | `--..`      |
| `I`    | `..`        | `R`    | `.-.`       |        |             |

Znaki spoza alfabetu (np. cyfry i znaki interpunkcyjne) program powinien ignorować.

Poszczególne znaki wynikowego kodu Morse'a należy oddzielać spacją, natomiast grupy znaków (słowa) ukośnikiem.

### Wywołanie programu

Wywołanie programu z linii poleceń powinno mieć postać:

    $ python morse.py nazwa_pliku

Zakładając, że `plik.txt` zawiera tekst:

    Ala ma kota
      a kot ma Ale
    a12b 3 c

wynikiem działania programu powinno być:

    $ python morse.py plik.txt
    .- .-.. .- / -- .- / -.- --- - .-
    .- / -.- --- - / -- .- / .- .-.. .
    .- -... / -.-.

Zwróć uwagę, aby wynik działania programu dla podanego przykładu był identyczny.