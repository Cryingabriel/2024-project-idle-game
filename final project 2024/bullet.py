import random
import pygame
from pygame.math import Vector2
from Player import screen
from Enemy import BaseEnemy

class Bullet:
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
        self.alive = True
        self.vx = 10

    def draw(self):
        if self.alive == True:
            pygame.draw.circle(screen,(255,0,0), (self.pos.x, self.pos.y), 5)

    def move(self,r):
        if r == 0:
            self.pos.x += self.vx
        else:
            self.pos.x -= self.vx

    def kill(self, pos):
        if self.pos.x >= 1200:
            self.alive = False
        elif self.pos.x <= 0:
            self.alive = False

        if self.alive == False:
            self.pos = pos
            self.alive = True
