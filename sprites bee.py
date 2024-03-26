import random


import pygame


pygame.init()

FPS = 30
W, H = 500, 500
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Mine Bobrs')

class Inigirium(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('ing.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) * random.choice((1, -1)),
                                   random.randrange(3) * random.choice((1, -1)))


all_sprite = pygame.sprite.Group()
for _ in range(50):
    Inigirium(all_sprite)

clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    all_sprite.update()
    win.fill((250, )* 3)
    all_sprite.draw(win)
    pygame.display.update()
    clock.tick(FPS)
