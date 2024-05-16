import pygame

class Tower:
    def __init__(self, position):
        self.position = position
        self.image = pygame.image.load('images/marek.jpg')

    def draw(self, screen):
        screen.blit(self.image, (self.position[0] - 40, self.position[1] - 40))