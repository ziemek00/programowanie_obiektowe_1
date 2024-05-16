# Zmiany po kontakcie z Panem drogą mailową (20.03.2024): 
1. Zmienienie nazw klas:
     - Ustawienie prywatnych zmiennych
2. Dodanie "odswiezenia" terminala za 1 odtworzeniem petli
3. Dodanie zamiany liczb na liczby rzymskie
4. Poprawa komentarzy, już nie znajdują się pomiędzy kodem (zostały jedynie 2 bardzo krótkie)
5. Ogólna poprawa czytelności kodu

# Zmiany po zajęciach (21.03.2024):
1. Poprawa czytelności kodu:
    - Funckcja main zawiera moim zdaniem już tylko potrzebne komendy
    - Poprawa komentarzy:
        - Usunięcie komentarzy
        - Stworzenie read.me
2. Ustawienie set oraz get points:
    - Zmiana prywatności poszczególnych zmiennych
3. Poprawa arabic_to_roman:
   - Przeniesienie z view do modelu
   - Poprawa wywoływania funkcji
4. Dodanie obsługi błędów w view oraz ogólne poprawienie MVC
5. Program zapisuje oraz wczytuje stan gry z pilku tekstowego
6. Program pyta się, czy użytkownik chce rozpocząć nową gre, czy wczytać stary zapis
7. Zmieniono jeden długi, ciągły plik na poszczególny, odpowiadający za klasy

# Zmiany po kontakcie z Panem drogą mailową (26.03.2024):
1. Zmiana klas, do których należą read_save oraz save_game
2. View->Model:
	-View "bierze" teraz dane z klasy Controller
	-Zmiana w main ustawianie kontrolera dla main oraz dodanie funckji w klasie View (set_controller), aby ustawić controller
3. Poprawa wyglądu kodu dla klasy controller: funckje są napisane w kolejności uruchamiania, w celu przejrzystości kodu

# Zmiany po kontakcie z Panem drogą mailową (03.04.2024):
1. Modyfikacja metody show_points_and_level i show_end
2. Usunięcie z View Controllera
3. Modyfikacja metody __new_or_old_game() oraz __press_button()
