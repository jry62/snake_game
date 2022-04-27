import random

from pyparsing import FollowedBy

HEIGHT = 800
WIDTH = 600

X1 = WIDTH / 2
Y1 = HEIGHT / 2

SNAKE_BLOCK = 10
SNAKE_SPEED = 30

FOODX = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0 ) * 10.0
FOODY = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0 ) * 10.0