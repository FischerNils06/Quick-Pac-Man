import pygame

class Scoreboard():

    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.text = self.font.render(f"Score: {self.score}", True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (400, 25)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def update(self):
        self.text = self.font.render(f"Score: {self.score}", True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (400, 25)

    def get_score(self):
        return self.score
    

    def add_score(self, score):
        self.score += score
        self.update()