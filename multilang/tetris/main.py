import pygame
from game import Game

# --- constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = {
    "cyan": (0, 255, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128),
    "blue": (0, 0, 255),
    "orange": (255, 165, 0),
    "green": (0, 255, 0),
    "red": (255, 0, 0),
}
CELL_SIZE = 40
STAGE_WIDTH = 10
STAGE_HEIGHT = 20
SIDEBAR_WIDTH = 5  # Width of the sidebar in cells
SCREEN_WIDTH = CELL_SIZE * (STAGE_WIDTH + SIDEBAR_WIDTH)
SCREEN_HEIGHT = CELL_SIZE * STAGE_HEIGHT

# --- functions ---

def draw_grid(screen, stage):
    # Draw grid for the main stage area only
    for y in range(stage.height):
        for x in range(stage.width):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

def draw_sidebar(screen):
    # Draw a line to separate the stage from the sidebar
    sidebar_x = STAGE_WIDTH * CELL_SIZE
    pygame.draw.line(screen, WHITE, (sidebar_x, 0), (sidebar_x, SCREEN_HEIGHT), 2)
    
    # Display "Next" text
    font = pygame.font.Font(None, 36)
    text = font.render("Next", True, WHITE)
    screen.blit(text, (sidebar_x + 30, 20))

def draw_stage(screen, stage):
    for y in range(stage.height):
        for x in range(stage.width):
            cell = stage.grid[y][x]
            if cell != '.':
                color = COLORS.get(cell, WHITE)
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect)

def draw_block(screen, block, x, y):
    for r_idx, row in enumerate(block.shape):
        for c_idx, cell in enumerate(row):
            if cell == 'X':
                color = COLORS.get(block.color, WHITE)
                rect = pygame.Rect((x + c_idx) * CELL_SIZE, (y + r_idx) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect)

def main():
    pygame.init()
    # Disable Pygame's built-in key repeat
    pygame.key.set_repeat(0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    game = Game(STAGE_WIDTH, STAGE_HEIGHT)
    fall_time = 0
    fall_speed = 500  # milliseconds

    # Custom key repeat variables
    key_left_pressed = False
    key_right_pressed = False
    key_down_pressed = False # Add key down to repeat as well
    last_horizontal_move_time = 0
    last_down_move_time = 0
    initial_repeat_delay = 200 # milliseconds for first repeat
    repeat_interval = 80 # milliseconds for subsequent repeats

    running = True
    while running:
        screen.fill(BLACK)
        
        delta_time = clock.tick(60)
        current_time = pygame.time.get_ticks() # Get current time in milliseconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_block(-1, 0)
                    key_left_pressed = True
                    last_horizontal_move_time = current_time # Record initial move time
                if event.key == pygame.K_RIGHT:
                    game.move_block(1, 0)
                    key_right_pressed = True
                    last_horizontal_move_time = current_time # Record initial move time
                if event.key == pygame.K_DOWN:
                    game.move_block(0, 1)
                    key_down_pressed = True
                    last_down_move_time = current_time
                if event.key == pygame.K_UP:
                    game.rotate_block()
                if event.key == pygame.K_SPACE:
                    game.drop_block()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    key_left_pressed = False
                if event.key == pygame.K_RIGHT:
                    key_right_pressed = False
                if event.key == pygame.K_DOWN:
                    key_down_pressed = False

        # Custom key repeat logic for horizontal movement
        if key_left_pressed or key_right_pressed:
            # Check if initial delay has passed or if it's time for a repeat
            if current_time - last_horizontal_move_time > initial_repeat_delay:
                # If enough time has passed, attempt to move and reset timer
                if key_left_pressed and game.move_block(-1, 0):
                    last_horizontal_move_time = current_time - initial_repeat_delay + repeat_interval # Adjusted for smoother repeat
                elif key_right_pressed and game.move_block(1, 0):
                    last_horizontal_move_time = current_time - initial_repeat_delay + repeat_interval

        # Custom key repeat logic for fast down movement
        if key_down_pressed:
            if current_time - last_down_move_time > initial_repeat_delay:
                if game.move_block(0, 1):
                    last_down_move_time = current_time - initial_repeat_delay + repeat_interval

        fall_time += delta_time
        if fall_time >= fall_speed:
            fall_time = 0
            game.update()

        if game.game_over:
            # You can add a game over screen here
            running = False

        draw_stage(screen, game.stage)
        draw_block(screen, game.current_block, game.block_x, game.block_y)
        draw_grid(screen, game.stage)
        draw_sidebar(screen)
        # Draw the next block in the sidebar
        draw_block(screen, game.next_block, STAGE_WIDTH + 1, 2)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

