import pygame
import random
from map import Map
from enemy import Enemy
from tower import Tower
from start import StartScreen
from game_over import GameOverScreen
from lives import Lives

# czekałem raz 27 sekund na pierwszego moba przez rng
class Game:
    def __init__(self, screen, map_image):
        self.screen = screen
        self.clock=pygame.time.Clock()
        self.map=Map(map_image)
        self.running = True
        self.enemies = []
        self.towers = []
        self.spawn_timer = 0
        self.game_timer = 0
        self.lives = Lives(screen)
        self.start_screen = StartScreen(screen)
        self.game_over_screen = GameOverScreen(screen)

    def run(self):
        while self.running:
            self.handle_events()
            if not self.start_screen.active:
                if self.lives.lives > 0:
                    self.update()
                    self.render()
                else:
                    self.game_over_screen.draw()
            else:
                self.start_screen.draw()
            self.clock.tick(60)

    def spawn_enemy(self):
        self.enemies.append(Enemy(self.map.waypoints))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif not self.start_screen.active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.place_tower(x, y)
            else:
                self.start_screen.handle_event(event)
    def place_tower(self, x, y):
        for tower_waypoint in self.map.tower_waypoints:
            if abs(tower_waypoint[0] - x) < 20 and abs(tower_waypoint[1] - y) < 20:
                self.towers.append(Tower(tower_waypoint))
                break

    def generate_enemies(self):
        self.spawn_timer += self.clock.get_time()
        if self.spawn_timer >= 1000:
            self.spawn_timer = 0

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
        self.game_timer += self.clock.get_time() / 1000
        self.generate_enemies()

        for enemy in self.enemies:
            enemy.update()
            if not enemy.alive:
                self.lives.decrease_life()
                self.enemies.remove(enemy)

    def render(self):
        self.screen.fill((0, 0, 0))
        self.map.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        pygame.display.flip()
        for tower in self.towers:
            tower.draw(self.screen)
        # self.lives.draw()
        pygame.display.flip()