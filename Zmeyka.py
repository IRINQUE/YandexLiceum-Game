import pygame
import time
import random

pygame.init() # Инициализация
WhiteColor = (255, 255, 255) # Белый Цвет
Background = (0, 0, 0) # Цвет Фона
RedColor = (213, 50, 80) # Красный Цвет
GreenColor = (0, 255, 0) # Зеленый Цвет
ScreenWidth, ScreenHeight = 800, 600 # Размер Экрана

Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight)) # Экран
pygame.display.set_caption('RQ - Змейка') # Название игры
clock = pygame.time.Clock() # FPS
SnakeHeight = 10 # Размер Змейки
SnakeSpeed = 10 # Скорость перемещения змейки
font = pygame.font.SysFont("bahnschrift", 25) # Шрифт игры

def GameScore(Score):
    Score = font.render("Счет:" + str(Score), True, WhiteColor) # Текст
    Screen.blit(Score, [800 / 2 - Score.get_width() // 2, 0]) # Вывод

def SnakePos(SnakeHeight, SnakePositions):
    for X in SnakePositions: # Смотрим список с последними местами змейки
        pygame.draw.rect(Screen, GreenColor, [X[0], X[1], SnakeHeight, SnakeHeight]) # Отрисовка

def MessageFail(msg, color):
    message = font.render(msg, True, color) # Сообщение
    Screen.blit(message, [800 / 2 - message.get_width() // 2, 600 / 2 - message.get_height() // 2]) # Вывод

def GameZmeyka():
    GameFail = False # Статус Игры
    GameClose = False # Статус Игры
    X1 = ScreenWidth / 2 # Серидина по X
    Y1 = ScreenHeight / 2 # Середина по Y
    X1Changed = 0 
    Y1Changed = 0
    SnakePositions = list() # Список позиций змейки
    SnakeLenght = 1 # Стандарная длина змеи

    # Генерация по X и Y Еды
    BoostCoordinateX = round(random.randrange(0, ScreenWidth - SnakeHeight) / 10.0) * 10.0 
    BoostCoordinateY = round(random.randrange(0, ScreenHeight - SnakeHeight) / 10.0) * 10.0

    # Игровой Цикл
    while not GameFail:
        while GameClose == True: # Пока игра завершена
            Screen.fill(Background) # Фон
            MessageFail("GAME OVER", WhiteColor) # Сообщение
            GameScore(SnakeLenght - 1) # Счет
            pygame.display.update() # Обновляем экран
            for event in pygame.event.get(): # Отслеживаем действия после смерти
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Если Esc - Выход
                        GameFail = True
                        GameClose = False
                    if event.key == pygame.K_SPACE: # Если Space - Заново
                        GameZmeyka()
        # Цикл пока игра идет:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Выход из игры
                GameFail = True
            if event.type == pygame.KEYDOWN: # Если нажата кнопка
                if event.key == pygame.K_a:
                    X1Changed = -SnakeHeight # Влево движение
                    Y1Changed = 0
                elif event.key == pygame.K_d:
                    X1Changed = SnakeHeight # Движение вправо
                    Y1Changed = 0
                elif event.key == pygame.K_w:
                    Y1Changed = -SnakeHeight # Движение вверх!
                    X1Changed = 0
                elif event.key == pygame.K_s:
                    Y1Changed = SnakeHeight # Движение вниз
                    X1Changed = 0

        if X1 >= ScreenWidth or X1 < 0 or Y1 >= ScreenHeight or Y1 < 0: # Выход за пределы
            GameClose = True # Статус завершенной игры => Выход

        X1 += X1Changed # Изменения X
        Y1 += Y1Changed # Изменения Y
        Screen.fill(Background) # Фон
        pygame.draw.rect(Screen, RedColor, [BoostCoordinateX, BoostCoordinateY, SnakeHeight, SnakeHeight]) # Отрисовка
        SnakeHead = list() # Голова
        SnakeHead.append(X1) # Координа X головы
        SnakeHead.append(Y1) # Координата Y головы
        SnakePositions.append(SnakeHead) # Позиция змейки
        if len(SnakePositions) > SnakeLenght:
            del SnakePositions[0] # Чистим конец змейки(Движение)
        for x in SnakePositions[:-1]: # Если мы врезались сами в себя
            if x == SnakeHead:
                GameClose = True # Конец игры
        SnakePos(SnakeHeight, SnakePositions)
        GameScore(SnakeLenght - 1)
        pygame.display.update() # Обновление экрана
        if X1 == BoostCoordinateX and Y1 == BoostCoordinateY: # Если мы съели ягодку
            # Спавн Новой
            BoostCoordinateX = round(random.randrange(0, ScreenWidth - SnakeHeight) / 10.0) * 10.0
            BoostCoordinateY = round(random.randrange(0, ScreenHeight - SnakeHeight) / 10.0) * 10.0
            SnakeLenght += 1 # Увеличение длины
        clock.tick(SnakeSpeed)
    pygame.quit() # Выход иг игры
GameZmeyka()