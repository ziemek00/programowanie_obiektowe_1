# Napisz program który umożliwi mnożenie dwóch liczb całkowitych x i y podawanych z klawiatury.
# Program powinien wyświetlać wynik na ekranie. Dla wyjścia z programu użytkownik powninien wcisnąć "e"

import sys
def mnozenie():
    while True:
        while True:
            x = input("Podaj pierwszą liczbę całkowitą. Jeśli naciśniesz 'e' program skończy pracę.")
            if x.lower() == 'e':
                print('Program skończył pracę.')
                sys.exit()
            try:
                x=int(x)
                break
            except ValueError:
                print('Podano złą wartość. Spróbuj jeszcze raz wprowadzić liczbę całkowitą.')

        while True:
            y = input("Podaj pierwszą drugą całkowitą. Jeśli naciśniesz 'e' program skończy pracę.")
            if y.lower() == 'e':
                print('Program skończył pracę.')
                sys.exit()
            try:
                y=int(y)
                break
            except ValueError:
                print('Podano złą wartość. Spróbuj jeszcze raz wprowadzić liczbę całkowitą.')

        wynik = x * y
        print(f"Wynik mnożenia liczby '{x}' i liczby '{y}' to: '{wynik}' ")

mnozenie()