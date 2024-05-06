import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from main import screen

class default:
    pos: Vector2
    alive: bool
    velocity: float
    rect: Rect

    def __init__(self, pos: Vector2, alive: bool, velocity: float):
        self.pos = pos
        self.alive = True
        self.rect = Rect(self.pos, (50,100))
        self.velocity = velocity
    def move(self):
        self.pos.x += self.velocity
    def draw(self):
        if self.alive == True:
            pygame.draw.rect(screen,(255,255,255), self.rect) # if this isn't working (the player isn't moving), then create a new rect every frame instead
    def update(self, player_pos: Vector2):
        pass