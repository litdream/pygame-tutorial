import pygame
import random
import sys

# Constants
GRID_SIZE = 16
PLAYABLE_WIDTH = 40
PLAYABLE_HEIGHT = 24
MARGIN = 16
GAME_WIDTH = PLAYABLE_WIDTH * GRID_SIZE + 2 * MARGIN
GAME_HEIGHT = PLAYABLE_HEIGHT * GRID_SIZE + 2 * MARGIN
UI_HEIGHT = 120
SCREEN_WIDTH = GAME_WIDTH
SCREEN_HEIGHT = GAME_HEIGHT + UI_HEIGHT

# Colors (Apple II style)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_SNAKE = (0, 255, 0)
COLOR_APPLE = (255, 80, 0)
COLOR_BORDER = (180, 180, 0)
COLOR_UI_TEXT = (255, 255, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.length = 5
        # Start in the middle of playable area
        self.positions = [(PLAYABLE_WIDTH // 2, PLAYABLE_HEIGHT // 2)]
        for i in range(1, self.length):
            self.positions.append((PLAYABLE_WIDTH // 2 - i, PLAYABLE_HEIGHT // 2))
        self.direction = RIGHT
        self.score = 0
        self.apples_left = 10
        self.snakes_left = 2
        self.level = 1
        self.value = 15

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + x, cur[1] + y)
        
        # Check collision with playable area boundaries
        if new[0] < 0 or new[0] >= PLAYABLE_WIDTH or new[1] < 0 or new[1] >= PLAYABLE_HEIGHT:
            return True # Collision
            
        # Check collision with self
        if new in self.positions:
            return True # Collision
            
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return False

    def draw(self, surface):
        for i, p in enumerate(self.positions):
            # Translate grid to screen
            sx = p[0] * GRID_SIZE + MARGIN
            sy = p[1] * GRID_SIZE + MARGIN
            
            if i == 0: # Head
                # Horizontal bar: 14x4
                h_bar = pygame.Rect(sx + 1, sy + 6, 14, 4)
                # Vertical bar: 4x10
                v_bar = pygame.Rect(sx + 6, sy + 3, 4, 10)
                pygame.draw.rect(surface, COLOR_SNAKE, h_bar)
                pygame.draw.rect(surface, COLOR_SNAKE, v_bar)
            else: # Body
                r = pygame.Rect(sx + 2, sy + 2, GRID_SIZE - 4, GRID_SIZE - 4)
                pygame.draw.rect(surface, COLOR_SNAKE, r)

class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position([])

    def randomize_position(self, snake_positions):
        while True:
            self.position = (random.randint(0, PLAYABLE_WIDTH - 1), random.randint(0, PLAYABLE_HEIGHT - 1))
            if self.position not in snake_positions:
                break

    def draw(self, surface):
        ax = self.position[0] * GRID_SIZE + MARGIN
        ay = self.position[1] * GRID_SIZE + MARGIN
        # Draw apple as a "+" shape
        h_bar = pygame.Rect(ax + 4, ay + 7, 8, 2)
        v_bar = pygame.Rect(ax + 7, ay + 4, 2, 8)
        pygame.draw.rect(surface, COLOR_APPLE, h_bar)
        pygame.draw.rect(surface, COLOR_APPLE, v_bar)

def draw_ui(surface, snake, hi_score):
    ui_rect = pygame.Rect(0, GAME_HEIGHT, SCREEN_WIDTH, UI_HEIGHT)
    pygame.draw.rect(surface, COLOR_BLACK, ui_rect)
    
    font = pygame.font.SysFont("monospace", 22, bold=True)
    
    # Matching the layout from the screenshot
    # Row 1
    score_text = font.render(f"SCORE: {snake.score}", True, COLOR_UI_TEXT)
    hi_score_text = font.render(f"HI SCORE: {hi_score}", True, COLOR_UI_TEXT)
    surface.blit(score_text, (MARGIN, GAME_HEIGHT + 10))
    surface.blit(hi_score_text, (SCREEN_WIDTH // 2, GAME_HEIGHT + 10))
    
    # Row 2
    apples_text = font.render(f"APPLES LEFT: {snake.apples_left}", True, COLOR_UI_TEXT)
    value_text = font.render(f"VALUE: {snake.value}", True, COLOR_UI_TEXT)
    surface.blit(apples_text, (MARGIN, GAME_HEIGHT + 35))
    surface.blit(value_text, (SCREEN_WIDTH // 2, GAME_HEIGHT + 35))
    
    # Row 3
    snakes_text = font.render(f"SNAKES LEFT: {snake.snakes_left}", True, COLOR_UI_TEXT)
    level_text = font.render(f"LEVEL: {snake.level}", True, COLOR_UI_TEXT)
    surface.blit(snakes_text, (MARGIN, GAME_HEIGHT + 60))
    surface.blit(level_text, (SCREEN_WIDTH // 2, GAME_HEIGHT + 60))

    # Row 4
    prompt_text = font.render("HOW MANY PLUMS (0-2)?", True, COLOR_UI_TEXT)
    surface.blit(prompt_text, (SCREEN_WIDTH // 2 - prompt_text.get_width() // 2, GAME_HEIGHT + 85))

def draw_border(surface):
    # Border is drawn in the MARGIN area
    # Top
    pygame.draw.rect(surface, COLOR_BORDER, (0, 0, SCREEN_WIDTH, MARGIN))
    # Bottom (between game and UI)
    pygame.draw.rect(surface, COLOR_BORDER, (0, GAME_HEIGHT - MARGIN, SCREEN_WIDTH, MARGIN))
    # Left
    pygame.draw.rect(surface, COLOR_BORDER, (0, 0, MARGIN, GAME_HEIGHT))
    # Right
    pygame.draw.rect(surface, COLOR_BORDER, (SCREEN_WIDTH - MARGIN, 0, MARGIN, GAME_HEIGHT))
    
    # In the screenshot, there are some gaps in the border (specifically at the bottom center)
    # Let's add that detail
    gap_width = 80
    pygame.draw.rect(surface, COLOR_BLACK, (SCREEN_WIDTH // 2 - gap_width // 2, GAME_HEIGHT - MARGIN, gap_width, MARGIN))
    # And maybe some purple blocks in the gap? The screenshot shows some pink/purple segments.
    pygame.draw.rect(surface, (255, 0, 255), (SCREEN_WIDTH // 2 - gap_width // 2, GAME_HEIGHT - MARGIN + 4, 10, 8))
    pygame.draw.rect(surface, (255, 0, 255), (SCREEN_WIDTH // 2 + gap_width // 2 - 10, GAME_HEIGHT - MARGIN + 4, 10, 8))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Byte Clone")

    snake = Snake()
    apple = Apple()
    hi_score = 0
    
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    snake.reset()
                    game_over = False
                else:
                    if event.key == pygame.K_UP:
                        snake.turn(UP)
                    elif event.key == pygame.K_DOWN:
                        snake.turn(DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.turn(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.turn(RIGHT)

        if not game_over:
            if snake.move():
                game_over = True
                if snake.score > hi_score:
                    hi_score = snake.score
            
            if snake.get_head_position() == apple.position:
                snake.length += 1
                snake.score += snake.value
                snake.apples_left -= 1
                if snake.apples_left <= 0:
                    snake.apples_left = 10
                    snake.level += 1
                apple.randomize_position(snake.positions)

        screen.fill(COLOR_BLACK)
        
        # Draw game area
        draw_border(screen)
        snake.draw(screen)
        apple.draw(screen)
        
        # Draw UI area
        draw_ui(screen, snake, hi_score)
        
        pygame.display.flip()
        clock.tick(10 + (snake.level * 2))

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
