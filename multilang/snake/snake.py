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
COLOR_WALL = (180, 180, 180) # Retro grey/white for inner walls

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class LevelManager:
    def __init__(self):
        self.levels = self._define_levels()

    def _define_levels(self):
        levels = {}
        for i in range(1, 21):
            levels[i] = set()
        
        # Level 1: No walls
        
        # Level 2: Horizontal bar in center
        for x in range(10, 30):
            levels[2].add((x, 12))
            
        # Level 3: Cross in center
        for x in range(10, 30):
            levels[3].add((x, 12))
        for y in range(6, 18):
            levels[3].add((20, y))
            
        # Level 4: "E" shape
        for y in range(6, 18):
            levels[4].add((14, y))
        for x in range(14, 26):
            levels[4].add((x, 6))
            levels[4].add((x, 12))
            levels[4].add((x, 17))
            
        # Level 5: Double H / Three verticals
        for y in range(6, 18):
            levels[5].add((14, y))
            levels[5].add((25, y))
            levels[5].add((36, y))
        for x in range(14, 37):
            levels[5].add((x, 12))

        # Level 6: Box with gap at top
        for x in range(10, 30):
            if x < 18 or x > 22: # Gap in middle
                levels[6].add((x, 6))
            levels[6].add((x, 18))
        for y in range(6, 19):
            levels[6].add((10, y))
            levels[6].add((30, y))
            
        # Level 7: Rotated E / Fork
        for y in range(6, 18):
            levels[7].add((14, y))
        for x in range(14, 26):
            levels[7].add((x, 6))
            levels[7].add((x, 11))
            levels[7].add((x, 17))
        for y in range(6, 18):
            levels[7].add((26, y))

        # Level 8: Horizontal line with center gap
        for x in range(0, 40):
            if x < 18 or x > 22:
                levels[8].add((x, 12))
                
        # Level 9: Multiple vertical bars
        for x in [5, 12, 19, 26, 33]:
            for y in range(4, 20):
                levels[9].add((x, y))

        # Level 10: Maze-like E/Fork pattern
        for x in range(8, 32):
            levels[10].add((x, 6))
            levels[10].add((x, 18))
        for y in range(6, 19):
            levels[10].add((8, y))
        for x in range(8, 25):
            levels[10].add((x, 12))
        for y in range(6, 13):
            levels[10].add((31, y))

        # Level 11: Two boxes
        for x in range(5, 18):
            levels[11].add((x, 6))
            levels[11].add((x, 18))
        for y in range(6, 19):
            levels[11].add((5, y))
            if y < 11 or y > 13:
                levels[11].add((17, y))
        for x in range(22, 35):
            levels[11].add((x, 6))
            levels[11].add((x, 18))
        for y in range(6, 19):
            if y < 11 or y > 13:
                levels[11].add((22, y))
            levels[11].add((34, y))
        for y in range(6, 19):
            levels[11].add((20, y))

        # Level 12: Box with gaps and center wall
        for x in range(10, 30):
            if x < 18 or x > 22:
                levels[12].add((x, 6))
                levels[12].add((x, 18))
        for y in range(6, 19):
            if y < 11 or y > 13:
                levels[12].add((10, y))
                levels[12].add((30, y))
        for y in range(10, 15):
            levels[12].add((20, y))

        # Level 13: Spiral/Snake Maze
        for x in range(5, 35):
            levels[13].add((x, 4))
            levels[13].add((x, 20))
        for y in range(4, 10):
            levels[13].add((5, y))
        for x in range(5, 20):
            levels[13].add((x, 10))
        for y in range(10, 21):
            levels[13].add((20, y))
        for x in range(20, 35):
            levels[13].add((x, 15))
        for y in range(4, 15):
            levels[13].add((34, y))

        # Level 14: Four boxes
        for x in range(5, 35):
            levels[14].add((x, 4))
            levels[14].add((x, 12))
            levels[14].add((x, 20))
        for y in range(4, 21):
            levels[14].add((5, y))
            levels[14].add((19, y))
            levels[14].add((34, y))
        # Add gaps
        levels[14].discard((19, 7))
        levels[14].discard((19, 16))
        levels[14].discard((12, 12))
        levels[14].discard((26, 12))

        # Level 15: Interlocking
        for y in range(4, 16):
            levels[15].add((10, y))
        for x in range(10, 25):
            levels[15].add((x, 15))
        for y in range(8, 20):
            levels[15].add((25, y))
        for x in range(15, 40):
            levels[15].add((x, 8))
        for x in range(0, 20):
            levels[15].add((x, 20))

        # Level 16: Simple Cross with Gaps
        for x in range(0, 40):
            if x < 18 or x > 22:
                levels[16].add((x, 12))
        for y in range(0, 24):
            if y < 10 or y > 14:
                levels[16].add((20, y))

        # Level 17: Pinwheel
        for x in range(10, 20): levels[17].add((x, 6))
        for y in range(6, 16): levels[17].add((20, y))
        for x in range(21, 31): levels[17].add((x, 18))
        for y in range(8, 18): levels[17].add((10, y))

        # Level 18: Double Cross
        for x in range(5, 35):
            if x < 18 or x > 22:
                levels[18].add((x, 8))
                levels[18].add((x, 16))
        for y in range(0, 24):
            if y < 20: # Gap at bottom for starting
                levels[18].add((20, y))

        # Level 19: Concentric
        for x in range(5, 35):
            levels[19].add((x, 4))
            levels[19].add((x, 20))
        for y in range(4, 21):
            levels[19].add((5, y))
            levels[19].add((34, y))
        for x in range(10, 30):
            levels[19].add((x, 8))
            levels[19].add((x, 16))
        for y in range(8, 17):
            levels[19].add((10, y))
            levels[19].add((29, y))
        # Gaps
        levels[19].discard((20, 4))
        levels[19].discard((20, 20))
        levels[19].discard((5, 12))
        levels[19].discard((34, 12))

        # Level 20: Full Maze (Simplified representation)
        for x in range(0, 40, 4):
            for y in range(0, 24):
                if (x // 4) % 2 == 0:
                    if y > 4: levels[20].add((x, y))
                else:
                    if y < 20: levels[20].add((x, y))
        for x in range(40):
            if x % 8 == 0: continue
            levels[20].add((x, 12))

        return levels

    def get_walls(self, level):
        return self.levels.get(level, set())

class Snake:
    def __init__(self):
        self.snakes_left = 3
        self.reset_game()

    def reset_game(self):
        self.score = 0
        self.level = 1
        self.apples_left = 10
        self.value = 15
        self.reset_level()

    def reset_level(self):
        self.length = 5
        # Start at bottom center moving UP
        self.positions = [(PLAYABLE_WIDTH // 2, PLAYABLE_HEIGHT - 2)]
        for i in range(1, self.length):
            self.positions.append((PLAYABLE_WIDTH // 2, PLAYABLE_HEIGHT - 2 + i))
        self.direction = UP
        self.new_direction = UP

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if (point[0] * -1, point[1] * -1) == self.direction:
            return
        self.new_direction = point

    def move(self, walls):
        self.direction = self.new_direction
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + x, cur[1] + y)
        
        # Check collision with playable area boundaries
        if new[0] < 0 or new[0] >= PLAYABLE_WIDTH or new[1] < 0 or new[1] >= PLAYABLE_HEIGHT:
            return True # Collision
            
        # Check collision with self
        if new in self.positions:
            return True # Collision
            
        # Check collision with walls
        if new in walls:
            return True # Collision
            
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return False

    def draw(self, surface):
        for i, p in enumerate(self.positions):
            sx = p[0] * GRID_SIZE + MARGIN
            sy = p[1] * GRID_SIZE + MARGIN
            
            if i == 0: # Head
                h_bar = pygame.Rect(sx + 1, sy + 6, 14, 4)
                v_bar = pygame.Rect(sx + 6, sy + 3, 4, 10)
                pygame.draw.rect(surface, COLOR_SNAKE, h_bar)
                pygame.draw.rect(surface, COLOR_SNAKE, v_bar)
            else: # Body
                r = pygame.Rect(sx + 2, sy + 2, GRID_SIZE - 4, GRID_SIZE - 4)
                pygame.draw.rect(surface, COLOR_SNAKE, r)

class Apple:
    def __init__(self):
        self.position = (0, 0)

    def randomize_position(self, snake_positions, walls):
        while True:
            self.position = (random.randint(0, PLAYABLE_WIDTH - 1), random.randint(0, PLAYABLE_HEIGHT - 1))
            if self.position not in snake_positions and self.position not in walls:
                break

    def draw(self, surface):
        ax = self.position[0] * GRID_SIZE + MARGIN
        ay = self.position[1] * GRID_SIZE + MARGIN
        h_bar = pygame.Rect(ax + 4, ay + 7, 8, 2)
        v_bar = pygame.Rect(ax + 7, ay + 4, 2, 8)
        pygame.draw.rect(surface, COLOR_APPLE, h_bar)
        pygame.draw.rect(surface, COLOR_APPLE, v_bar)

def draw_ui(surface, snake, hi_score):
    ui_rect = pygame.Rect(0, GAME_HEIGHT, SCREEN_WIDTH, UI_HEIGHT)
    pygame.draw.rect(surface, COLOR_BLACK, ui_rect)
    
    font = pygame.font.SysFont("monospace", 22, bold=True)
    
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
    pygame.draw.rect(surface, COLOR_BORDER, (0, 0, SCREEN_WIDTH, MARGIN))
    pygame.draw.rect(surface, COLOR_BORDER, (0, GAME_HEIGHT - MARGIN, SCREEN_WIDTH, MARGIN))
    pygame.draw.rect(surface, COLOR_BORDER, (0, 0, MARGIN, GAME_HEIGHT))
    pygame.draw.rect(surface, COLOR_BORDER, (SCREEN_WIDTH - MARGIN, 0, MARGIN, GAME_HEIGHT))
    
    gap_width = 80
    pygame.draw.rect(surface, COLOR_BLACK, (SCREEN_WIDTH // 2 - gap_width // 2, GAME_HEIGHT - MARGIN, gap_width, MARGIN))
    pygame.draw.rect(surface, (255, 0, 255), (SCREEN_WIDTH // 2 - gap_width // 2, GAME_HEIGHT - MARGIN + 4, 10, 8))
    pygame.draw.rect(surface, (255, 0, 255), (SCREEN_WIDTH // 2 + gap_width // 2 - 10, GAME_HEIGHT - MARGIN + 4, 10, 8))

def draw_walls(surface, walls):
    for w in walls:
        sx = w[0] * GRID_SIZE + MARGIN
        sy = w[1] * GRID_SIZE + MARGIN
        r = pygame.Rect(sx, sy, GRID_SIZE, GRID_SIZE)
        # Apple II walls often have a textured or dotted look, but solid is fine for now
        pygame.draw.rect(surface, COLOR_WALL, r)
        pygame.draw.rect(surface, COLOR_BLACK, r, 1)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Byte Clone")

    level_manager = LevelManager()
    snake = Snake()
    apple = Apple()
    walls = level_manager.get_walls(snake.level)
    apple.randomize_position(snake.positions, walls)
    
    hi_score = 0
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if snake.snakes_left > 0:
                        snake.reset_level()
                        game_over = False
                    else:
                        snake.reset_game()
                        game_over = False
                        walls = level_manager.get_walls(snake.level)
                        apple.randomize_position(snake.positions, walls)
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
            if snake.move(walls):
                snake.snakes_left -= 1
                game_over = True
                if snake.score > hi_score:
                    hi_score = snake.score
            
            if snake.get_head_position() == apple.position:
                snake.length += 1
                snake.score += snake.value
                snake.apples_left -= 1
                if snake.apples_left <= 0:
                    snake.level += 1
                    if snake.level > 20:
                        snake.level = 1 # Loop back or win
                    snake.apples_left = 10
                    walls = level_manager.get_walls(snake.level)
                    snake.reset_level()
                apple.randomize_position(snake.positions, walls)

        screen.fill(COLOR_BLACK)
        
        draw_border(screen)
        draw_walls(screen, walls)
        snake.draw(screen)
        apple.draw(screen)
        draw_ui(screen, snake, hi_score)
        
        if game_over:
            font = pygame.font.SysFont("monospace", 40, bold=True)
            if snake.snakes_left > 0:
                msg = "CRASHED! PRESS ANY KEY"
            else:
                msg = "GAME OVER! PRESS ANY KEY"
            text = font.render(msg, True, COLOR_WHITE)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, GAME_HEIGHT // 2))

        pygame.display.flip()
        clock.tick(10 + (snake.level)) # Gradually increase speed

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
