import pygame
import random
from scoreboard import Scoreboard

class Ghost():
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.image = pygame.image.load(f"./Grafiken/GH_{color}.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.direction = "right"
        self.speed = 0.35
        self.weak = False
        self.timer = 0


    def change_speed(self):
        scoreboard = Scoreboard()
        score = scoreboard.get_score()
        if score >= 10:
            self.speed = 0.4
        if score >= 20:
            self.speed = 0.45
        if score >= 30:
            self.speed = 0.5
        if score >= 40:
            self.speed = 0.55
        if score >= 50:
            self.speed = 0.6
        if score >= 60:
            self.speed = 0.65
        
        

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def update(self):
        if self.direction == "right":
            self.move(self.speed, 0)
            if self.x > 750:
                self.direction = "left"
                self.x = 750
        elif self.direction == "left":
            self.move(-self.speed, 0)
            if self.x < 0:
                self.direction = "right"
                self.x = 0
        elif self.direction == "up":
            self.move(0, -self.speed)
            if self.y < 50:
                self.direction = "down"
                self.y = 50
        elif self.direction == "down":
            self.move(0, self.speed)
            if self.y > 600:
                self.direction = "up"
                self.y = 600
        if self.timer > 0:
            self.timer += 1
        if self.timer == 5000:
            self.timer = 0
            self.normal_ghost()


    def update_direction(self):
        directions = ["up", "down", "left", "right"]
        self.direction = random.choice(directions)

    def change_direction(self):
        if self.direction == "right":
            self.direction = "left"
            self.x -= 10
        elif self.direction == "left":
            self.direction = "right"
            self.x += 10
        elif self.direction == "up":
            self.direction = "down"
            self.y += 10
        elif self.direction == "down":
            self.direction = "up"
            self.y -= 10

    def keys(self, controls):
        global keys
        keys = pygame.key.get_pressed()
        controlkeys = controls.get_key_mode()
        if controlkeys == "Arrows":
            if keys[pygame.K_RIGHT]:
                self.update_direction()
            elif keys[pygame.K_LEFT]:
                self.update_direction()
            elif keys[pygame.K_UP]:
                self.update_direction()  
            elif keys[pygame.K_DOWN]:
                self.update_direction()
        elif controlkeys == "Wasd":
            if keys[pygame.K_d]:
                self.update_direction()
            elif keys[pygame.K_a]:
                self.update_direction()
            elif keys[pygame.K_w]:
                self.update_direction()  
            elif keys[pygame.K_s]:
                self.update_direction()


    def weak_ghost(self):
        self.image = pygame.image.load(f"./Grafiken/GH_Blue.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.weak = True
        self.timer = 1

    def normal_ghost(self):
        self.weak = False
        self.image = pygame.image.load(f"./Grafiken/GH_{self.color}.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

    def go_back(self):
        self.x = 375
        self.y = 325
        self.direction = "right"

    
    
        
        
                

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
