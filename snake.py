import pygame
import settings
import time
import random

pygame.init()

blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

dis = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Snake Game JRY62")



x1 = settings.X1
y1 = settings.Y1





clock = pygame.time.Clock()
snake_block = settings.SNAKE_BLOCK
snake_speed = settings.SNAKE_SPEED

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [settings.WIDTH / 3, settings.HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = settings.X1
    y1 = settings.Y1

    x1_change = 0
    y1_change = 0

    foodx = settings.FOODX
    foody = settings.FOODY

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

        if x1 >= settings.WIDTH or x1 < 0 or y1 >= settings.HEIGHT or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print('Yum!')
        clock.tick(snake_speed)




    pygame.quit()
    quit()

game_loop()