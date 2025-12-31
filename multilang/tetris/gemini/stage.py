class Stage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self._create_empty_grid()

    def _create_empty_grid(self):
        """Initializes an empty grid for the stage."""
        return [['.' for _ in range(self.width)] for _ in range(self.height)]

    def is_valid_position(self, block, x, y):
        """Checks if a block can be placed at the given position (x, y)."""
        for r_idx, row in enumerate(block.shape):
            for c_idx, cell in enumerate(row):
                if cell == 'X':
                    stage_x = x + c_idx
                    stage_y = y + r_idx

                    # Check horizontal boundaries
                    if not (0 <= stage_x < self.width):
                        return False

                    # Check vertical boundaries
                    if not (0 <= stage_y < self.height):
                        return False

                    # Check for collision with existing blocks
                    if self.grid[stage_y][stage_x] != '.':
                        return False
        return True

    def add_block(self, block, x, y):
        """Adds a block to the stage at the given position (x, y)."""
        for r_idx, row in enumerate(block.shape):
            for c_idx, cell in enumerate(row):
                if cell == 'X':
                    stage_x = x + c_idx
                    stage_y = y + r_idx
                    if 0 <= stage_x < self.width and 0 <= stage_y < self.height:
                        self.grid[stage_y][stage_x] = block.color

    def clear_lines(self):
        """Checks for and clears any completed lines."""
        new_grid = []
        lines_cleared = 0
        for r_idx in range(self.height):
            if '.' not in self.grid[r_idx]: # Line is full
                lines_cleared += 1
            else:
                new_grid.append(self.grid[r_idx])
        
        # Add empty lines to the top
        for _ in range(lines_cleared):
            new_grid.insert(0, ['.' for _ in range(self.width)])
            
        self.grid = new_grid
        return lines_cleared

    def __str__(self):
        """Returns a string representation of the stage for debugging."""
        return "\n".join([" ".join(row) for row in self.grid])

