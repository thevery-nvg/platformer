import pygame
from pygame.locals import *
import random
from game_variables import *
from player import Player
pygame.init()


def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class World():
    def __init__(self, data):
        self.tile_list = []

        # load images
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


def create_world_data(size):
    data = [[random.randint(0, 5) for _ in range(size[0])] for _ in range(size[1])]
    return data


player = Player(100, screen_height - 130)
# world = World(create_world_data(size=(screen_width // tile_size, screen_height // tile_size)))
world = World([
    [1] * 10,
    [1] + [0] * 8 + [1],
    [1] + [0] * 8 + [1],
    [1] + [0] * 8 + [1],
    [1] + [0] * 8 + [1],
    [1] + [0] * 8 + [1],
    [1] + [0] * 8 + [1],
    [1] + [0] * 8 + [1],
    [1] + [0] * 8 + [1],
    [2] * 10,
])
run = True
while run:
    clock.tick(fps)
    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))
    draw_grid()
    world.draw()
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
