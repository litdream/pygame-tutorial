import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

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

    pygame.key.set_repeat(0)
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    running = True
    fps = 60         # for block left/right sensitivity

    last_update_time = pygame.time.get_ticks()   # get current time in millis
    while running:
        screen.fill(BLACK)
        current_time = pygame.time.get_ticks()   # get current time in millis

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:     # CTRL-X:  quit game.
                    if event.mod & pygame.KMOD_CTRL:
                        running = False

        pygame.display.flip()
        

if __name__  == '__main__':
    main()
