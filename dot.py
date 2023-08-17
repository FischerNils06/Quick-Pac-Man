import pygame
import random

class Dot():
    
        def __init__(self):
            xvar = random.randint(0, 775)
            yvar = random.randint(50, 625)
            self.x = xvar
            self.y = yvar
            self.image = pygame.image.load("./Grafiken/Dot.png")
            self.image = pygame.transform.scale(self.image, (25, 25))
    
        def draw(self, screen):
            screen.blit(self.image, (self.x, self.y))