import pygame

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")
tile_size = 50
blob_group = pygame.sprite.Group()

# frame rate
clock = pygame.time.Clock()
fps = 100

# load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')

