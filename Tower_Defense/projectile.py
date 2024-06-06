import pygame
import math

class Projectile:
    def __init__(self, position, target, damage=10, speed=5):
        self.position = list(position)
        self.target = target
        self.damage = damage
        self.speed = speed
        self.alive = True
        self.image = pygame.image.load('images/projectile.png')
        self.image = pygame.transform.scale(self.image, (10, 10))

    def update(self):
        if not self.alive:
            return

        direction = (self.target.position[0] - self.position[0], self.target.position[1] - self.position[1])
        distance = math.hypot(*direction)
        direction = (direction[0] / distance, direction[1] / distance)

        self.position[0] += direction[0] * self.speed
        self.position[1] += direction[1] * self.speed

        if math.hypot(self.target.position[0] - self.position[0], self.target.position[1] - self.position[1]) < self.speed:
            self.alive = False
            self.target.take_damage(self.damage)

    def draw(self, screen):
        screen.blit(self.image, (int(self.position[0]), int(self.position[1])))
