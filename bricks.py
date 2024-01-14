import pygame
from pygame.locals import *

class Bricks:
    def __init__(self, window, width, height, x, y):
        self.counter = 0
        self.window = window
        self.color = (255, 0, 0)
        self.colors_per_row = [
            [(255, 0, 0), (0, 0, 139), (255, 255, 0), (205, 127, 50), (255, 192, 203)],
            [(144, 238, 144), (152, 251, 152), (173, 216, 230), (144, 238, 144), (0, 128, 0)]
            # Add more rows with different colors as needed
        ]
        self.brick_object = pygame.Rect(x, y, width, height)
        self.is_visible = True

    def create_bricks(self, row_index, col_index):
        if self.is_visible:
            row_colors = self.colors_per_row[row_index % len(self.colors_per_row)]
            color = row_colors[col_index % len(row_colors)]
            pygame.draw.rect(self.window, color, self.brick_object)

    def hit_by_ball(self):
        self.is_visible = False
                

