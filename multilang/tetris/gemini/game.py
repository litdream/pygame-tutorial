import random
#from tetris.stage import Stage
#from tetris.block import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock
from stage import Stage
from block import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock

class Game:
    def __init__(self, width, height):
        self.stage = Stage(width, height)
        self.current_block = self._new_block()
        self.next_block = self._new_block()
        self.score = 0
        self.game_over = False
        self.block_x = width // 2 - self._get_block_center_offset(self.current_block)
        self.block_y = 0

    def _get_block_center_offset(self, block):
        # For a 4x4 block, the center is roughly at 1.5. If the shape is 3x3, it's 1.
        # This approximation helps center the block initially.
        if len(block.shape) == 4: # IBlock
            return 2 # center IBlock at x - 2 to align with middle of 4x4 bounding box
        elif len(block.shape) == 3: # T,J,L,S,Z Blocks
            return 1 # center 3x3 blocks at x - 1 to align
        else: # OBlock
            return 1 # center 2x2 blocks at x - 1

    def _new_block(self):
        blocks = [IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock]
        return random.choice(blocks)()

    def _is_valid_move(self, block, new_x, new_y):
        return self.stage.is_valid_position(block, new_x, new_y)

    def move_block(self, dx, dy):
        if self.game_over:
            return
        new_x = self.block_x + dx
        new_y = self.block_y + dy
        if self._is_valid_move(self.current_block, new_x, new_y):
            self.block_x = new_x
            self.block_y = new_y
            return True
        return False

    def rotate_block(self):
        if self.game_over:
            return
        original_rotation = self.current_block.rotation
        self.current_block.rotate()
        if not self._is_valid_move(self.current_block, self.block_x, self.block_y):
            # If rotation is invalid, revert to original rotation
            self.current_block.rotation = original_rotation
            self.current_block.shape = self.current_block.SHAPES[original_rotation]
            return False
        return True

    def drop_block(self):
        if self.game_over:
            return
        # Move down until collision
        while self.move_block(0, 1):
            pass
        self._lock_block()

    def _lock_block(self):
        if self.game_over:
            return
        self.stage.add_block(self.current_block, self.block_x, self.block_y)
        lines_cleared = self.stage.clear_lines()
        self.score += lines_cleared * 100 # Simple scoring

        # Check for game over condition (if a new block cannot be placed)
        self.current_block = self.next_block
        self.next_block = self._new_block()
        self.block_x = self.stage.width // 2 - self._get_block_center_offset(self.current_block)
        self.block_y = 0
        if not self._is_valid_move(self.current_block, self.block_x, self.block_y):
            self.game_over = True

    def update(self):
        if self.game_over:
            return
        if not self.move_block(0, 1): # Try to move block down by one
            self._lock_block()

    def __str__(self):
        # Create a temporary grid to show current block position for debugging
        temp_grid = [row[:] for row in self.stage.grid] # Make a copy
        for r_idx, row in enumerate(self.current_block.shape):
            for c_idx, cell in enumerate(row):
                if cell == 'X':
                    stage_x = self.block_x + c_idx
                    stage_y = self.block_y + r_idx
                    if 0 <= stage_x < self.stage.width and 0 <= stage_y < self.stage.height:
                        temp_grid[stage_y][stage_x] = self.current_block.color
        return "\n".join([" ".join(row) for row in temp_grid])
