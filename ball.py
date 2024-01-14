import pygame
from pygame.locals import *

class Ball:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        self.color = (128, 0, 128)
        self.speed = [1, 3]
        self.x = self.width // 2
        self.y = self.height // 2
    
    def create_ball(self):
        self.ball_object = pygame.Rect(self.x, self.y, 20, 20)
        pygame.draw.ellipse(self.window, self.color, self.ball_object) 
    
        