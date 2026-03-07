# I acknowledge the use of ChatGPT (OpenAI) to help generate this code.



import pygame
import sys
import math

pygame.init()

# Fireball colors
fire_colors = [
    (255, 0, 0),    # red
    (255, 140, 0),  # orange
    (255, 215, 0)   # yellow
]

# Water platform color
water_color = (0, 191, 255)  # deep sky blue

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

def draw_fireball(surface, x, y, radius, spikes):
    points = []
    for i in range(spikes * 2):
        angle = i * math.pi / spikes
        r = radius if i % 2 == 0 else radius // 2
        px = x + int(math.cos(angle) * r)
        py = y + int(math.sin(angle) * r)
        points.append((px, py))
    # Draw layered fire colors from outer to inner
    pygame.draw.polygon(surface, fire_colors[0], points)  # outer red
    inner_points = [(x + int((px - x) * 0.7), y + int((py - y) * 0.7)) for px, py in points]
    pygame.draw.polygon(surface, fire_colors[1], inner_points)  # middle orange
    inner_points2 = [(x + int((px - x) * 0.4), y + int((py - y) * 0.4)) for px, py in points]
    pygame.draw.polygon(surface, fire_colors[2], inner_points2)  # inner yellow

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

    screen.fill((160, 82, 45))  # brown background)

    for y in range(0, HEIGHT, 40):
      pygame.draw.rect(screen, (139, 69, 19), (0, y, WIDTH, 40))
      pygame.draw.line(screen, (110, 50, 15), (0, y), (WIDTH, y), 2)



    draw_fireball(screen,ball_x,ball_y,10,8)
    pygame.draw.rect(screen, water_color, (paddle_x, paddle_y, paddle_width, paddle_height))

    pygame.display.update()

    clock.tick(60)