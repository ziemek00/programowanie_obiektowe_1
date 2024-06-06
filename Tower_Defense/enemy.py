import pygame

class Enemy:
    def __init__(self, waypoints, enemy_type='normal'):
        """Inicjalizuje obiekt wroga z wyznaczonymi punktami trasy i typem wroga."""
        self.waypoints = waypoints
        self.current_wp = 0
        self.position = [float(waypoints[0][0]), float(waypoints[0][1])]
        self.alive = True
        self.enemy_type = enemy_type
        self.set_attributes(enemy_type)
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image_rect = self.image.get_rect(center=(int(self.position[0]), int(self.position[1])))

    def set_attributes(self, enemy_type):
        """Ustawia atrybuty wroga w zależności od jego typu."""
        if enemy_type == 'normal':
            self.health = 100
            self.max_health = 100
            self.speed = 2.0
            self.image_path = 'images/enemy.png'
        elif enemy_type == 'fast':
            self.health = 60
            self.max_health = 60
            self.speed = 3.2
            self.image_path = 'images/fast_enemy.png'
        elif enemy_type == 'strong':
            self.health = 300
            self.max_health = 300
            self.speed = 1.0
            self.image_path = 'images/strong_enemy.png'

    def get_type(self):
        """Zwraca typ wroga."""
        return self.enemy_type

    def update(self):
        """Wyznacza trasę wroga."""
        if self.current_wp < len(self.waypoints) - 1:
            target = self.waypoints[self.current_wp + 1]

            delta_x = target[0] - self.position[0]
            delta_y = target[1] - self.position[1]

            if abs(delta_x) > 0:
                step = self.speed if delta_x > 0 else -self.speed
                self.position[0] += step
                if abs(target[0] - self.position[0]) < self.speed:
                    self.position[0] = float(target[0])
            elif abs(delta_y) > 0:
                step = self.speed if delta_y > 0 else -self.speed
                self.position[1] += step
                if abs(target[1] - self.position[1]) < self.speed:
                    self.position[1] = float(target[1])

            if self.position == [float(target[0]), float(target[1])]:
                self.current_wp += 1
                if self.current_wp == len(self.waypoints) - 1:
                    self.alive = False

            self.image_rect.center = (int(self.position[0]), int(self.position[1]))

    def draw(self, screen):
        """Rysuje wroga na ekranie."""
        screen.blit(self.image, self.image_rect.topleft)
        self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        """Rysuje pasek zdrowia wroga nad jego pozycją."""
        bar_width = 40
        bar_height = 5
        bar_x = self.position[0] - bar_width // 2
        bar_y = self.position[1] - 30
        health_percentage = self.health / self.max_health
        current_bar_width = bar_width * health_percentage

        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, current_bar_width, bar_height))

    def take_damage(self, damage):
        """Odpowiada za odejmowanie zdrowia po otrzymaniu obrażeń."""
        self.health -= damage
        if self.health <= 0:
            self.alive = False
