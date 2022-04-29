import random


HEIGHT = 600
WIDTH = 600

X1 = WIDTH / 2
Y1 = HEIGHT / 2

SNAKE_BLOCK = 10
SNAKE_SPEED = 15

FOODX = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0 ) * 10.0
FOODY = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0 ) * 10.0


WHITE = (255,255,255)
YELLOW = (255,255,102)
BLACK = (0,0,0)
RED = (213,50,0)
GREEN = (0,255,0)
BLUE = (50,153,213)
