import pygame
from game import Game

def main():
    """Główna funkcja uruchamiająca grę."""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Tower Defense")

    game = Game(screen, 'Images/map.png')
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()