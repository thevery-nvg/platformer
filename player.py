import pygame
from game_variables import *


class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (50, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_left.append(img_left)
            self.images_right.append(img_right)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.counter += 1
            dx -= 5
            self.direction = -1
        if key[pygame.K_RIGHT]:
            self.counter += 1
            dx += 5
            self.direction = 1
        if key[pygame.K_SPACE]:
            if not self.jumped:
                self.vel_y = -15
                self.jumped = True
            else:
                self.jumped = False
        if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
            self.counter = 0
            self.index = 0
            self.image = self.images_right[self.index]
        # animation

        if self.counter > walk_cooldown:
            self.counter = 0
            if self.index == len(self.images_right) - 1:
                self.index = 0
            else:
                self.index += 1
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

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
