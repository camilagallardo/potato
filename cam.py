
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Attempt Create")

screenWidth = 500
screenHeight = 500


x = 0
y = 460
width = 40
height = 40
vel = 6

isJump = False
jumpCount = 10
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if not isJump:
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= jumpCount ** 2 * 0.5
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    win.fill((255, 255, 255))
    pygame.draw.rect(win,(0, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()




