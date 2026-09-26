import os
import pygame
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

# SETUP Global
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60  # Conventionally uppercase for constants

def main():
    pygame.init()

    pygame.key.set_repeat(0)    # Turn-off key auto-repeat
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Pygame Window")
    clock = pygame.time.Clock()

    running = True
    last_update_time = pygame.time.get_ticks()   # Get time in millis

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:     # CTRL-X: Quit game
                    if event.mod & pygame.KMOD_CTRL:
                        running = False


        # Render / Draw
        screen.fill(BLACK)
        
        #----------
        # Custom Draw calls go here
        #----------
        # pygame.draw.rect(screen, WHITE, (50, 50, 100, 100))


        # Display Update
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
