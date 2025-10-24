# morse.py
import sys # Importowanie modułu sys do obsługi argumentów wiersza poleceń

MORSE_CODE = { # Słownik mapujący litery alfabetu na kod Morse’a, struktura typu dict
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..'
}


def main():
    if len(sys.argv) != 2:
        print("Użycie: python morse.py nazwa_pliku")
        sys.exit(1)

    filename = sys.argv[1]


# Można próbować jeszcze prościej po poprzednim znaku:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:  				# czytany plik linia po linii
                words = line.strip().split()
                morse_line = []  			# tu budujemy od razu całą zakodowaną linię żeby nie ładować i ładować znow
                for word in words:
                    morse_word = " ".join(
                        MORSE_CODE[ch] for ch in word.upper() if ch in MORSE_CODE
                    )
                    if morse_word:
                        morse_line.append(morse_word)
                if morse_line:
                    print(" / ".join(morse_line))
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {filename}")
        sys.exit(1)

if __name__ == "__main__":
    main()




# def text_to_morse(text): 
#     result_lines = []
#     for line in text.splitlines(): 		# rozdziela tekst po znakach nowej linii
#         words = line.strip().split() 	# strip() usuwa białe znaki z początku i końca linii, split() dzieli linię na słowa (w domyśle zostawiam po spacjach)
#         morse_words = []
#         for word in words:				# początek pętli po słowach w linii
#             morse_letters = []
#             for char in word.upper(): 	# konwertuje każdą literę na wielką literę żeby wielkość nie miała znaczenia
#                 if char in MORSE_CODE:
#                     morse_letters.append(MORSE_CODE[char]) 	# sprawdzam sobie czy literka jest w słowniku morsa i jeżeli jest to dopasowuję do niej kod morsea
#             if morse_letters:
#                 morse_words.append(" ".join(morse_letters)) # dodajemy wynikowe słowo do listy morse words
#         if morse_words:
#             result_lines.append(" / ".join(morse_words))  	# łączenie słów spacją i ukośnikiem
#     return "\n".join(result_lines)							# zwracanie słowa wynikowego 

# def main():					# moj mainik
#     if len(sys.argv) != 2:	# sprawdzam czy jest dokładnie jeden argument (nazwa pliku), jak nie to rzucam błąd
#         print("Użycie: python morse.py nazwa_pliku")
#         sys.exit(1)	

#     filename = sys.argv[1]		# otwarcie pliku
#     try:
#         with open(filename, "r", encoding="utf-8") as f: # UTF-8 żeby polskie znaki mogły działać (wiem, że na razie ich nie ma)
#             content = f.read() 	# czytam cały plik jako jeden tekst
#     except FileNotFoundError:	# obsługa błędu gdy plik nie istnieje
#         print(f"Nie znaleziono pliku: {filename}")
#         sys.exit(1)

#     result = text_to_morse(content)	# wywołanie funkcji konwertującej tekst na kod Morse’a i print resulta
#     print(result)	

# if __name__ == "__main__":	# uruchomienie maina jeżeli skrypt jest uruchamiany bezpośrednio 
#     main()
