import pygame
import os
import random
from copy import deepcopy
import pytest

os.environ['SDL_VIDEO_CENTERED'] = '1'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

COLORS = [
    BLACK,
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
        [[0,2,0,0],
         [0,2,0,0],
         [0,2,0,0],
         [0,2,0,0]],

        [[0,0,0,0],
         [2,2,2,2],
         [0,0,0,0],
         [0,0,0,0]]
    ],
    'O': [
        [[3,3],
         [3,3]]
    ],
    'T': [
        [[0,4,0],
         [4,4,4],
         [0,0,0]],

        [[0,4,0],
         [0,4,4],
         [0,4,0]],

        [[0,0,0],
         [4,4,4],
         [0,4,0]],

        [[0,4,0],
         [4,4,0],
         [0,4,0]]
    ],
    'J': [
        [[5,0,0],
         [5,5,5],
         [0,0,0]],

        [[0,5,5],
         [0,5,0],
         [0,5,0]],

        [[0,0,0],
         [5,5,5],
         [0,0,5]],

        [[0,5,0],
         [0,5,0],
         [5,5,0]]

    ],
    'L': [
        [[0,0,6],
         [6,6,6],
         [0,0,0]],

        [[0,6,0],
         [0,6,0],
         [0,6,6]],

        [[0,0,0],
         [6,6,6],
         [6,0,0]],

        [[6,6,0],
         [0,6,0],
         [0,6,0]]
    ],
    'S': [
        [[0,7,7],
         [7,7,0],
         [0,0,0]],

        [[0,7,0],
         [0,7,7],
         [0,0,7]]
    ],
    'Z': [
        [[8,8,0],
         [0,8,8],
         [0,0,0]],

        [[0,0,8],
         [0,8,8],
         [0,8,0]]
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

def applicable(stage, curblk_shape, block_location) -> bool:
    """
    return false if block's current position collides with wall, or existing blocks.
    otherwise returns true
    """
    (bx, by) = block_location
    x, y = bx, by
    for dy, row in enumerate(curblk_shape):
        for dx, cell in enumerate(row):
            if cell != 0 and stage[y+dy][x+dx] != 0:
                return False
    return True

def new_block():
    curblk_type = random.choice( list(SHAPES.keys()) )
    curblk_lst_shape = SHAPES[ curblk_type ]

    curblk_index = 0
    curblk_shape = curblk_lst_shape[curblk_index]
    blk_x, blk_y = 5, 0
    return curblk_lst_shape, curblk_shape, blk_x, blk_y

def collapse_stage(stage) -> bool:
    for idx, row in enumerate(stage):
        if 0 not in row and row != [1,1,1,1,1,1,1,1,1,1,1,1]:
            stage.pop(idx)
            stage.insert(0, [1,0,0,0,0,0,0,0,0,0,0,1])
            return True
    return False

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
    curblk_lst_shape, curblk_shape, blk_x, blk_y  = new_block()
    curblk_index = 0
    
    while running:
        screen.fill(BLACK)
        current_time = pygame.time.get_ticks()   # get current time in millis

        #print(last_update_time,  current_time)
        
        delta_time = clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:     # CTRL-X:  quit game.
                    if event.mod & pygame.KMOD_CTRL:
                        running = False
                if event.key == pygame.K_UP:    # Up: rotate
                    next_index = curblk_index
                    next_index -= 1
                    next_index %= len(curblk_lst_shape)
                    next_shape = curblk_lst_shape[ next_index ]
                    if applicable(stage, next_shape, (blk_x, blk_y)):
                        curblk_index += 1
                        curblk_index %= len(curblk_lst_shape)

                        #print(curblk_index, len(curblk_lst_shape))
                        curblk_shape = curblk_lst_shape[ curblk_index ]

                if event.key == pygame.K_LEFT:   # left
                    if applicable(stage, curblk_shape, (blk_x-1, blk_y)):
                        blk_x -= 1
                        
                if event.key == pygame.K_RIGHT:   # right
                    if applicable(stage, curblk_shape, (blk_x+1, blk_y)):                    
                        blk_x += 1

                if event.key == pygame.K_SPACE:
                    while applicable(stage, curblk_shape, (blk_x, blk_y+1)):
                        blk_y +=1
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
                    pygame.draw.rect(screen, COLORS[cell], rect)
                    
        pygame.display.flip()                    

        # After moved, update values for the next round.
        if current_time - last_update_time > falling_speed:
            blk_y += 1
            last_update_time = current_time

        # Check if we have to re-generate block.
        if not applicable(stage, curblk_shape, (blk_x, blk_y +1)):
            for dy, row in enumerate(curblk_shape):
                for dx, cell in enumerate(row):
                    #print(cell)
                    if cell != 0:
                        # Copy block into the stage.
                        stage[blk_y + dy][blk_x + dx] = cell
                        
            # Regenerate block
            #  - TODO: refactor:  copied from above
            curblk_lst_shape, curblk_shape, blk_x, blk_y  = new_block()
            curblk_index = 0

        while True:
            if not collapse_stage(stage):
                break
            
        
                        

if __name__  == '__main__':
    main()
