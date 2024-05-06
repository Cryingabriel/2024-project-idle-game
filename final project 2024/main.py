import pygame
#import Enemy
#import Players
from Player import ammo
from pygame.math import Vector2
from pygame.rect import Rect
from Player import Players
from Player import screen
# config:
FRAMERATE = 60


# pygame init:
pygame.init()
pygame.display.set_caption("Idle Game - Tam/Cai Final Project")

# definitions:

dummy = Players(600,400)

for i in range(2):
    ammo.append(dummy.bullet())
def main():
    # game setup:
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
            ammo[i]

        pygame.display.flip()

if __name__ == "__main__":
    main()