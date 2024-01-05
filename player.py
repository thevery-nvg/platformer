from game_variables import *
from world import world


class Player:
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
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.counter += 1
            dx -= 5
            self.direction = -1
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.counter += 1
            dx += 5
            self.direction = 1
        if key[pygame.K_SPACE]:
            if not self.jumped:
                self.vel_y = -15
                self.jumped = True
            else:
                self.jumped = False
        if not (key[pygame.K_LEFT] or key[pygame.K_RIGHT] or key[pygame.K_a] or key[pygame.K_d]):
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

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
        self.vel_y += 2
        if self.vel_y > 15:
            self.vel_y = 15
        dy += self.vel_y

        # check for collision
        for tile in world.tile_list:
            # check for collision for x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # check for collision for y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        # check if player is off the screen
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0

        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
