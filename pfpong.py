#!/usr/bin/env python
#   This is just a simple pong game to test using pygame

import sys
import pygame

width = 640
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
left_start = [40, height / 2 - 50]
right_start = [width - 60, height / 2 - 50]
left = left.move(left_start)
right = right.move(right_start)
left_pos = [0, 0]
right_pos = [0, 0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_pos[1] = -10
                left = left.move(left_pos)
            elif event.key == pygame.K_s:
                left_pos[1] = 10
                left = left.move(left_pos)
            elif event.key == pygame.K_UP:
                right_pos[1] = -10
                right = right.move(right_pos)
            elif event.key == pygame.K_DOWN:
                right_pos[1] = 10
                right = right.move(right_pos)

    ball = ball.move(speed)
    if ball.left < 0 or ball.right > width:
        speed[0] = -speed[0]
    if ball.top < 0 or ball.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball_image, ball)
    screen.blit(paddle_image, left)
    screen.blit(paddle_image, right)
    pygame.display.flip()
