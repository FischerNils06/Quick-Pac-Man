import pygame
import random
from scoreboard import Scoreboard

class Bonusdot():
    
    def __init__(self):
        xvar = random.randint(0, 785)
        yvar = random.randint(50, 635)
        self.x = xvar
        self.y = yvar
        self.image = pygame.image.load("./Grafiken/Dot2.png")
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.dot = "Black"

    def change_costume(self):
        if self.dot == "White":
            self.image = pygame.image.load("./Grafiken/Dot2.png")
            self.image = pygame.transform.scale(self.image, (15, 15))
            self.dot = "Black"
        elif self.dot == "Black":
            self.image = pygame.image.load("./Grafiken/Dot.png")
            self.image = pygame.transform.scale(self.image, (15, 15))
            self.dot = "White"
        




    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))