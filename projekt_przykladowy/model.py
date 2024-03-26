class Model:
    def __init__(self):
        self.__points = 0
        self.__level = 0

    def get_points(self):
        return self.__points

    def set_points(self, points):
        self.__points = points
        self.__add_level()

    def add_points(self):
        self.set_points(self.__points + 1)

    def __add_level(self):
        self.__level = self.__points // 5 + 1

    def roman_level(self):
        return self.arabic_to_roman(self.__level)

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

    def read_save(self):
        self.file_path_save = 'save_gry.txt'
        with open(self.file_path_save, 'r') as file_object:
            lines = file_object.readlines()
            points_line = lines[0]
            points = int(points_line.strip().split(': ')[1])
            self.set_points(points)

    def save_game(self):
        file_path_save = 'save_gry.txt'
        with open(file_path_save, 'w') as file_object:
            file_object.write(f'Punkty: {self.get_points()} \nLevel:  {self.roman_level()}')
