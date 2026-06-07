import pygame
import os
import random
from copy import deepcopy


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

def get_stage():
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

def can_block_apply(stage, block, block_idx, block_left_x, block_left_y) -> bool:
    stg = deepcopy(stage)
    # TODO:  implement this.  going upstairs with Justin


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
    fall_speed = 500
    curblk_type = random.choice(block_types)
    curblk_lst = SHAPES[curblk_type]
    curblk_idx = 0
    (blk_x, blk_y) = ( 5 - len(SHAPES[curblk_type][0])//2 ,0)
    stage = get_stage()

    last_update_time = pygame.time.get_ticks()  # Get time in millis.
    
    while running:
        screen.fill(BLACK)

        delta_time = clock.tick(60)
        current_time = pygame.time.get_ticks()  # Get time in millis.
        #print(last_update_time, current_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:     # CTRL-X:  quit game.
                    if event.mod & pygame.KMOD_CTRL:
                        running = False
                if event.key == pygame.K_SPACE:
                    curblk_idx += 1
                    curblk_idx %= len(curblk_lst)


        # DRAW block
        shape = curblk_lst[curblk_idx]
        #print(shape)
        #print(blk_x, blk_y)
        
        for dy,blk_row in enumerate(shape):
            for dx,val in enumerate(blk_row):
                if val == 1:
                    rect = pygame.Rect( (blk_x + dx)*CELL_SIZE, blk_y + dy*CELL_SIZE, CELL_SIZE, CELL_SIZE )
                    pygame.draw.rect(screen, GRAY, rect)
                
                
        # DRAW Stage
        y = 0
        for stage_row in stage:
            for dx,val in enumerate(stage_row):
                if val == 1:
                    rect = pygame.Rect( dx*CELL_SIZE, y, CELL_SIZE, CELL_SIZE )
                    pygame.draw.rect(screen, GRAY, rect)
            y += CELL_SIZE
            
        pygame.display.flip()

        if current_time - last_update_time > fall_speed:
            blk_y += CELL_SIZE
            last_update_time = current_time

        # Collision:  new init.
        if not can_block_apply(stage, curblk_lst, curblk_idx, blk_x, blk_y + CELL_SIZE):
            for dy,blk_row in enumerate(shape):
                for dx,val in enumerate(blk_row):
                    if val == 1:
                        print(blk_x, blk_y, dx, dy)
                        stage[blk_y+dy][blk_x+dx] = 1
                                    
            curblk_type = random.choice(block_types)
            curblk_lst = SHAPES[curblk_type]
            curblk_idx = 0
            (blk_x, blk_y) = ( 5 - len(SHAPES[curblk_type][0])//2 ,0)
        

if __name__ == '__main__':
    main()
