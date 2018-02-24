# For more details visit http://copitosystem.com

import sys
import time
import pygame
from pygame.locals import *

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()


class Player():
    """docstring for Player"""
    def __init__(self,x,y,w,h):
        self.position = [x,y,w,h]
        self.dx = 0
        self.speed = 5

    def move(self):
        if self.dx != 0 and self.position[0]+self.dx > 0 and self.position[0]+self.position[2]+self.dx < DISPLAY_WIDTH:
            self.position[0] += self.dx * self.speed

    def draw(self):
        pygame.draw.rect(gameDisplay, WHITE, self.position, 0)

    def update(self):
        self.move()
        self.draw()


class Ball():
    """docstring for Ball"""
    def __init__(self):
        self.radius = 10
        self.position = [700,100]
        self.dir = [-1,1]
        self.speed = 4
        self.alive = True

    def move(self):
        self.position[0] += self.dir[0] * self.speed
        self.position[1] += self.dir[1] * self.speed

    def draw(self):
        pygame.draw.circle(gameDisplay, WHITE, self.position, self.radius, 0)

    def check_collision(self,obj_pos):
        if (obj_pos[0] < self.position[0] < obj_pos[0]+obj_pos[2]) and (obj_pos[1] < self.position[1] < obj_pos[1]+obj_pos[3]) :
            self.dir = [self.dir[0],self.dir[1]*-1]
        if self.position[0] < 0:
            self.dir[0] = 1
        if self.position[0] > DISPLAY_WIDTH:
            self.dir[0] = -1
        if self.position[1] < 0:
            self.dir[1] = 1
        if self.position[1] > DISPLAY_HEIGHT:
            #self.dir[1] = -1
            self.alive = False

    def update(self):
        self.move()
        self.draw()


player1 = Player(400,500,100,20)
ball1 = Ball()

while True:
    for event in pygame.event.get():
        #windows cross button
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                player1.dx = -1
            if event.key == pygame.K_RIGHT:
                player1.dx = 1
        if event.type == KEYUP:
            if event.key == pygame.K_LEFT:
                player1.dx = 0
            if event.key == pygame.K_RIGHT:
                player1.dx = 0     
        #print(event)
    gameDisplay.fill(BLACK)
    player1.update()    
    ball1.check_collision(player1.position)
    ball1.update()
    if ball1.alive == False:
        #GAME OVER
        time.sleep(3)
        player1 = Player(400,500,100,20)
        ball1 = Ball()

    pygame.display.update()
    clock.tick(60)


