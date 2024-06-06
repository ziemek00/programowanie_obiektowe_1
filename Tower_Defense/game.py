import pygame
import random
from map import Map
from enemy import Enemy
from tower import Tower, FastTower, StrongTower
from screens import  GameOverScreen, StartScreen
from lives import Lives
from score import Score

class Game:
    """Klasa odpowiedzialna za główną logikę gry."""
    def __init__(self, screen, map_image):
        self.screen = screen
        self.clock=pygame.time.Clock()
        self.map=Map(map_image)
        self.running = True
        self.enemies = []
        self.towers = []
        self.projectiles = []
        self.spawn_timer = 0
        self.game_timer = 0
        self.lives = Lives(screen)
        self.start_screen = StartScreen(screen)
        self.game_over_screen = GameOverScreen(screen)
        self.score = Score(initial_score=1500)

    def run(self):
        """Uruchamia główną pętlę gry."""
        while self.running:
            self.handle_events()
            if not self.start_screen.active:
                if self.lives.lives > 0:
                    self.update()
                self.render()
            else:
                self.start_screen.draw()
            self.clock.tick(60)

    def spawn_enemy(self):
        """Losuje, którego wroga zrodzi gra."""
        enemy_type = random.choice(['normal', 'fast', 'strong'])
        self.enemies.append(Enemy(self.map.waypoints, enemy_type))

    def handle_events(self):
        """Obsługuje zdarzenia gry."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif self.start_screen.active:
                self.start_screen.handle_event(event)
            elif self.lives.lives > 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    # Sprawdzenie, czy kliknięto na ikonę wieży
                    if self.is_click_on_icon(x, y):
                        Tower.handle_click(x, y)
                    else:
                        if Tower.selling_mode:
                            self.sell_tower(x, y)
                        elif Tower.active:
                            self.place_tower(x, y)
            elif self.lives.lives <= 0:
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    self.running = False
    def is_click_on_icon(self, x, y):
        """Sprawdza, czy kliknięto na ikonę wieży lub sprzedaży."""
        return (Tower.normal_icon_rect.collidepoint(x, y) or
                Tower.fast_icon_rect.collidepoint(x, y) or
                Tower.strong_icon_rect.collidepoint(x, y) or
                Tower.sell_icon_rect.collidepoint(x, y))

    def place_tower(self, x, y):
        """Umieszcza wieżę na mapie, jeśli to możliwe."""
        if not Tower.active:
            return

        tower_type = Tower.selected_tower_type
        cost = tower_type.cost

        for tower_waypoint in self.map.tower_waypoints:
            if abs(tower_waypoint[0] - x) < 20 and abs(tower_waypoint[1] - y) < 20:
                for tower in self.towers:
                    if tower.position == tower_waypoint:
                        return
                self.towers.append(tower_type(tower_waypoint))
                self.score.deduct_score(cost)
                Tower.active = False
                return

    def sell_tower(self, x, y):
        """Sprzedaje wieżę i dodaje punkty do wyniku."""
        for tower in self.towers:
            if abs(tower.position[0] - x) < 20 and abs(tower.position[1] - y) < 20:
                if isinstance(tower, FastTower):
                    sell_value = 450
                elif isinstance(tower, StrongTower):
                    sell_value = 750
                else:
                    sell_value = 300
                self.score.add_sell_points(sell_value)
                self.towers.remove(tower)
                Tower.selling_mode = False
                return

    def generate_enemies(self):
        """Generuje wrogów w losowych odstępach czasowych."""
        self.spawn_timer += self.clock.get_time()
        if self.spawn_timer >= 1000:
            self.spawn_timer = 0
            # Losowe generowanie wrogów z różnym prawdopodobieństwem w zależności od czasu gry
            if self.game_timer < 20:
                if random.randint(1, 5) > 4:
                    self.spawn_enemy()
            elif self.game_timer < 40:
                if random.randint(1, 5) > 3:
                    self.spawn_enemy()
            elif self.game_timer < 60:
                if random.randint(1, 5) > 2:
                    self.spawn_enemy()
            elif self.game_timer < 80:
                if random.randint(1, 5) > 1:
                    self.spawn_enemy()
            else:
                if random.randint(1, 5) > 0:
                    self.spawn_enemy()
    def update(self):
        """Aktualizuje stan gry."""
        self.game_timer += self.clock.get_time() / 1000
        if self.lives.lives > 0:
            self.generate_enemies()

            for enemy in self.enemies:
                enemy.update()
                if enemy.current_wp == len(enemy.waypoints) - 1:
                    self.enemies.remove(enemy)
                    self.lives.decrease_life()

            for enemy in self.enemies[:]:
                if not enemy.alive:
                    self.score.add_score(enemy.get_type())
                    self.enemies.remove(enemy)

            for tower in self.towers:
                tower.update(self.enemies, self.projectiles)

            for projectile in self.projectiles:
                projectile.update()
                if not projectile.alive:
                    self.projectiles.remove(projectile)

    def render(self):
        """Renderuje wszystkie elementy gry na ekranie."""
        self.screen.fill((0, 0, 0))
        if self.lives.lives > 0:
            self.map.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)
            for tower in self.towers:
                tower.draw(self.screen)
            for projectile in self.projectiles:
                projectile.draw(self.screen)
            self.lives.draw()
            Tower.draw_icons(self.screen)
            self.score.draw(self.screen)
        else:
            self.render_game_over()
        pygame.display.flip()

    def render_game_over(self):
        """Wyświetla ekran końca gry."""
        self.screen.fill((0, 0, 0))
        self.game_over_screen.draw()
        pygame.display.flip()