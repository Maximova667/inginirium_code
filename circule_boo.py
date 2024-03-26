import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

xc = 40
cx = 30
color = (250, 250, 0)
speed = 3
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    if abs(250 - xc) > 150 or abs(250 - cx) > 150:
       color = (250, 250, 0)
       speed = 1
    else:
       color = (250, 0, 0)
       speed = 3
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        xc += speed
    elif key[pygame.K_UP]:
        xc -= speed
    elif key[pygame.K_RIGHT]:
        cx += speed
    elif key[pygame.K_LEFT]:
        cx -= speed
    else:
        if xc > 250:
            xc -= speed
        elif xc < 250:
            xc += speed
        elif cx > 250:
            cx -= speed
        elif cx < 250:
            cx += speed 

    win.fill((0, 0, 255))
    pygame.draw.circle(win, color, (cx, xc), 50)
    pygame.display.update()

    pygame.time.delay(10)
