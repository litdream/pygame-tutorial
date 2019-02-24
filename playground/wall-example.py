"""
This is example similar to move_with_walls_example.py

"""

import pygame
import pycolor

class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Player sprite location, and rect.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0

        # This is the reference shortcut for walls (or later platforms)
        #   - collision detection is easy by sprite-group.
        #
        self.walls = None

class Wall(pygame.sprite.Sprite):
    pass


def main():
    pygame.init()
    size = [700, 500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Maze-like Wall example")
    clock = pygame.time.Clock()
    done = False

    player = Player(50,50)
    
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
