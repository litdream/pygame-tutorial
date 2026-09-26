import os
import pygame
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'


# SETUP Global
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)


def main():
    pygame.init()

    pygame.key.set_repeat(0)    # turn-off: key auto-repeat
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    running = True
    last_update_time = pygame.time.get_ticks()   # Get time in millis
    
    while running:
        screen.fill(BLACK)
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:     # CTRL-X:  quit game.
                    if event.mod & pygame.KMOD_CTRL:
                        running = False

        # Custom Draw
        # pygame.draw(xxx)
        # Then, flip the buffer.
            
        pygame.display.flip()

        
                    

