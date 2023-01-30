import pygame
import random
import math
from pygame import mixer
import time
import runpy
from main import *

pygame.init()  # Инициализация
ScreenWidth, ScreenHeight = 800, 600  # Размер Экрана
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))  # Экран
pygame.display.set_caption("RQ - SpaceDefender")  # Название Игры

Score = 0  # Счет
ScoreCoordinateX = 5  # Где отрисовывается счет
ScoreCoordinateY = 5
font = pygame.font.SysFont("bahnschrift", 25)

White = (255, 255, 255)
Background = (0, 0, 0)  # Цвет Фона

def GameScore(x, y):
    Gamescore = font.render("Счет:" + str(Score), True, White)
    Screen.blit(Gamescore, (x, y))

def GameOver():
    Text = font.render("GAME OVER", True, White)
    Screen.blit(Text, [800 / 2 - Text.get_width() // 2,
                       600 / 2 - Text.get_height() // 2])

"""if random.randint(1, 2) == 1:
    mixer.music.load('data/Matery.waw')  # Музыка(Загрузка)
    mixer.music.play(-1)  # Музыка(Проигрывание)
else:
    mixer.music.load('data/War.waw')  # Музыка(Загрузка)
    mixer.music.play(-1)  # Музыка(Проигрывание)
"""
# Игрок
HeroImage = pygame.image.load('data/MainHero.png')  # Загрузка Корабля
HeroX = 370  # Начальная Позиция Корабля X
HeroY = 480  # Начальная Позиция Корабля Y
HeroXChanged = 0
# Атакующие
AttackerImage = list()
AttackerX = list()
AttackerY = list()
AttackerXChanged = list()
AttackerYChanged = list()
NumberOfAttackers = 5
# Количество атакующих
for AttackerN in range(NumberOfAttackers):
    AttackerImage.append(pygame.image.load('data/Attacker.png'))  # Загружаем фото врага
    AttackerX.append(random.randint(64, 737))  # Спавн по X
    AttackerY.append(random.randint(30, 180))  # Спавн по Y
    AttackerXChanged.append(1.2)  # Изменяем позицию X
    AttackerYChanged.append(50)  # Изменяем позицию Y
# Патроны
BulletImage = pygame.image.load('data/bullet.png')  # Загружаем фото пули
BulletX = 0  # Позиция отрисовки пули по X
BulletY = 500  # Позиция отрисовки пули по Y
BulletXChanged = 0  # Позиция отрисованной пули измененная по X
BulletYChanged = 3  # Позиция отрисованной пули измененная по Y
BulletStatus = "AFK"  # Начальный статус пули


def isCollision(X1, X2, Y1, Y2):
    Dis = math.sqrt((math.pow(X1 - X2, 2)) + (math.pow(Y1 - Y2, 2)))
    if Dis <= 50:
        return True
    else:
        return False

def Hero(X, Y):
    Screen.blit(HeroImage, (X - 16, Y + 10))  # Отрисовка Игрока

def Attacker(X, Y, i):
    Screen.blit(AttackerImage[i], (X, Y))  # Отрисовка атакующих

def Bullet(X, Y):
    global BulletStatus
    Screen.blit(BulletImage, (X, Y))  # Трисовка пули
    BulletStatus = "Fire"  # Статус

Game = True
while Game:
    Screen.fill(Background)  # Фон
    for event in pygame.event.get():  # Отслеживаем Ивенты
        if event.type == pygame.QUIT:
            Game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  #
                HeroXChanged = -1.7
            if event.key == pygame.K_d:
                HeroXChanged = 1.7
            if event.key == pygame.K_SPACE:
                if BulletStatus == "AFK":
                    BulletX = HeroX
                    Bullet(BulletX, BulletY)
            if event.key == pygame.K_ESCAPE:
                Game = False
                runpy.run_path('main.py')
                StartScreenRQ()
                
        if event.type == pygame.KEYUP:
            HeroXChanged = 0

    HeroX += HeroXChanged  # Изменение позиции героя
    for i in range(NumberOfAttackers):
        AttackerX[i] += AttackerXChanged[i]

    # Движение патрона
    if BulletY <= 0:
        BulletY = 600
        BulletStatus = "AFK"

    if BulletStatus == "Fire":
        Bullet(BulletX, BulletY)
        BulletY -= BulletYChanged

    # Движение атакующих
    for i in range(NumberOfAttackers):  # Смотрим всех атакующих
        if AttackerY[i] >= 450:  # Если позиция атакующего больше 45 пикселей
            if abs(HeroX - AttackerX[i]) < 80:  # Если они подошли близко
                for j in range(NumberOfAttackers):
                    AttackerY[j] = 2000
                GameOver()  # Завершение работы

        if AttackerX[i] >= 735 or AttackerX[
            i] <= 0:  # Если атакующий зашел за экран
            AttackerXChanged[i] *= -1  # Приближение Атакующих
            AttackerY[i] += AttackerYChanged[i]

        Kill = isCollision(BulletX, AttackerX[i], BulletY, AttackerY[i])
        if Kill:
            Score += 1  # Прибавляем Счет
            BulletY = 600
            BulletStatus = "AFK"  # Ставим Статус Пули на бездействие
            # Рандомное Появление Врагов
            AttackerX[i] = random.randint(64, 736)
            AttackerY[i] = random.randint(30, 200)
            AttackerXChanged[i] *= -1

        Attacker(AttackerX[i], AttackerY[i], i)
    if HeroX <= 16:
        HeroX = 16
    elif HeroX >= 750:
        HeroX = 750

    GameScore(ScoreCoordinateX, ScoreCoordinateY)
    Hero(HeroX, HeroY)
    pygame.display.update()