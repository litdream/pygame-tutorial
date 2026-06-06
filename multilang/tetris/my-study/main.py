import pygame
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

# -- Colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = {
    "cyan": (0, 255, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128),
    "blue": (0, 0, 255),
    "orange": (255, 165, 0),
    "green": (0, 255, 0),
    "red": (255, 0, 0),
}

CELL_SIZE = 40
STAGE_WIDTH = 10
STAGE_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * STAGE_WIDTH
SCREEN_HEIGHT = CELL_SIZE * STAGE_HEIGHT



# Game setup

SHAPES = {
    'I': [
        [[0,1,0,0],
         [0,1,0,0],
         [0,1,0,0],
         [0,1,0,0]],
        
        [[0,0,0,0],
         [1,1,1,1],
         [0,0,0,0],
         [0,0,0,0]]
    ],
    'O': [
        [[1,1],
         [1,1]]
    ],
    'T': [
        [[0,1,0],
         [1,1,1],
         [0,0,0]],
        
        [[0,1,0],
         [0,1,1],
         [0,1,0]],
        
        [[0,0,0],
         [1,1,1],
         [0,1,0]],
        
        [[0,1,0],
         [1,1,0],
         [0,1,0]]
    ],
    'J': [
        [[1,0,0],
         [1,1,1],
         [0,0,0]],

        [[0,1,1],
         [0,1,0],
         [0,1,0]],

        [[0,0,0],
         [1,1,1],
         [0,0,1]],

        [[0,1,0],
         [0,1,0],
         [1,1,0]]

    ],
    'L': [
        [[0,0,1],
         [1,1,1],
         [0,0,0]],

        [[0,1,0],
         [0,1,0],
         [0,1,1]],

        [[0,0,0],
         [1,1,1],
         [1,0,0]],

        [[1,1,0],
         [0,1,0],
         [0,1,0]]
    ],
    'S': [
        [[0,1,1],
         [1,1,0],
         [0,0,0]],

        [[0,1,0],
         [0,1,1],
         [0,0,1]]        
    ],
    'Z': [
        [[1,1,0],
         [0,1,1],
         [0,0,0]],

        [[0,0,1],
         [0,1,1],
         [0,1,0]]
    ],
}


def main():
    pygame.init()

    # This disables pygame's built-in key repeat
    pygame.key.set_repeat(0)
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    running = True
    block_types = list("IOTJLSZ")

    # initial    
    curblk_type = random.choice(block_types)      
    curblk_lst = SHAPES[curblk_type]
    curblk_idx = 0

    while running:
        screen.fill(BLACK)
        

        delta_time = clock.tick(60)
        current_time = pygame.time.get_ticks()  # Get time in millis.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:     # CTRL-X:  quit game.
                    if event.mod & pygame.KMOD_CTRL:
                        running = False

        # DRAW BLOCKS
        pygame.display.flip()
    pygame.display.flip()
        

if __name__ == '__main__':
    main()
