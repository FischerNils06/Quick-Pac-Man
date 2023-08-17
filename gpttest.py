import pygame
import time

class Pacman:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 1
        self.image = pygame.image.load("./Grafiken/PCM_Close.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.direction = "right"
        self.last_move_time = 0
        self.last_costume_change = 0
        self.costume_change_delay = 0.05  # Delay between costume changes in seconds
        self.is_open = False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        current_time = time.time()
        if current_time - self.last_move_time >= self.move_delay:
            if self.direction == "right":
                self.move(self.speed, 0)
                if self.x > 750:
                    self.x = 750
            elif self.direction == "left":
                self.move(-self.speed, 0)
                if self.x < 0:
                    self.x = 0
            elif self.direction == "up":
                self.move(0, -self.speed)
                if self.y < 0:
                    self.y = 0
            elif self.direction == "down":
                self.move(0, self.speed)
                if self.y > 550:
                    self.y = 550
            self.last_move_time = current_time

        if current_time - self.last_costume_change >= self.costume_change_delay:
            self.is_open = not self.is_open
            self.last_costume_change = current_time
            if self.is_open:
                self.image = pygame.image.load(f"./Grafiken/PCM_{self.direction}.png")
            else:
                self.image = pygame.image.load("./Grafiken/PCM_Close.png")
            self.image = pygame.transform.scale(self.image, (50, 50))

    def keys(self):
        global keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = "up"
        elif keys[pygame.K_DOWN]:
            self.direction = "down"
        elif keys[pygame.K_LEFT]:
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            self.direction = "right"

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pacman Changing Costumes")

# Create a Pacman instance
pacman = Pacman()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle character movement based on keys
    pacman.keys()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update Pacman position and costume
    pacman.update()

    # Draw Pacman on the screen
    pacman.draw(screen)

    # Update the display
    pygame.display.update()

pygame.quit()

