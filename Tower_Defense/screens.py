import pygame

class GameOverScreen:
    """Klasa odpowiedzialna za ekran końca gry."""
    def __init__(self, screen):
        """Inicjalizuje obiekt ekranu końca gry."""
        self.screen = screen
        self.game_over_image = pygame.image.load('images/game_over.png')
        self.game_over_rect = self.game_over_image.get_rect(center=(600, 400))

    def draw(self):
        """Rysuje ekran końca gry."""
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.game_over_image, self.game_over_rect)
        pygame.display.flip()

class StartScreen:
    """Klasa odpowiedzialna za ekran startowy gry."""
    def __init__(self, screen):
        """Inicjalizuje obiekt ekranu startowego gry."""
        self.screen = screen
        self.start_image = pygame.image.load('images/start.png')
        self.start_rect = self.start_image.get_rect(center=(600, 400))
        self.active = True

    def handle_event(self, event):
        """Odpowiedzialna jest za kliknięcie w "Start"."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if abs(x-600) <= 100 and abs (y - 400) <= 47:
                self.active = False

    def draw(self):
        """Rysuje ekran startowy."""
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.start_image, self.start_rect)
        pygame.display.flip()