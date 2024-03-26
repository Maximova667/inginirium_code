import pygame

from sprites.block import Block
from sprites.plain import Plain
from sprites.ball import Ball

pygame.init()
win = pygame.display.set_mode((740, 800))
pygame.display.set_caption('Food')
pygame.display.set_icon(pygame.image.load('ing.png'))

all_sprites = pygame.sprite.Group()

plain = Plain(690, all_sprites)
ball = Ball(all_sprites)

score = 0
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)


blacks = pygame.sprite.Group()
for i in range(24):
    for j in range(3):
        Block(20+25*i, 200+25*j, 1, "#C2F83E", blacks, all_sprites)

    for j in range(3):
        Block(20+25*i, 100+25*j, 1, (165, 0, 165), blacks, all_sprites)


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if ball.rect.colliderect(plain.rect):
        ball.collisions(plain.rect.center)

    collisions_blocks = pygame.sprite.spritecollide(ball, blacks, True)
    if collisions_blocks is not None:
        if len(collisions_blocks) > 0:
            ball.block_collisions(collisions_blocks[0].rect.center)
            score += 1

    surf_font = my_font.render(f'SCORE: {score}', False, (255,) * 3)
    win.blit(surf_font, (20, 0))


    all_sprites.update()
    win.fill((0, ) * 3)
    all_sprites.draw(win)
    win.blit(surf_font, (20, 0))
    pygame.display.update()


    clock.tick(90)