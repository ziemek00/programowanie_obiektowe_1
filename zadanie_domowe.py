# Napisz program który umożliwi mnożenie dwóch liczb całkowitych x i y podawanych z klawiatury.
# Program powinien wyświetlać wynik na ekranie. Dla wyjścia z programu użytkownik powninien wcisnąć "e"

def mnozenie():

    while True:
        x = input("Podaj pierwszą liczbę całkowitą. Jeśli naciśniesz 'e' program skończy pracę.")
        if x.lower() == 'e':
            print('Program skończył pracę.')
            break
        try:
            x=int(x)
            break
        except ValueError:
            print('Podano złą wartość. Spróbuj jeszcze raz wprowadzić liczbę całkowitą.')

    while True:
        x = input("Podaj pierwszą liczbę całkowitą. Jeśli naciśniesz 'e' program skończy pracę.")
        if x.lower() == 'e':
            print('Program skończył pracę.')
            break
        try:
            x=int(x)
            break
        except ValueError:
            print('Podano złą wartość. Spróbuj jeszcze raz wprowadzić liczbę całkowitą.')