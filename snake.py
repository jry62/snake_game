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

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, settings.BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [settings.WIDTH / 6, settings.HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = settings.X1
    y1 = settings.Y1

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = settings.FOODX
    foody = settings.FOODY

    while not game_over:

        while game_close == True:
            dis.fill(settings.BLUE)
            message('You lost! Press C-Play Again or Q-Quit', settings.RED)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= settings.WIDTH or x1 < 0 or y1 >= settings.HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(settings.BLUE)
        pygame.draw.rect(dis, settings.GREEN, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, settings.WIDTH - snake_block) / 10.0)
            foody = round(random.randrange(0, settings.HEIGHT - snake_block) / 10.0)
            length_of_snake += 1

        
        clock.tick(snake_speed)




    pygame.quit()
    quit()

game_loop()