#!/usr/bin/env python
#   This is just a simple pong game to test using pygame

import sys
import pygame

#width = 1366
width = 640
#height = 768
height = 480
size = width, height
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball_image = pygame.image.load('ball.gif')
ball = ball_image.get_rect()
paddle_image = pygame.image.load('paddle.gif')
left = paddle_image.get_rect()
right = paddle_image.get_rect()
left.inflate(-2, -2)
right.inflate(-2, -2)
left_start = [40, height / 2 - 50]
right_start = [width - 60, height / 2 - 50]
left = left.move(left_start)
right = right.move(right_start)
left_pos = [0, 0]
right_pos = [0, 0]
ball_hit = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pygame.key.get_pressed()[pygame.K_w] and left.top > 0:
        left_pos[1] = -2
        left = left.move(left_pos)
    elif pygame.key.get_pressed()[pygame.K_s] and left.bottom < height:
        left_pos[1] = 2
        left = left.move(left_pos)
    elif pygame.key.get_pressed()[pygame.K_UP] and right.top > 0:
        right_pos[1] = -2
        right = right.move(right_pos)
    elif pygame.key.get_pressed()[pygame.K_DOWN] and right.bottom < height:
        right_pos[1] = 2
        right = right.move(right_pos)

    ball = ball.move(speed)
    if ball.left < 0 or ball.right > width:
        speed[0] = -speed[0]
    if ball.top < 0 or ball.bottom > height:
        speed[1] = -speed[1]

    if ball.colliderect(left) or ball.colliderect(right) and not ball_hit:
        speed[0] = -speed[0]
        ball_hit = not ball_hit
    elif ball_hit:
        ball_hit = not ball_hit

    screen.fill(black)
    screen.blit(ball_image, ball)
    screen.blit(paddle_image, left)
    screen.blit(paddle_image, right)
    pygame.display.flip()
