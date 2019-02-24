"""
This is example similar to move_with_walls_example.py

"""

import pygame
import pycolor

class Player(pygame.sprite.Sprite):
    pass

class Wall(pygame.sprite.Sprite):
    pass


def main():
    pygame.init()
    size = [700, 500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Maze-like Wall example")
    clock = pygame.time.Clock()
    done = False

    while not done:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                done = True
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                    print("pressed: CTRL + q")
                    done = True

        # TODO: update logic
                    
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
                
if __name__ == '__main__':
    main()
