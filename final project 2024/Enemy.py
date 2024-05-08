import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from Player import screen
from Player import Players

class BaseEnemy:
    pos: Vector2
    velocity: float
    alive: bool

    def __init__(self, pos: Vector2, velocity, r):
        self.rand = r
        if self.rand == 0:
            self.pos = pos
        elif self.rand == 1:
            self.pos = Vector2(1200,350)
        self.alive = True
        self.size = Vector2(50,100)
        self.velocity = velocity
        self.score = 0
        self.respawn_timer = 0

    def update(self, delta: float, playerpos: Vector2):
        if self.respawn_timer > 0:
            self.respawn_timer -= delta
            if self.respawn_timer < 0: # reset to 0 if overshot
                self.respawn_timer = 0

        self.move()
        self.collision(playerpos)
        self.draw()

    def move(self):
        if self.rand == 0:
            self.pos.x += self.velocity
        elif self.rand == 1:
            self.pos.x -= self.velocity

    def draw(self):
        if self.alive == True:
            rect = Rect(self.pos, self.size)
            pygame.draw.rect(screen,(255,255,255), rect)

    def collision(self, playerpos: Vector2):
        if Rect(self.pos, self.size).collidepoint(playerpos):
            self.alive = False
            self.respawn_timer = 5

        if not self.alive and self.respawn_timer == 0:
            self.alive = True
            if self.rand == 0:
                self.pos.x = -50
            elif self.rand == 1: 
                self.pos.x = 1200
            self.score += 10

            self.alive = True

    def coin(self):
        return self.score