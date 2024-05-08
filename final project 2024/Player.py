import pygame
from pygame.math import Vector2
SCREEN_SIZE = Vector2(1200, 800)

# pygame init:
screen = pygame.display.set_mode(SCREEN_SIZE)


class Players():
    def __init__(self,xpos,ypos):
        self.pos = Vector2(xpos,ypos)
        self.health = 100
        self.attack = .1
        self.vx = 10
        self.bpos = Vector2(xpos,ypos)
    def draw(self):
        pygame.draw.circle(screen,(255,255,255), (self.pos.x,self.pos.y),10)