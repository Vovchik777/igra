import pygame
from configs import *

pygame.init()
screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption('Игрушка')
clock = pygame.time.Clock()
font = pygame.font.SysFont('couriernew', 40)
text = font.render(str('Папа, тебе пора спать!'), True, (255,255,0))
textHeight = text.get_height()
textWidth = text.get_width()
def screen_draw():
    screen.fill((0,0,20))
    screen.blit(text, (ScreenWidth//2-textWidth//2,ScreenHeight//2-textHeight//2))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(1)
    screen_draw()
    clock.tick(FPS)