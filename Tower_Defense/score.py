import pygame

class Score:
    def __init__(self, initial_score = 0):
        self.score = initial_score
        self.font = pygame.font.Font(None, 36)

    def add_score(self, enemy_type):
        if enemy_type == 'normal':
            self.score += 30
        elif enemy_type == 'fast':
            self.score += 45
        elif enemy_type == 'strong':
            self.score += 70

    def add_sell_points(self, points):
        self.score += points
    def deduct_score(self, amount):
        if self.score >= amount:
            self.score -= amount
            return True
        return False

    def get_score(self):
        return self.score

    def draw(self, screen):
        score_text = self.font.render(f'Money: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (screen.get_width() - score_text.get_width() - 10, 10))