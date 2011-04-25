#!/usr/bin/env python
#   This is just a simple pong game to test using pygame

import sys
import pygame

class Game(object):
    """The main class for the game"""
    
    def __init__(self, left_paddle, right_paddle, ball):
        self.left = left_paddle
        self.right = right_paddle
        self.ball = ball
        self.width = 640
        self.height = 480
        self.size = self.width, self.height
        self.speed = [1, 1]
        self.black = 0, 0, 0

    def make_screen(self, size):
        self.screen = pygame.display.set_mode(size)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.move_ball = self.ball.move(self.speed)
            self.screen.fill(self.black)
#            self.screen.blit(self.ball.image(), self.move_ball)
            pygame.display.flip()

class Paddle(object):
    """Class for the paddles"""
    
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.paddle = self.image.get_rect()

    def image(self):
        return self.image

    def paddle(self):
        return self.paddle
    

class Ball(object):
    """Class for the ball"""

    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.ball = self.image.get_rect()

    def image(self):
        return self.image

    def ball(self):
        return self.ball

    def move(self, speed):
        return self.ball.move(speed)

if __name__=='__main__':
    pygame.init()
    ball = Ball('ball.gif')
    left = Paddle('paddle.gif')
    right = Paddle('paddle.gif')
    game = Game(left, right, ball)
    game.make_screen(game.size)
    game.play()
