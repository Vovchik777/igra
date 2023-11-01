import random

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

    def get_icon_name(self):
        return self.icon


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

    def minus(self):
        self.text = str(int(self.text) - 1)
        self.text_write = self.font.render(self.text, True, self.text_color)


class Player:
    def __init__(self, x, y, w, h, speed, team_color,border_radius = 3):
        self.border_radius = border_radius
        self.h = h
        self.w = w
        self.team_color = team_color
        self.speed = speed
        self.y = y
        self.x = x
    def draw(self):
        r = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, self.team_color, r,border_radius=self.border_radius)

    def move_x(self):
        if self.get_speed() < 0:
            if self.x > 0:
                self.x += self.speed
        else:
            if self.x+self.w < ScreenWidth:
                self.x += self.speed


    def check_wall(self):
        if self.x <= 0 or self.x + self.w >=ScreenWidth:
            self.speed*=-1



    def reverse_speed(self):
        self.speed*=-1


    def get_speed(self):
        return self.speed


start_button_play = Button(screen, (255, 125, 255), "Играть", (0, 130, 60), font_name='arial', border_radius=15)

start_button_exit = Button(screen, (255, 0, 125), "Выход", (0, 125, 0), font_size=20, border_radius=15)

config_button_back = Button(screen, (255, 255, 0), "", (0, 125, 0), font_size=20, image_file_name='button_back.png',
                            border_radius=10)

bot_plus = Button(screen, (0, 255, 0), "", (0, 125, 0), font_size=20, image_file_name='plus.png',
                  border_radius=10)
bot_minus = Button(screen, (255, 0, 0), "", (0, 125, 0), font_size=20, image_file_name='minus.png',
                   border_radius=10)

config_button_back.move(20, 20)

text_bot = Text("5", (255, 0, 255), font_size=40)

button_start_game = Button(screen, (255, 125, 255), "Играть", (0, 130, 60), font_name='arial', border_radius=5)

menu_cofigure_bot = Text('Количество ботов', (255, 123, 0))

text_max = Text('Максимальное количество ботов!', (0, 255, 0), font_size=30)
max = False
text_min = Text('Минимальное количество ботов!', (0, 255, 0), font_size=30)
min = False

bots = []


# 441 280


def screen_draw():
    screen.fill((0, 0, 0))
    if scene == 'start':
        screen.fill((0, 0, 255))
        start_button_play.draw()
        start_button_play.move(screen.get_width() // 2 - start_button_play.get_width() // 2,
                               screen.get_height() // 2 - start_button_play.get_height() // 2)
        start_button_exit.draw()
        start_button_exit.move(screen.get_width() // 2 - start_button_exit.get_width() // 2,
                               screen.get_height() // 2 - start_button_exit.get_height() // 2 + 100)

    if scene == 'configure_game':
        screen.fill((123, 87, 0))
        bot_plus.draw()
        bot_minus.draw()
        menu_cofigure_bot.write()
        menu_cofigure_bot.move(screen.get_width() // 2 - menu_cofigure_bot.get_width() // 2,
                               screen.get_height() // 3 - menu_cofigure_bot.get_height() - 100)
        config_button_back.draw()
        bot_plus.move(screen.get_width() // 2 + 50, screen.get_height() // 2 - 20)
        bot_minus.move(screen.get_width() // 2 - 100, screen.get_height() // 2 - 20)
        text_bot.write()
        text_bot.move(screen.get_width() // 2 - text_bot.get_width() // 2,
                      screen.get_height() // 2 - text_bot.get_height() // 2)
        button_start_game.draw()
        button_start_game.move(screen.get_width() // 2 - button_start_game.get_width() // 2,
                               screen.get_height() // 2 + button_start_game.get_height())
        if max:
            text_max.move(screen.get_width() // 2 - text_max.get_width() // 2, screen.get_height() // 4)
            text_max.write()

        if min:
            text_min.move(screen.get_width() // 2 - text_max.get_width() // 2, screen.get_height() // 4)
            text_min.write()
    if scene == 'game':
        bg = pygame.image.load('bg.jpg')
        screen.blit(bg, (0, 0))

        for i in bots:
            i.move_x()
            i.check_wall()

        for i in bots:
            i.draw()
        player.draw()


    pygame.display.flip()

player = Player(ScreenWidth//2,ScreenHeight//2+ScreenHeight//4,50,50,5,(255,0,0),7)

def speed_ball():
    pass


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
                if bot_plus.is_pressed(mpos):
                    if int(text_bot.get_value()) < 15:
                        text_bot.add()
                        min = False

                    else:
                        max = True
                if bot_minus.is_pressed(mpos):
                    if int(text_bot.get_value()) > 5:
                        text_bot.minus()
                        max = False
                    else:
                        min = True
                if button_start_game.is_pressed(mpos):
                    scene = 'game'

                    for i in range(int(text_bot.get_value())):
                        bots.append(
                            Player(random.randrange(100, ScreenWidth - 25),
                                   random.randrange(50, ScreenHeight // 2 - 50), 25, 25,
                                   random.choice((3, -3,2,-2)),
                                   (0, 0, 255)))

    if scene == 'game':
        if pygame.key.get_pressed()[pygame.K_a]:
            if player.get_speed() == -5:
                player.move_x()
            else:
                player.reverse_speed()
                player.move_x()
        elif pygame.key.get_pressed()[pygame.K_d]:
            if player.get_speed() == 5:
                player.move_x()
            else:
                player.reverse_speed()
                player.move_x()

    screen_draw()
    clock.tick(FPS)
