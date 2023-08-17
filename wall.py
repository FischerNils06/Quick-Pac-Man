import pygame
import random


class Wall():
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0,0,255)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


    