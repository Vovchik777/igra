import pygame

from configs import *

pygame.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.RESIZABLE)
pygame.display.set_caption('Игрушка')
clock = pygame.time.Clock()

scene = 'start'


class Button:
    def __init__(self, screen, color, text, text_color, font_name='candara', font_size=40, image_file_name=''):
        font = pygame.font.SysFont(font_name, font_size)
        self.icon = None
        if image_file_name:
            self.icon = pygame.image.load(image_file_name)
        self.button_text = font.render(text, True, text_color)
        self.screen = screen
        self.x = 0
        self.y = 0
        self.spacing = 10
        self.w = self.spacing * 2
        self.h = self.spacing * 2
        if text:
            self.w += self.button_text.get_width()
            self.h += self.button_text.get_height()
        if self.icon:
            self.w += self.icon.get_width()
            self.h += self.icon.get_height()
        self.color = color

    def draw(self):
        r = pygame.Rect((self.x, self.y, self.w, self.h))
        pygame.draw.rect(screen, self.color, r, width=0)
        screen.blit(self.button_text, (self.x + self.spacing, self.y + self.spacing))
        if self.icon:
            screen.blit(self.icon, (self.x + self.spacing, self.y + self.spacing))

    def get_width(self):
        return self.w

    def get_height(self):
        return self.h

    def move(self, x, y):
        self.x = x
        self.y = y

    def is_pressed(self, mousepos):
        return self.x < mousepos[0] < self.x + self.w and self.y < mousepos[1] < self.y + self.h


start_button_play = Button(screen, (0, 255, 255), "Играть", (125, 125, 0))
start_button_play.move(screen.get_width() // 2 - start_button_play.get_width() // 2,
                       screen.get_height() // 2 - start_button_play.get_height() // 2)
start_button_exit = Button(screen, (255, 0, 125), "Выход", (0, 125, 0), font_size=20)
start_button_exit.move(screen.get_width() // 2 - start_button_exit.get_width() // 2,
                       screen.get_height() // 2 - start_button_exit.get_height() // 2 + 100)
config_button_back = Button(screen, (255, 255, 0), "", (0, 125, 0), font_size=20, image_file_name='button_back.png')
config_button_back.move(20, 20)


# 441 280


def screen_draw():
    screen.fill((0, 0, 20))
    if scene == 'start':
        start_button_play.draw()
        start_button_exit.draw()
    if scene == 'configure_game':
        config_button_back.draw()
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if scene == 'start':
                if start_button_exit.is_pressed(mpos):
                    exit(1)
                if start_button_play.is_pressed(mpos):
                    scene = 'configure_game'
            if scene == 'configure_game':
                if config_button_back.is_pressed(mpos):
                    scene = 'start'

    screen_draw()
    clock.tick(FPS)
