import pygame
import sys
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from pygame.locals import *

pygame.init()

game_over_font = pygame.font.Font(None, 36)  # Choose a font and size
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("BreakOut Game")
clock = pygame.time.Clock()

paddle = Paddle(screen)
ball = Ball(screen, width, height)
bricks = []
bricks_width = 60
bricks_height = 20
bricks_spacing = 10
bricks_rows = 8
bricks_col = 11

# Calculate total width of all bricks and spacing
total_bricks_width = bricks_col * bricks_width + (bricks_col - 1) * bricks_spacing

# Calculate starting x-coordinate to center the bricks
start_x = (width - total_bricks_width) // 2


for i in range(bricks_rows):
    for j in range(bricks_col):
        x = start_x + j * (bricks_width + bricks_spacing)
        y = i * (bricks_height + bricks_spacing)
        bricks.append(Bricks(screen, bricks_width, bricks_height, x, y))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(paddle.black)
    
    ball.create_ball()
    paddle.draw_paddle()

    # Draw and Check Collisions with bricks
    for i, row_bricks in enumerate(bricks):
        row_bricks.create_bricks(i, 0)
        brick = row_bricks
        if brick.is_visible and ball.ball_object.colliderect(brick.brick_object):
            brick.hit_by_ball()
            ball.speed[1] *= -1


    # Update the ball Position
    ball.x += ball.speed[0]
    ball.y += ball.speed[1]


    # Bounce the ball off the walls
    if ball.ball_object.left <= 0:
        ball.speed[0] = abs(ball.speed[0])

    elif ball.ball_object.right >= width:
        ball.speed[0] = -abs(ball.speed[0])

    if ball.ball_object.top <= 0:
        ball.speed[1] = abs(ball.speed[1])
    
    # Display Game over
    elif ball.ball_object.bottom > height:
        text = game_over_font.render("Game Over!", True, (255, 255, 255))
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        running = False

    #check of there are no bricks
    if all(not brick.is_visible for brick in bricks):
        text = game_over_font.render("Congrats! ", True, (255, 255, 255))
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        running = False


    # Bounce the ball off the paddle
    if ball.ball_object.colliderect(paddle.paddle_object) and ball.speed[1] > 0:
        ball.speed[1] = -ball.speed[1]

    
    keys = pygame.key.get_pressed()
    if keys[K_a] and paddle.x > 0:
        paddle.x -= 5
    if keys[K_d] and paddle.x < width - paddle.paddle_height:
        paddle.x += 5


    pygame.display.flip()


    clock.tick(60)

pygame.quit()
sys.exit()
