# napisac clicker konsolowy. klikamy "b" i dostajemy za to +1 punkt. zaimplenetowac to
# uzywajac modul view control. do wyjscia z programu uzytkownik powineine nacisnac "e".
# dodatkowym zadaniem jest dodanie mechaniki poziomow: kazdy nastepny poziom to 5
# zdobytych punktow. poziomy powinny byc wyswietlane jako liczby rzymskie(napisac
# funkcje, ktora bedzie przetwarzala liczbe w liczbe rzymska). 1 tyg od teraz (czyli na
# 21 marca mam przyniesc).

class __Model:
    def __init__(self):
        self.points = 0
        self.level = 1
    def add_points(self):
        self.points += 1
        self.add_level()
        print(self.points)
    def add_level(self):
        self.level = self.points // 5 + 1

class View:
    def __init__(self, model):
        self.model = model
    def show_instructions(self):
        print("To jest clicker. Naciskaj 'b' aby zdobywać puntky. Naciśnij 'e' aby zakończyć działanie programu.")
    def show_points_and_level(self):
        pass
    def show_end(self):
        print(f'Zakończyłeś grę z wynikiem {self.model.points} i {self.model.level} poziomem.')
        quit()

class __Controller:
    def __init__(self, view, model):
        self.model = model
        self.view = view
    def press_button(self):
        self.points = []
        while True:
            click = input()
            if click.lower() == 'e':
                self.view.show_end()
            if click.lower() == 'b':
                self.model.add_points()
            else:
                print("Musisz klikac w 'b' aby zdobyć punkt, lub w 'e' aby zakończyć grę")

def main():
    model = __Model()
    view = View(model)
    controller = __Controller(view, model)
    view.show_instructions()
    controller.press_button()

if __name__ == "__main__":
    main()