import pygame
import sys

# --- Initialization ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Movement and Shooting")

# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- Player (Spaceship) ---
try:
    player_img = pygame.image.load("sprite/spaceship.png")
    player_img = pygame.transform.scale(player_img, (80, 80)) # Resized to 80x80
except pygame.error as e:
    print(f"Unable to load image sprite/spaceship.png: {e}")
    pygame.quit()
    sys.exit()

player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 50))
player_speed = 5

# --- Bullets ---
bullets = []
bullet_speed = 10
bullet_cooldown = 200  # milliseconds
last_shot = pygame.time.get_ticks()

# --- Game Loop ---
clock = pygame.time.Clock()
def main():
    """Main game loop."""
    global last_shot
    
    while True:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- Key presses for continuous movement and shooting ---
        keys = pygame.key.get_pressed()
        
        # Movement
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += player_speed
        if keys[pygame.K_UP] and player_rect.top > 0:
            player_rect.y -= player_speed
        if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
            player_rect.y += player_speed
            
        # Shooting
        if keys[pygame.K_SPACE]:
            time_now = pygame.time.get_ticks()
            if time_now - last_shot > bullet_cooldown:
                bullet = pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10)
                bullets.append(bullet)
                last_shot = time_now

        # --- Game State Updates ---
        # Move bullets
        for bullet in bullets:
            bullet.y -= bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)

        # --- Drawing ---
        screen.fill(BLACK)
        screen.blit(player_img, player_rect)
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, bullet)
        
        pygame.display.flip()

        # --- Frame Rate ---
        clock.tick(60)

if __name__ == "__main__":
    main()
