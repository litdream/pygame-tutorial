import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Input")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Player rectangle:  Sprite alternative.
player_size = 50
player_rect = pygame.Rect(
    (WIDTH - player_size) // 2, 
    (HEIGHT - player_size) // 2, 
    player_size, 
    player_size
)
player_speed = 5

# --- Game Loop ---
clock = pygame.time.Clock()
def main():
    """Main game loop."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get keycode and handle it.
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed
        if keys[pygame.K_UP]:
            player_rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            player_rect.y += player_speed

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
        pygame.draw.rect(screen, WHITE, player_rect)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
