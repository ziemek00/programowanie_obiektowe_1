import pygame

class Score:
    def __init__(self, initial_score = 0):
        """Inicjalizuje obiekt klasy Score"""
        self.score = initial_score
        self.font = pygame.font.Font(None, 36)

    def add_score(self, enemy_type):
        """Dodaje punkty do wyniku w zależności od typu wroga."""
        if enemy_type == 'normal':
            self.score += 30
        elif enemy_type == 'fast':
            self.score += 45
        elif enemy_type == 'strong':
            self.score += 70

    def add_sell_points(self, points):
        """Dodaje określoną liczbę punktów do wyniku za sprzedaż wieży."""
        self.score += points
    def deduct_score(self, amount):
        """Odejmuje cenę wieży od wyniku, jeśli wynik jest wystarczający"""
        if self.score >= amount:
            self.score -= amount
            return True
        return False

    def get_score(self):
        """Zwraca aktualny wynik."""
        return self.score

    def draw(self, screen):
        """Rysuje "Money" na ekranie."""
        score_text = self.font.render(f'Money: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (screen.get_width() - score_text.get_width() - 10, 10))