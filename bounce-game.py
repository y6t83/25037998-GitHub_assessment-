# I acknowledge the use of ChatGPT (OpenAI) to help generate this code.

# I acknowledge the use of ChatGPT (OpenAI) to help generate this code.

import pygame
import sys
import math

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nokia Bounce Style Game")

ball_x = 300
ball_y = 200
ball_speed_x = 4
ball_speed_y = 4

paddle_x = 250
paddle_y = 350
paddle_width = 100
paddle_height = 10
paddle_speed = 7

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed

    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= 0 or ball_x >= WIDTH:
        ball_speed_x *= -1

    if ball_y <= 0:
        ball_speed_y *= -1

    if ball_y >= paddle_y and paddle_x < ball_x < paddle_x + paddle_width:
        ball_speed_y *= -1

    screen.fill((0,0,0))

    



    pygame.draw.circle(screen, (192,192,192), (int(ball_x), int(ball_y)), 10)
    pygame.draw.rect(screen,(139,69,19),(paddle_x,paddle_y,paddle_width,paddle_height))

    pygame.display.update()

    clock.tick(60)