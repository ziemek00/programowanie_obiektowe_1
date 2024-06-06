import pygame

class Map:
    """Klasa reprezentująca mapę gry."""
    def __init__(self, image_file):
        self.image = pygame.image.load(image_file)
        self.waypoints = [(5, 430), (200,430), (200, 210), (445, 210),
                     (445, 510),(760, 510), (760, 370), (1195, 370)]
        self.tower_waypoints = [(320, 280), (520, 440), (680, 440), (840, 440)]

    def draw(self, screen):
        """Rysuje obraz mapy na ekranie."""
        screen.blit(self.image, (0, 0))
        # for waypoint in self.waypoints:
        #     pygame.draw.circle(screen, (255, 0, 0), waypoint, 5)
        for tower_waypoint in self.tower_waypoints:
            pygame.draw.circle(screen, (101, 67,33), tower_waypoint, 30)