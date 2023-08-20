import pygame

class Controls():

    def __init__(self, name, x, y):
        self.key_mode = "Arrows"
        self.name = name
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"./Grafiken/{name}.png")
        self.image = pygame.transform.scale(self.image, (90, 40))
            


    def get_key_mode(self):
        return self.key_mode
    
    def set_key_mode(self, key_mode):
        self.key_mode = key_mode
    
    def change_key_mode(self):
        if self.key_mode == "Arrows":
            self.set_key_mode("Wasd")
            self.image = pygame.image.load(f"./Grafiken/{self.name}_g.png")
            self.image = pygame.transform.scale(self.image, (90, 40))
        elif self.key_mode == "Wasd":
            self.set_key_mode("Arrows")
            self.image = pygame.image.load(f"./Grafiken/{self.name}.png")
            self.image = pygame.transform.scale(self.image, (90, 40))


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


    def handle_keys(self):
        global keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.change_key_mode()
    
