class View:
    def __init__(self):
        self.controller = None
        self.is_first_display = True

    def error_button(self):
        print("Musisz klikac w 'b' aby zdobywać punkty, lub w 'e' aby zakończyć grę")

    def error_start(self):
        print("Musisz kliknąć w '1' aby kontynuować grę, lub w '2' jeśli chcesz rozpocząć nową grę ")
    def show_instructions(self):
        print("To jest clicker. Naciskaj 'b' aby zdobywać puntky. Naciśnij 'e' aby zakończyć działanie programu.")

    def create_new_game(self):
        print("Posiadasz już zapis gry. Jeśli chcesz kontynuować grę wciśnij '1'. Jeśli chcesz rozpocząć nową grę wciśnij '2' ")

    def show_points_and_level(self):
        if self.is_first_display:
            print("\n" * 30)
            self.is_first_display = False
        print(f"\rPunkty: {self.controller.pktt()}, level: {self.controller.lvl()}     ", end="", flush=True)

    def show_end(self):
        print(f'\rZakończyłeś grę z wynikiem {self.controller.pktt()} i {self.controller.lvl()} poziomem.')

    def set_controller(self, controller):
        self.controller = controller

