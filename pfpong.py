#!/usr/bin/env python
# This is just a simple pong game to test using pygame
# TODO: Needs to be completely refactored.
# I need to comment this like crazy!

import sys
import pygame

width = 1366
#width = 640
height = 768
#height = 480
size = width, height
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

pygame.init()

screen = pygame.display.set_mode(size)
ball_image = pygame.image.load('ball.gif')
ball = ball_image.get_rect()
paddle_image = pygame.image.load('paddle.gif')
left = paddle_image.get_rect()
right = paddle_image.get_rect()
left.inflate(2, 2)
right.inflate(2, 2)
net_image = pygame.image.load('net.gif')
net = net_image.get_rect()
net_pos = [width / 2 - 5, 0]
net = net.move(net_pos)
left_start = [40, height / 2 - 50]
right_start = [width - 60, height / 2 - 50]
left = left.move(left_start)
right = right.move(right_start)
left_pos = [0, 0]
right_pos = [0, 0]
ball_hit = False
left_score = 0
right_score = 0

font = pygame.font.Font(None, 72)
left_text = font.render(str(left_score), True, white, black)
right_text = font.render(str(right_score), True, white, black)
left_text_rect = left_text.get_rect()
right_text_rect = right_text.get_rect()
left_text_rect.center = [width / 4, 56]
right_text_rect.center = [3 * width / 4, 56]

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
    if pygame.key.get_pressed()[pygame.K_UP] and right.top > 0:
        right_pos[1] = -2
        right = right.move(right_pos)
    elif pygame.key.get_pressed()[pygame.K_DOWN] and right.bottom < height:
        right_pos[1] = 2
        right = right.move(right_pos)

    ball = ball.move(speed)
    if ball.left < 0:
        right_score += 1
        right_text = font.render(str(right_score), True, white, black)
        ball.center = (width - 80, 100)
    if ball.right > width:
        left_score += 1
        left_text = font.render(str(left_score), True, white, black)
        ball.center = (80, 100)
    if ball.top < 0 or ball.bottom > height:
        speed[1] = -speed[1]

    if ball.left < left.right - 3:
        pass
    elif ball.right > right.left + 3:
        pass
    elif ball.colliderect(left) or ball.colliderect(right):
        speed[0] = -speed[0]

    screen.fill(black)
    screen.blit(left_text, left_text_rect)
    screen.blit(right_text, right_text_rect)
    screen.blit(net_image, net)
    screen.blit(ball_image, ball)
    screen.blit(paddle_image, left)
    screen.blit(paddle_image, right)
    pygame.display.flip()

