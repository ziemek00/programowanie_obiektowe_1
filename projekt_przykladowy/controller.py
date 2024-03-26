import msvcrt
import os
from model import Model
from view import View

class Controller:
    def __init__(self, view, model):
        self.model = model
        self.view = view

    def pkt(self):
        return self.model.get_points()

    def lvl(self):
        return self.model.roman_level()

    def start(self):
        self.__is_there_save()

    def __is_there_save(self):
        self.file_path_save = 'save_gry.txt'
        if os.path.exists(self.file_path_save):
            self.__new_or_old_game()
        else:
            self.view.show_instructions()
            self.__press_button()

    def __new_or_old_game(self):
        self.view.create_new_game()
        while True:
            if msvcrt.kbhit():
                click = msvcrt.getch()
                if click == b'1':
                    self.model.read_save()
                    self.view.show_points_and_level()
                    self.__press_button()
                elif click == b'2':
                    self.view.show_instructions()
                    self.__press_button()
                else:
                    self.view.error_start()

    def __press_button(self):
        while True:
            if msvcrt.kbhit():
                click = msvcrt.getch()
                if click.lower() == b'e':
                    self.view.show_end()
                    self.end()
                elif click.lower() == b'b':
                    self.model.add_points()
                    self.view.show_points_and_level()
                else:
                    self.view.error_button()

    def end(self):
        self.model.save_game()
        quit()

