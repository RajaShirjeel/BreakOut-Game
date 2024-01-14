import pygame


class Paddle():
    def __init__(self, screen):
        self.screen = screen
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.paddle_height = 67
        self.paddle_width = 10
        self.x = 370
        self.y = 500
    
    def draw_paddle(self):
        self.paddle_object = pygame.Rect(self.x, self.y,  self.paddle_height, self.paddle_width)
        pygame.draw.rect(self.screen, self.white, self.paddle_object)