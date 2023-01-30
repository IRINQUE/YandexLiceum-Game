import pygame
import sys
import os
from Zmeyka import *
from STYLE import *
import runpy

pygame.init()


# Загрузка изображения
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def killprocess():
    pygame.quit()
    sys.exit


def StartScreenRQ():
    try:
        ScreenSize = (800, 600)
        Screen = pygame.display.set_mode(ScreenSize)  # Размер окна
        pygame.display.set_caption("IRINQUE - Launcher")  # Название
        # Logo = pygame.image.load("Logo.jpg")  # Загрузка фото
        # pygame.display.set_icon(Logo)  # Иконка
        Screen.fill((0, 0, 0))
        width, height = ScreenSize

        bg = pygame.transform.scale(load_image('background.jpg'), ScreenSize)
        Screen.blit(bg, (0, 0))

        FonT = pygame.font.SysFont("bahnschrift", 60)
        TexT = FonT.render("Выберите Игру!", True, TITLE)

        TextX = width // 2 - TexT.get_width() // 2
        TextY = height // 3 - TexT.get_height() // 2

        Screen.blit(TexT, (TextX, TextY))

        ButtonX1 = width // 2
        ButtonY1 = height // 2

        pygame.draw.rect(Screen, BUTTON, (ButtonX1 - 100, ButtonY1 - 25,
                          200, 50), 0)

        FonT = pygame.font.SysFont("bahnschrift", 40)
        TexT = FonT.render("Змейка", True, PLAY)

        ButtonX1Text = width // 2 - TexT.get_width() // 2
        ButtonY1Text = height // 2 - TexT.get_height() // 2

        Screen.blit(TexT, (ButtonX1Text, ButtonY1Text))

        ButtonX2 = width // 2
        ButtonY2 = height // 2 + 80

        pygame.draw.rect(Screen, BUTTON, (ButtonX2 - 100, ButtonY2 - 25, 200, 50), 0)

        FonT = pygame.font.SysFont("bahnschrift", 20)
        TexT = FonT.render("Space Defender", True, PLAY2)

        ButtonXText2 = width // 2 - TexT.get_width() // 2
        ButtonYText2 = height // 2 + 80 - TexT.get_height() // 2

        Screen.blit(TexT, (ButtonXText2, ButtonYText2))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    killprocess()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    x, y = position
                    if ButtonX1 - 100 < x < ButtonX1 + 100 and ButtonY1 - 25 < y < ButtonY1 + 25:
                        RQ = GameZmeyka()
                        if RQ:
                            main()
                    elif ButtonX2 - 100 < x < ButtonX2 + 100 and ButtonY2 - 25 < y < ButtonY2 + 25:
                        runpy.run_path('SpaceDefender.py')
                        main()
            pygame.display.flip()
    except Exception as e:
        pass


def main():
    StartScreenRQ()
    pygame.quit()


if __name__ == '__main__':
    main()
