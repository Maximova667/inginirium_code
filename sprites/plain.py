import pygame


class Plain(pygame.sprite.Sprite):
    def __init__(self, y, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((150, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.y = 690
        self.rect.x = 400


    def update(self):
        x, _ = pygame.mouse.get_pos()
        self.rect.x = x - 75





