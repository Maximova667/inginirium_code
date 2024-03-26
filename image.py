import pygame


pygame.init()

FPS = 60
W, H = 800, 800
win = pygame.display.set_mode((W, H))
def load_img(name):
    img = pygame.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img
img = load_img('ing.png')
img1 = pygame.transform.scale(img, (100, 100))
img2 = pygame.transform.scale(img, (300, 300))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    win.fill('#dbf6e9')
    win.blit(img1, (0, 0))
    win.blit(img2, (100, 200))
    pygame.display.update()

