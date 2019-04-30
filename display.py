import sys
import pygame
import time


pygame.init()
size = width, height = 500,270
win = pygame.display.set_mode(size)
pygame.display.set_caption("testing")
SCORE_FONT = pygame.font.SysFont("monospace", 16)
WHITE = (255,255,255)


score = 0
while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    win.fill(WHITE)
    time.sleep(0.03)
    score_text = SCORE_FONT.render("Score {0}".format(score), 1, (0, 0, 0))
    win.blit(score_text, (370, 5))
    score += 1
