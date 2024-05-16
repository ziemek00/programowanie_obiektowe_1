import pygame

class Enemy:
    def __init__(self, waypoints):
        self.waypoints = waypoints
        self.current_waypoint = 0
        self.position = list(waypoints[0])
        self.speed = 2
        self.alive = True
        self.image = pygame.image.load('Images/zygzak.png')

    def update(self):
        if self.current_waypoint < len(self.waypoints) - 1:
            next_waypoint = self.waypoints[self.current_waypoint + 1]

            direction_x = next_waypoint[0] - self.position[0]
            direction_y = next_waypoint[1] - self.position[1]

            if abs(direction_x) > 0:
                step = self.speed if direction_x > 0 else -self.speed
                self.position[0] += step
                if abs(next_waypoint[0] - self.position[0]) < self.speed:
                    self.position[0] = next_waypoint[0]
            elif abs(direction_y) > 0:
                step = self.speed if direction_y > 0 else -self.speed
                self.position[1] += step
                if abs(next_waypoint[1] - self.position[1]) < self.speed:
                    self.position[1] = next_waypoint[1]

            if self.position == list(next_waypoint):
                self.current_waypoint += 1
                if self.current_waypoint == len(self.waypoints) - 1:
                    self.alive = False

    def draw(self, screen):
            screen.blit(self.image, (int(self.position[0] - 22), int(self.position[1] - 12)))

