import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

xc = 20
cx = 30
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    cx = cx - 1
    if cx < 0:
        cx = 500
    xc = xc + 1
    if xc > 500:
        xc = 0
    win.fill((0, 0, 255))
    pygame.draw.circle(win, (250, 0, 0), (250, cx), 50)
    pygame.draw.rect(win, (0, 250, 0), (xc, 100, 120, 110))
    pygame.display.update()

    pygame.time.delay(10)


