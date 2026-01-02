Schemat działania: 
python program.py <zawartosc_taśmy> <plik_funkcji_przejścia>

Z katalogu projektu (LAB6) odpalasz jedną z tych trzech komend:

Komendy:
python3 program.py 1011 transitions_add1.txt        --> dodawanie 1 do liczby binarnej
python3 program.py 101101 transitions_ends01.txt    --> sprawdzenie czy liczba kończy się na 01 
python3 program.py 01001 transitions_flip0to1.txt   --> zamiana wszystkich 0 na 1

Nowe pliki inne niz te z instrukcji:
python3 program.py 1011 NEW_transitions_double1.txt     --> podwaja liczbę binarną
python3 program.py 101101 NEW_transitions_count1.txt    --> liczy ile jest jedynek na taśmie
python3 program.py 01001 NEW_transitions_flip0to1.txt   --> zamiana wszystkich 0 na 1