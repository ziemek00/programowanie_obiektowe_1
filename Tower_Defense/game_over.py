import pygame

class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.game_over_image = pygame.image.load('images/game_over.png')
        self.game_over_rect = self.game_over_image.get_rect(center=(600, 400))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.game_over_image, self.game_over_rect)
        pygame.display.flip()