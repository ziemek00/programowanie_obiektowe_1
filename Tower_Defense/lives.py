import pygame

class Lives:
    def __init__(self, screen, initial_lives=3):
        self.screen = screen
        self.lives = initial_lives
        # self.life_images = [
        #     pygame.image.load('images/life_3.png'),
        #     pygame.image.load('images/life_2.png'),
        #     pygame.image.load('images/life_1.png'),
        #     pygame.image.load('images/life_0.png'),
        # ]

    def decrease_life(self):
        if self.lives > 0:
            self.lives -= 1

    # def draw(self):
    #     life_image = self.life_images[max(0, 3 - self.lives)]
    #     self.screen.blit(life_image, (30, 30))