#!/usr/bin/env python
#   This is just a simple pong game to test using pygame

import sys
import pygame

width = 640
height = 480
size = width, height
speed = [1, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load('ball.gif')
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
