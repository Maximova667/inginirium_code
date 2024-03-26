import pygame

class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, health, color, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health

    def kill(self) -> None:
        self.health -= 1
        if self.health == 0:
            super().kill()
