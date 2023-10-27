import pygame

from configs import *

pygame.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.RESIZABLE)
pygame.display.set_caption('Игрушка')
clock = pygame.time.Clock()

scene = 'start'


class Button:
    def __init__(self, screen, color, text, text_color, font_name='candara', font_size=40, image_file_name='',
                 border_radius=0):
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
        self.border_radius = border_radius
        if text:
            self.w += self.button_text.get_width()
            self.h += self.button_text.get_height()
        if self.icon:
            self.w += self.icon.get_width()
            self.h += self.icon.get_height()
        self.color = color

    def draw(self):
        r = pygame.Rect((self.x, self.y, self.w, self.h))
        pygame.draw.rect(screen, self.color, r, width=0, border_radius=self.border_radius)
        screen.blit(self.button_text, (self.x + self.spacing, self.y + self.spacing), )
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


class Text:

    def __init__(self, text, text_color, font_name='arial', font_size=40):

        self.text_color = text_color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.text = text
        self.text_write = self.font.render(self.text, True, self.text_color)
        self.x = 0
        self.y = 0

    def write(self):

        screen.blit(self.text_write, (self.x, self.y))

    def move(self, x, y):
        self.x = x
        self.y = y

    def get_width(self):
        return self.text_write.get_width()

    def get_height(self):
        return self.text_write.get_height()


    def get_value(self):
        return self.text


    def add(self):

        self.text = str(int(self.text) + 1)
        self.text_write = self.font.render(self.text, True, self.text_color)


start_button_play = Button(screen, (255, 125, 255), "Играть", (0, 130, 60), font_name='arial', border_radius=15)

start_button_exit = Button(screen, (255, 0, 125), "Выход", (0, 125, 0), font_size=20, border_radius=15)

config_button_back = Button(screen, (255, 255, 0), "", (0, 125, 0), font_size=20, image_file_name='button_back.png',
                            border_radius=10)

bot_plus = Button(screen, (255, 255, 0), "", (0, 125, 0), font_size=20, image_file_name='plus.png',
                  border_radius=10)

config_button_back.move(20, 20)

text_bot = Text("5", (255, 0, 255), font_size=40)


# 441 280


def screen_draw():
    screen.fill((0, 0, 255))
    if scene == 'start':
        start_button_play.draw()
        start_button_play.move(screen.get_width() // 2 - start_button_play.get_width() // 2,
                               screen.get_height() // 2 - start_button_play.get_height() // 2)
        start_button_exit.draw()
        start_button_exit.move(screen.get_width() // 2 - start_button_exit.get_width() // 2,
                               screen.get_height() // 2 - start_button_exit.get_height() // 2 + 100)
    if scene == 'configure_game':
        bot_plus.draw()
        config_button_back.draw()
        bot_plus.move(screen.get_width() // 2 + 50, screen.get_height() // 2 - 20)
        text_bot.write()
        text_bot.move(screen.get_width() // 2 - text_bot.get_width() // 2,
                      screen.get_height() // 2 - text_bot.get_height() // 2)

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
                if bot_plus.is_pressed(mpos) and int(text_bot.get_value()) < 15:
                    text_bot.add()

    screen_draw()
    clock.tick(FPS)
