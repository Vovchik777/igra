import pygame

from configs import *

pygame.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.RESIZABLE)
pygame.display.set_caption('Игрушка')
clock = pygame.time.Clock()


class Button:
    def __init__(self, screen, color, text, text_color,font_name = 'candara',font_size = 40):
        font = pygame.font.SysFont(font_name, font_size)
        self.button_text = font.render(text, True, text_color)
        self.screen = screen
        self.x = 0
        self.y = 0
        self.w = self.button_text.get_width()
        self.h = self.button_text.get_height()
        self.color = color


    def draw(self):
        r = pygame.Rect((self.x-10, self.y-10, self.w+20, self.h+20))
        pygame.draw.rect(screen, self.color, r, width=0)
        screen.blit(self.button_text, (self.x, self.y))


    def get_width(self):
        return self.w


    def get_height(self):
        return self.h


    def move(self, x, y):
        self.x = x
        self.y = y


button_play = Button(screen, (0, 255, 255), "Играть", (125, 125, 0))
button_play.move(screen.get_width() // 2 - button_play.get_width() // 2, screen.get_height() // 2 - button_play.get_height() // 2)
button_exit = Button(screen, (255, 0, 125), "Выход", (0, 125, 0),font_size=20)
button_exit.move(screen.get_width() // 2 - button_exit.get_width() // 2 , screen.get_height() // 2 - button_exit.get_height() // 2+100)
# 441 280


def screen_draw():
    screen.fill((0, 0, 20))
    button_play.draw()
    button_exit.draw()
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
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if pygame.mouse.get_pos() ==
            # if event.key == pygame.K_F11:
            #     print("width =", GetSystemMetrics(0))
            #     print("height =", GetSystemMetrics(1))
            #     screen = pygame.display.set_mode((GetSystemMetrics(0),GetSystemMetrics(1)))
    screen_draw()
    clock.tick(FPS)
