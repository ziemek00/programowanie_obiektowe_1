import msvcrt
class Model:
    def __init__(self):
        self.points = 0
        self.level = 0

    def add_points(self):
        self.points += 1
        self.__add_level()

    def __add_level(self):
        self.level = self.points // 5 + 1

class View:
    def __init__(self, model):
        self.model = model
        self.is_first_display = True

    @property
    def roman_level(self):
        return self.arabic_to_roman(self.model.level)

    def show_instructions(self):
        print("To jest clicker. Naciskaj 'b' aby zdobywać puntky. Naciśnij 'e' aby zakończyć działanie programu.")

    def arabic_to_roman(self, number: int) -> str:
        romans = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
                  ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                  ["C", 100], ["CD", 400], ["D", 500],
                  ["CM", 900], ["M", 1000]]
        result = ""
        for symbol, value in reversed(romans):
            while number // value:
                count = number // value
                result += (symbol * count)
                number = number % value
        return result

    def show_points_and_level(self):
        if self.is_first_display:
            print("\n" * 30)
            self.is_first_display = False
        print(f"\rPunkty: {self.model.points}, level: {self.roman_level}    ", end="", flush=True)
        # taki odstęp tutaj, ponieważ jak go nie ma, to w miejscu "migania" kursora pojawiają się liczby rzymskie

    def show_end(self):
        print(f'\rZakończyłeś grę z wynikiem {self.model.points} i {self.roman_level} poziomem.')
        quit()

class Controller:
    def __init__(self, view, model):
        self.model = model
        self.view = view

    def __press_button(self): # to dziala tylko na systemach windows
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

    def start(self):
        self.__press_button()

def main():
    model = Model()
    view = View(model)
    controller = Controller(view, model)
    view.show_instructions()
    controller.start()

if __name__ == "__main__":
    main()

# import os   do "odswiezania" terminala, w razie jakby nie działało odświeżanie
# z powodu innego środowsika
# if os.name == 'nt':
#     os.system('cls')
# else:
# (jakby system operacyjny to nie był windowsem)
# os.system('clear')
# print("\n" * 30)-druga opcja "odswieżania"
# nie działa mi jedno pod drugim, musi być obok siebie
# mi to odświeża "w miejscu", ale możliwe, że na innych systemach/w innym kompilatorze tak nie będzie,
# więc w razie czego można użyć alternatywnych opcji "odświeżania"
#
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

# zmiany po kontaktu z Panem: zmienienie nazw klas, ustawienie prywatnych klas: __press_button oraz __add_level
# dodanie "odswiezenia" terminala za 1 odtworzeniem petli
# dodanie zamiany liczb na liczby rzymskie (leetcode 12)
# poprawa komentarzy, już nie znajdują się pomiędzy kodem (zostały jedynie 2 bardzo krótkie)
# poprawa czytelności kodu