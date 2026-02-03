import pygame
import world

class Stick(world.WorldObject):
    def __init__(self):
        super().__init__("Stick", "A wooden stick.")

    def draw(self, screen, screen_x, screen_y):
        pygame.draw.rect(screen, (139, 69, 19), (screen_x, screen_y, 5, 20))