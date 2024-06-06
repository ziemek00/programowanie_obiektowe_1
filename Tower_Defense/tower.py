import pygame
import math
from projectile import Projectile
class Tower:
    """Bazowa klasa dla wszystkich typów wież."""
    active = False
    selected_tower_type = None
    selling_mode = False
    cost = 400

    normal_icon_image = pygame.image.load('images/tower_icon.png')
    normal_icon_image = pygame.transform.scale(normal_icon_image, (50, 70))
    normal_icon_rect = normal_icon_image.get_rect(center=(500, 50))

    fast_icon_image = pygame.image.load('images/fast_tower_icon.png')
    fast_icon_image = pygame.transform.scale(fast_icon_image, (50, 70))
    fast_icon_rect = fast_icon_image.get_rect(center=(600, 50))

    strong_icon_image = pygame.image.load('images/strong_tower_icon.png')
    strong_icon_image = pygame.transform.scale(strong_icon_image, (50, 70))
    strong_icon_rect = strong_icon_image.get_rect(center=(700, 50))

    sell_icon_image = pygame.image.load('images/sell_icon.png')
    sell_icon_image = pygame.transform.scale(sell_icon_image, (50, 50))
    sell_icon_rect = sell_icon_image.get_rect(center=(800, 50))
    def __init__(self, position, damage=10, range=200, cooldown=30, image_path='images/tower.png'):
        """Inicjalizuje obiekt wieży z domyślnymi wartościami dla obrażeń, zasięgu i czasu odnowienia."""
        self.position = position
        self.damage = damage
        self.range = range
        self.cooldown = cooldown
        self.current_cooldown = 0
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image_rect = self.image.get_rect(center=(int(self.position[0]), int(self.position[1])))
    @classmethod
    def handle_click(cls, x, y):
        """Obsługuje kliknięcia myszą na ikonach wież."""
        if cls.normal_icon_rect.collidepoint(x, y):
            cls.active = True
            cls.selected_tower_type = cls
        elif cls.fast_icon_rect.collidepoint(x, y):
            cls.active = True
            cls.selected_tower_type = FastTower
        elif cls.strong_icon_rect.collidepoint(x, y):
            cls.active = True
            cls.selected_tower_type = StrongTower
        elif cls.sell_icon_rect.collidepoint(x, y):
            cls.selling_mode = True
            cls.active = False

    @classmethod
    def draw_icons(cls, screen):
        """Rysuje ikony wież na ekranie."""
        screen.blit(cls.normal_icon_image, cls.normal_icon_rect.topleft)
        screen.blit(cls.fast_icon_image, cls.fast_icon_rect.topleft)
        screen.blit(cls.strong_icon_image, cls.strong_icon_rect.topleft)
        screen.blit(cls.sell_icon_image, cls.sell_icon_rect.topleft)

    def update(self, enemies, projectiles):
        """Aktualizuje cooldown wieży, sprawdza, czy może strzelać do wrogów"""
        if self.current_cooldown > 0:
            self.current_cooldown -= 1

        # Znalezienie najbliższego wroga
        closest_enemy = None
        closest_distance = float('inf')
        for enemy in enemies:
            distance = math.hypot(enemy.position[0] - self.position[0], enemy.position[1] - self.position[1])
            if distance < closest_distance:
                closest_distance = distance
                closest_enemy = enemy
        # Strzelanie do wroga, jeśli cooldown wynosi 0 i wróg jest w zasięgu
        if self.current_cooldown <= 0 and closest_enemy and closest_distance < self.range:
            self.shoot(closest_enemy, projectiles)
            self.current_cooldown = self.cooldown


    def shoot(self, target, projectiles):
        """Tworzy nowy pocisk skierowany w stronę wroga."""
        projectile = Projectile(self.position, target, damage=self.damage)
        projectiles.append(projectile)

    def draw(self, screen):
        """Rysuje wieżę na ekranie."""
        self.image_rect.center = (int(self.position[0]), int(self.position[1]))
        screen.blit(self.image, self.image_rect.topleft)

class FastTower(Tower):
    """Klasa reprezentująca szybko strzelającą wieżę."""
    cost = 600
    def __init__(self, position):
        super().__init__(position, damage=6, range=150, cooldown=15, image_path='images/fast_tower.png')


class StrongTower(Tower):
    """Klasa reprezentująca silną wieżę."""
    cost = 1000
    def __init__(self, position):
        super().__init__(position, damage=24, range=290, cooldown=55, image_path='images/strong_tower.png')
