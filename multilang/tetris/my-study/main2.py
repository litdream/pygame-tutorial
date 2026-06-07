import pygame
import random


os.environ['SDL_VIDEO_CENTERED'] = '1'

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


# SETUP Global
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

CELL_SIZE = 40
STAGE_WIDTH = 10
STAGE_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * ( STAGE_WIDTH + 2 )
SCREEN_HEIGHT = CELL_SIZE * ( STAGE_HEIGHT + 1 )

def main():
    pygame.init()

    pygame.key.set_repeat(0)    # turn-off: key auto-repeat
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    running = True
    last_update_time = pygame.time.get_ticks()   # Get time in millis
    
    # Initial state
    stage = get_stage()
    fps = 60  

    curblk_type = random.choice( list("IOTJLSZ"))
    curblk_shape_list = SHAPES[curblk_type]
    curblk_idx = 0
    blk_x, blk_y = ( 5 - len(curblk_shape_list[0])//2, 0)   # will fall down
    
    while running:
        screen.fill(BLACK)
        clock.tick(fps)

        shape = curblk_shape_list[curblk_idx]
        
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
        for dy,blk_row in enumerate(shape):
            for dx,val in enumerate(blk_row):
                if val == 1:
                    rect = pygame.Rect( (blk_x + dx)*CELL_SIZE, blk_y + dy*CELL_SIZE, CELL_SIZE, CELL_SIZE )
                    pygame.draw.rect(screen, WHITE, rect)

        # DRAW stage
        y = 0
        for stage_row in stage:
            for dx,val in enumerate(stage_row):
                if val == 1:
                    rect = pygame.Rect( dx*CELL_SIZE, y, CELL_SIZE, CELL_SIZE )
                    pygame.draw.rect(screen, GRAY, rect)
            y += CELL_SIZE
            
        pygame.display.flip()

        
                    
