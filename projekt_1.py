# napisac clicker konsolowy. klikamy "b" i dostajemy za to +1 punkt. zaimplenetowac to
# uzywajac modul view control. do wyjscia z programu uzytkownik powineine nacisnac "e".
# dodatkowym zadaniem jest dodanie mechaniki poziomow: kazdy nastepny poziom to 5
# zdobytych punktow. poziomy powinny byc wyswietlane jako liczby rzymskie(napisac
# funkcje, ktora bedzie przetwarzala liczbe w liczbe rzymska). 1 tyg od teraz (czyli na
# 21 marca mam przyniesc).
class Clicker:
    def __init__(self, points, level, press):
        self.points = points
        self.level = level
        self.press = press

class __Model:
    def add_points(self):
        self.points = []
        for point in self.points:
            pass
    def add_level(self):
        self.level = []
        pass

class View:
    def show_instructions(self):
        pass
    def rome_letters(self):
        pass
    def show_points_and_level(self):
        pass

class __Controller:
    def press_button(self):
        pass
