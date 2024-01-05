import pygame
from pygame.locals import *
import random
from game_variables import *
from player import Player
from world import world

pygame.init()


def create_world_data(size):
    data = [[random.randint(0, 5) for _ in range(size[0])] for _ in range(size[1])]
    return data


player = Player(100, screen_height - 130)

run = True
while run:
    clock.tick(fps)
    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))
    world.draw()
    blob_group.update()
    blob_group.draw(screen)
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
