# Game options and settings
import random

TITLE = "Jump"
WIDTH = 480
HEIGHT = 600
FPS = 30
FONT_NAME = ('arial.ttf')

# Player Properties
PLAYER_ACC = 1
PLAYER_FRICTION = -0.2
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Starting Platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                (random.randint(10, 300), random.randint(60, 300), 100, 20),
                (350, 200, 100, 20),
                (175, 100, 50, 20)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
