import pygame
import world

class Player(world.WorldObject):
    MOVEMENT_SPEED = 1
    def __init__(self):
        super().__init__("Player", "The user-controlled player character.")
        self.color = (0, 0, 255)
        self.size = 10
        self.movement = {'left': False, 'right': False, 'up': False, 'down': False}
        self.run_multiplier = 1

    def draw(self, screen, screen_x, screen_y):
        pygame.draw.circle(screen, self.color, (screen_x, screen_y), self.size)
    
    def movement_update(self):
        if self.movement['left']:
            self.x -= self.MOVEMENT_SPEED * self.run_multiplier
        if self.movement['right']:
            self.x += self.MOVEMENT_SPEED * self.run_multiplier
        if self.movement['up']:
            self.y += self.MOVEMENT_SPEED * self.run_multiplier
        if self.movement['down']:
            self.y -= self.MOVEMENT_SPEED * self.run_multiplier
    
    def toggle_run(self):
        self.run_multiplier = 1 if self.run_multiplier == 2.5 else 2.5

    def toggle_move_left(self):
        self.movement['left'] = not self.movement['left']

    def toggle_move_right(self):
        self.movement['right'] = not self.movement['right']

    def toggle_move_up(self):
        self.movement['up'] = not self.movement['up']

    def toggle_move_down(self):
        self.movement['down'] = not self.movement['down']