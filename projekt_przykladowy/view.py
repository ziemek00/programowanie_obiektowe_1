class View:
    def __init__(self):
        self.is_first_display = True

    def error_button(self):
        print("Musisz klikac w 'b' aby zdobywać punkty, lub w 'e' aby zakończyć grę")

    def error_start(self):
        print("Musisz kliknąć w '1' aby kontynuować grę, lub w '2' jeśli chcesz rozpocząć nową grę ")
    def show_instructions(self):
        print("To jest clicker. Naciskaj 'b' aby zdobywać puntky. Naciśnij 'e' aby zakończyć działanie programu.")

    def create_new_game(self):
        print("Posiadasz już zapis gry. Jeśli chcesz kontynuować grę wciśnij '1'. Jeśli chcesz rozpocząć nową grę wciśnij '2' ")

    def show_points_and_level(self, points, level):
        if self.is_first_display:
            print("\n" * 30)
            self.is_first_display = False
        print(f"\rPunkty: {points}, level: {level}     ", end="", flush=True)

    def show_end(self, points, level):
        print(f'\rZakończyłeś grę z wynikiem {points} i {level} poziomem.')

