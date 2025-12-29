import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("hello")

BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLUE = (153, 225, 225)
font = pygame.font.SysFont("Arial", 64)

# Surface:   Try  Renderer/Texture for SDL2/low-level-accel.
text_surface = font.render("Hello, Pygame!", True, BLUE)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
clock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
