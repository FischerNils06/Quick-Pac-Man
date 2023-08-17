import pygame
import time

class  Pacman():
   

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.25
        self.image = pygame.image.load("./Grafiken/PCM_Close.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.direction = "Close"
        self.last_costume_change = 0
        self.costume_change_delay = 0.1
        self.is_open = False


    def move(self, x, y):
            self.x += x
            self.y += y
           


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

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

    def update_costume(self):
        current_time = time.time()
        if  current_time - self.last_costume_change >= self.costume_change_delay:
            self.is_open = not self.is_open
            self.last_costume_change = current_time
            if self.is_open:
                self.image = pygame.image.load(f"./Grafiken/PCM_{self.direction}.png")
            else:
                self.image = pygame.image.load("./Grafiken/PCM_Close.png")
            self.image = pygame.transform.scale(self.image, (50, 50))

        
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




    def keys(self):
        global keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction = "right"
        elif keys[pygame.K_LEFT]:
            self.direction = "left"
        elif keys[pygame.K_UP]:
            self.direction = "up"     
        elif keys[pygame.K_DOWN]:
            self.direction = "down"
            
       
            
       
            