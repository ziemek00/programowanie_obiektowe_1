# napisac clicker konsolowy. klikamy "b" i dostajemy za to +1 punkt. zaimplenetowac to
# uzywajac modul view control. do wyjscia z programu uzytkownik powineine nacisnac "e".
# dodatkowym zadaniem jest dodanie mechaniki poziomow: kazdy nastepny poziom to 5
# zdobytych punktow. poziomy powinny byc wyswietlane jako liczby rzymskie(napisac
# funkcje, ktora bedzie przetwarzala liczbe w liczbe rzymska). 1 tyg od teraz (czyli na
# 21 marca mam przyniesc).

import msvcrt  #to jest import dla windowsa, dla systemów linux w tym miejscu import curses
# import os   do "odswiezania" terminala, w razie jakby nie działało odświeżanie
# z powodu innego środowsika

class __Model:
    def __init__(self):
        self.points = 0
        self.level = 1
    def add_points(self):
        self.points += 1
        self.add_level()
    def add_level(self):
        self.level = self.points // 5 + 1

class View:
    def __init__(self, model):
        self.model = model
    def show_instructions(self):
        print("To jest clicker. Naciskaj 'b' aby zdobywać puntky. Naciśnij 'e' aby zakończyć działanie programu.")
    def show_points_and_level(self):
        # if os.name == 'nt':
        #     os.system('cls')
        # else:
        # (jakby system operacyjny to nie był windowsem)
        # os.system('clear')
        # print("\n" * 30)-druga opcja "odswieżania"
        # nie działa mi jedno pod drugim, musi być obok siebie
        # mi to odświeża "w miejscu", ale możliwe, że na innych systemach/w innym kompilatorze tak nie będzie,
        # więc w razie czego można użyć alternatywnych opcji "odświeżania"
        print(f"\rPunkty: {self.model.points}, level: {self.model.level}", end="", flush=True)
    def show_end(self):
        print(f'Zakończyłeś grę z wynikiem {self.model.points} i {self.model.level} poziomem.')
        quit()

class __Controller:
    def __init__(self, view, model):
        self.model = model
        self.view = view
    def press_button(self):
        while True:
            if msvcrt.kbhit():
                click = msvcrt.getch()
                if click.lower() == b'e':
                    self.view.show_end()
                elif click.lower() == b'b':
                    self.model.add_points()
                    self.view.show_points_and_level()
                else:
                    print("Musisz klikac w 'b' aby zdobywać punkty, lub w 'e' aby zakończyć grę")
        # to dziala tylko na systemach windows


def main():
    model = __Model()
    view = View(model)
    controller = __Controller(view, model)
    view.show_instructions()
    controller.press_button()

if __name__ == "__main__":
    main()

# import curses
#
# def press_button(stdscr, model, view):
#     while True:
#         click = stdscr.getch()
#         if click == ord('e'):
#             view.show_end()
#             break
#         elif click == ord('b'):
#             self.model.add_points()
#             self.view.show_points_and_level()
#         else:
#             stdscr.addstr("Musisz klikac w 'b' aby zdobywać punkty, lub w 'e' aby zakończyć grę")
#             stdscr.refresh()
# to działa na systemach linux(prawdopodobnie)