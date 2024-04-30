import pygame
import Enemy
import Player
from pygame.math import Vector2
from pygame.rect import Rect


# config:
FRAMERATE = 60
SCREEN_SIZE = Vector2(1200, 800)


# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("")


# definitions:



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

        pygame.display.flip()

if __name__ == "__main__":
    main()