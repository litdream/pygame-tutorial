import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Input")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player rectangle:  Sprite alternative.
player_size = 50
player_rect = pygame.Rect(
    (WIDTH - player_size) // 2, 
    (HEIGHT - player_size) // 2, 
    player_size, 
    player_size
)
player_color = WHITE

# --- Game Loop ---
clock = pygame.time.Clock()
def main():
    """Main game loop."""
    global player_color
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_color = RED
            if event.type == pygame.MOUSEBUTTONUP:
                player_color = WHITE

        # Get mouse position and move the player.
        mouse_pos = pygame.mouse.get_pos()
        player_rect.centerx = mouse_pos[0]
        player_rect.centery = mouse_pos[1]

        # Keep player on screen
        if player_rect.left < 0:
            player_rect.left = 0
        if player_rect.right > WIDTH:
            player_rect.right = WIDTH
        if player_rect.top < 0:
            player_rect.top = 0
        if player_rect.bottom > HEIGHT:
            player_rect.bottom = HEIGHT

        screen.fill(BLACK)
        pygame.draw.rect(screen, player_color, player_rect)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
