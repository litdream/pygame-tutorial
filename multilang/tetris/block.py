class Block:
    def __init__(self, shape, color):
        self.shape = shape  # List of lists representing the block's current orientation
        self.color = color
        self.rotation = 0  # Current rotation state index
        self.x = 0  # Top-left x-coordinate on the stage
        self.y = 0  # Top-left y-coordinate on the stage

    def get_shape_coordinates(self):
        """Returns the global coordinates of the block's occupied cells on the stage."""
        coords = []
        for r_idx, row in enumerate(self.shape):
            for c_idx, cell in enumerate(row):
                if cell == 'X':  # 'X' denotes an occupied cell
                    coords.append((self.x + c_idx, self.y + r_idx))
        return coords

    def rotate(self):
        """Rotates the block to its next orientation."""
        # This method will be overridden by subclasses with specific shapes and rotations
        pass

class IBlock(Block):
    SHAPES = [
        [['.', 'X', '.', '.'],
         ['.', 'X', '.', '.'],
         ['.', 'X', '.', '.'],
         ['.', 'X', '.', '.']],

        [['.', '.', '.', '.'],
         ['X', 'X', 'X', 'X'],
         ['.', '.', '.', '.'],
         ['.', '.', '.', '.']]
    ]

    def __init__(self):
        super().__init__(self.SHAPES[0], "cyan")

    def rotate(self):
        self.rotation = (self.rotation - 1) % len(self.SHAPES)
        self.shape = self.SHAPES[self.rotation]

class OBlock(Block):
    SHAPES = [
        [['X', 'X'],
         ['X', 'X']]
    ]

    def __init__(self):
        super().__init__(self.SHAPES[0], "yellow")

    def rotate(self):
        # OBlock does not rotate
        pass

class TBlock(Block):
    SHAPES = [
        [['.', 'X', '.'],
         ['X', 'X', 'X'],
         ['.', '.', '.']],

        [['.', 'X', '.'],
         ['.', 'X', 'X'],
         ['.', 'X', '.']],

        [['.', '.', '.'],
         ['X', 'X', 'X'],
         ['.', 'X', '.']],

        [['.', 'X', '.'],
         ['X', 'X', '.'],
         ['.', 'X', '.']]
    ]

    def __init__(self):
        super().__init__(self.SHAPES[0], "purple")

    def rotate(self):
        self.rotation = (self.rotation - 1) % len(self.SHAPES)
        self.shape = self.SHAPES[self.rotation]

class JBlock(Block):
    SHAPES = [
        [['X', '.', '.'],
         ['X', 'X', 'X'],
         ['.', '.', '.']],

        [['.', 'X', 'X'],
         ['.', 'X', '.'],
         ['.', 'X', '.']],

        [['.', '.', '.'],
         ['X', 'X', 'X'],
         ['.', '.', 'X']],

        [['.', 'X', '.'],
         ['.', 'X', '.'],
         ['X', 'X', '.']]
    ]

    def __init__(self):
        super().__init__(self.SHAPES[0], "blue")

    def rotate(self):
        self.rotation = (self.rotation - 1) % len(self.SHAPES)
        self.shape = self.SHAPES[self.rotation]

class LBlock(Block):
    SHAPES = [
        [['.', '.', 'X'],
         ['X', 'X', 'X'],
         ['.', '.', '.']],

        [['.', 'X', '.'],
         ['.', 'X', '.'],
         ['.', 'X', 'X']],

        [['.', '.', '.'],
         ['X', 'X', 'X'],
         ['X', '.', '.']],

        [['X', 'X', '.'],
         ['.', 'X', '.'],
         ['.', 'X', '.']]
    ]

    def __init__(self):
        super().__init__(self.SHAPES[0], "orange")

    def rotate(self):
        self.rotation = (self.rotation - 1) % len(self.SHAPES)
        self.shape = self.SHAPES[self.rotation]

class SBlock(Block):
    SHAPES = [
        [['.', 'X', 'X'],
         ['X', 'X', '.'],
         ['.', '.', '.']],

        [['.', 'X', '.'],
         ['.', 'X', 'X'],
         ['.', '.', 'X']]
    ]

    def __init__(self):
        super().__init__(self.SHAPES[0], "green")

    def rotate(self):
        self.rotation = (self.rotation - 1) % len(self.SHAPES)
        self.shape = self.SHAPES[self.rotation]

class ZBlock(Block):
    SHAPES = [
        [['X', 'X', '.'],
         ['.', 'X', 'X'],
         ['.', '.', '.']],

        [['.', '.', 'X'],
         ['.', 'X', 'X'],
         ['.', 'X', '.']]
    ]

    def __init__(self):
        super().__init__(self.SHAPES[0], "red")

    def rotate(self):
        self.rotation = (self.rotation - 1) % len(self.SHAPES)
        self.shape = self.SHAPES[self.rotation]
