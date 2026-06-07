import pygame
import os
import random
from copy import deepcopy

os.environ['SDL_VIDEO_CENTERED'] = '1'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

COLORS = [
    GRAY,         # GRAY:  reserved for blank.
    (0, 255, 255),     # cyan
    (255, 255, 0),    # yellow
    (128, 0, 128),     # purple
    (0, 0, 255),       # blue
    (255, 165, 0),      # orange
    (0, 255, 0),       # green
    (255, 0, 0),        # red
    ]


CELL_SIZE = 40
STAGE_WIDTH = 10
STAGE_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * ( STAGE_WIDTH + 2 )
SCREEN_HEIGHT = CELL_SIZE * ( STAGE_HEIGHT + 1 )

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
        [[2,2],
         [2,2]]
    ],
    'T': [
        [[0,3,0],
         [3,3,3],
         [0,0,0]],

        [[0,3,0],
         [0,3,3],
         [0,3,0]],

        [[0,0,0],
         [3,3,3],
         [0,3,0]],

        [[0,3,0],
         [3,3,0],
         [0,3,0]]
    ],
    'J': [
        [[4,0,0],
         [4,4,4],
         [0,0,0]],

        [[0,4,4],
         [0,4,0],
         [0,4,0]],

        [[0,0,0],
         [4,4,4],
         [0,0,4]],

        [[0,4,0],
         [0,4,0],
         [4,4,0]]

    ],
    'L': [
        [[0,0,5],
         [5,5,5],
         [0,0,0]],

        [[0,5,0],
         [0,5,0],
         [0,5,5]],

        [[0,0,0],
         [5,5,5],
         [5,0,0]],

        [[5,5,0],
         [0,5,0],
         [0,5,0]]
    ],
    'S': [
        [[0,6,6],
         [6,6,0],
         [0,0,0]],

        [[0,6,0],
         [0,6,6],
         [0,0,6]]
    ],
    'Z': [
        [[7,7,0],
         [0,7,7],
         [0,0,0]],

        [[0,0,7],
         [0,7,7],
         [0,7,0]]
    ],
}


def create_empty_stage():
    rtn = [
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    return rtn


def main():
    pygame.init()

    pygame.key.set_repeat(0)
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    running = True
    fps = 60         # for block left/right sensitivity
    stage = create_empty_stage()

    last_update_time = pygame.time.get_ticks()   # get current time in millis


    # Initial condition
    falling_speed = 500   # 0.5sec
    curblk_type = random.choice( list(SHAPES.keys()) )
    curblk_lst_shape = SHAPES[ curblk_type ]

    curblk_index = 0
    curblk_shape = curblk_lst_shape[curblk_index]
    blk_x, blk_y = 5, 0
    
    while running:
        screen.fill(BLACK)
        current_time = pygame.time.get_ticks()   # get current time in millis

        print(last_update_time,  current_time)
        
        delta_time = clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:     # CTRL-X:  quit game.
                    if event.mod & pygame.KMOD_CTRL:
                        running = False
        
        # DRAW Block
        for dy, row in enumerate(curblk_shape):
            for dx, cell in enumerate(row):
                if cell !=0:
                    rect = pygame.Rect( (blk_x + dx) *CELL_SIZE, \
                                       (blk_y + dy) * CELL_SIZE, \
                                       CELL_SIZE, CELL_SIZE )
                    pygame.draw.rect(screen, COLORS[cell], rect)
                    
        # DRAW stage
        for dy, row in enumerate(stage):
            for dx, cell in enumerate(row):
                if cell !=0 :
                    rect = pygame.Rect( dx*CELL_SIZE, dy*CELL_SIZE, CELL_SIZE, CELL_SIZE )
                    pygame.draw.rect(screen, GRAY, rect)
                    
        pygame.display.flip()                    

        # After moved, update values for the next round.
        if current_time - last_update_time > falling_speed:
            blk_y += 1
            last_update_time = current_time

if __name__  == '__main__':
    main()
