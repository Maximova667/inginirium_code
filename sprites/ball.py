import math
import random

import pygame

class Ball (pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((20, 20))
        pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 370, 500
        self.dir = [0, 1]


    def update(self):
        if self.rect.x + 20 >= 740 or self.rect.x <= 0:
            self.dir[0] *= -1
            self.dir[1] += (random.random() * 2 - 1) * 0.1
        if self.rect.y <= 0:
            self.dir[1] *= -1
            self.dir[0] += (random.random() * 2 - 1) * 0.1
        self.rect = self.rect.move(10 * self.dir[0], 10 * self.dir[1])

    def collisions(self, plain_center):
        if abs(self.rect.centerx - plain_center[0]) >= 85:
            self.dir[0] *= -1
        self.dir[0] = (self.rect.center[0] - plain_center[0]) / 75
        self.dir[1] = -1 * math.sqrt(1 - math.pow(self.dir[0], 2))

    def block_collisions(self, center):
        if abs(self.rect.centerx - center[0]) <= 20:
            self.dir[1] *= -1

        if abs(self.rect.centery - center[1]) <= 20:
            self.dir[0] *= -1

