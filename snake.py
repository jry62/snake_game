import pygame
import settings
import time

pygame.init()

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
dis = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Snake Game JRY62")

game_over = False

x1 = settings.X1
y1 = settings.Y1

snake_block = settings.SNAKE_BLOCK

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = settings.SNAKE_SPEED

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [settings.WIDTH / 2, settings.HEIGHT / 2])

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
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)

message("You Lost!", red)
pygame.display.update()
time.sleep(2)


pygame.quit()
quit()