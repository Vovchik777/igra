import pygame
from win32api import GetSystemMetrics

from configs import *

pygame.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight),pygame.RESIZABLE)
pygame.display.set_caption('Игрушка')
clock = pygame.time.Clock()
font = pygame.font.SysFont('couriernew', 40)
text = font.render(str('Папа, тебе пора спать!'), True, (255, 255, 0))
textHeight = text.get_height()
textWidth = text.get_width()


def screen_draw():
    screen.fill((0, 0, 20))
    screen.blit(text, (screen.get_width() // 2 - textWidth // 2, screen.get_height() // 2 - textHeight // 2))
    pygame.display.flip()


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(1)
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h),
                                      pygame.RESIZABLE)
            # if event.key == pygame.K_F11:
            #     print("width =", GetSystemMetrics(0))
            #     print("height =", GetSystemMetrics(1))
            #     screen = pygame.display.set_mode((GetSystemMetrics(0),GetSystemMetrics(1)))
    screen_draw()
    clock.tick(FPS)
