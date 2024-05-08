import pygame
#import Enemy
#import Players
import random
from pygame.math import Vector2
from pygame.rect import Rect
from Player import Players
from Player import screen
from bullet import Bullet
from Enemy import BaseEnemy
import itertools
# config:
FRAMERATE = 60

# pygame init:
pygame.init()
pygame.display.set_caption("Idle Game - Tam/Cai Final Project")


def main():
    # game setup:
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    pbpos = Vector2(600,400)
    myfunc = itertools.cycle([0,1]).__next__
    coins = 0
    ammo: list[Bullet] = []
    attack: list[BaseEnemy] = []
    dummy = Players(pbpos.x,pbpos.y)

    for i in range(2):
        ammo.append(Bullet(pbpos.x,pbpos.y))

    for i in range(2):
        attack.append(BaseEnemy(Vector2(-50,350),5,myfunc()))
        
    clock = pygame.time.Clock()

    # main loop:
    running = True
    while running:
        delta = clock.tick(FRAMERATE) / 1000

        # input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # draw:
        screen.fill("#000000")
        dummy.draw()
        for i in range(len(ammo)):
            ammo[i].draw()
            ammo[i].move(myfunc())
            ammo[i].kill(pbpos)
            
        for enemy in attack:
            enemy.update(delta, dummy.pos)
            coins += enemy.coin()
                
        text_label3 = my_font.render(str("Coins: "),1,(255, 255, 255))#Makes text show up
        text_surface = my_font.render(str(coins), 1 ,(255, 255, 255))


        screen.blit(text_surface, (90,0))
        screen.blit(text_label3, (0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()