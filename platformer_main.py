import pygame
from pygame.locals import *
import random

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")
# define game variables
tile_size = 100

# load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')


def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class Player():
    def __init__(self, x, y):
        img = pygame.image.load('img/guy1.png')
        self.image = pygame.transform.scale(img, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5
        if key[pygame.K_SPACE]:
            if not self.jumped:
                self.vel_y = -15
                self.jumped = True
            else:
                self.jumped = False

        # gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # check for collision


        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0
        screen.blit(self.image, self.rect)


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
