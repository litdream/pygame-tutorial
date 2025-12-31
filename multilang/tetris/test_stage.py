from tetris.stage import Stage
from tetris.block import IBlock, OBlock

def test_stage_initialization():
    stage = Stage(10, 20)
    assert stage.width == 10
    assert stage.height == 20
    assert len(stage.grid) == 20
    assert len(stage.grid[0]) == 10
    for row in stage.grid:
        for cell in row:
            assert cell == '.'

def test_stage_str_representation():
    stage = Stage(2, 2)
    expected_str = ". .\n. ."
    assert str(stage) == expected_str

def test_is_valid_position_empty_stage():
    stage = Stage(10, 20)
    block = IBlock()
    assert stage.is_valid_position(block, 0, 0)

    # Test out of bounds (right)
    # For IBlock (vertical bar), 'X' is at c_idx=1. So x=9 means actual block cell at 9+1=10, which is out of bounds.
    assert not stage.is_valid_position(block, 9, 0)

    # Test out of bounds (bottom)
    assert not stage.is_valid_position(block, 0, 17) # IBlock is 4 units high, 17 + 4 = 21 > 20

def test_is_valid_position_collision():
    stage = Stage(10, 20)
    block1 = OBlock()
    stage.add_block(block1, 0, 18) # Place a block at the bottom left

    block2 = IBlock()
    # Try to place block2 overlapping block1
    assert not stage.is_valid_position(block2, 0, 17) # Overlaps with OBlock at (0,18) (0,19)

def test_add_block():
    stage = Stage(10, 20)
    block = OBlock()
    stage.add_block(block, 0, 0)
    assert stage.grid[0][0] == block.color
    assert stage.grid[0][1] == block.color
    assert stage.grid[1][0] == block.color
    assert stage.grid[1][1] == block.color
    assert stage.grid[0][2] == '.' # Ensure no extra cells are filled

def test_clear_lines_no_clear():
    stage = Stage(10, 4) # Smaller stage for easier testing
    block = OBlock()
    stage.add_block(block, 0, 2) # Place at (0,2) to (1,3)
    assert stage.clear_lines() == 0
    assert stage.grid[0][0] == '.'

def test_clear_lines_single_clear():
    stage = Stage(3, 3)
    # Fill the bottom line
    stage.grid[2] = ['X', 'X', 'X']
    # Fill the middle partially
    stage.grid[1] = ['Y', '.', 'Y']

    lines_cleared = stage.clear_lines()
    assert lines_cleared == 1
    # The middle line should now be the bottom line
    assert stage.grid[2] == ['Y', '.', 'Y']
    # The top line should be empty
    assert stage.grid[0] == ['.', '.', '.']

def test_clear_lines_multiple_clear():
    stage = Stage(3, 4)
    # Fill two bottom lines
    stage.grid[2] = ['X', 'X', 'X']
    stage.grid[3] = ['Y', 'Y', 'Y']
    # Keep one line partially filled at top
    stage.grid[1] = ['Z', '.', 'Z']

    lines_cleared = stage.clear_lines()
    assert lines_cleared == 2
    # The partially filled line should now be at the bottom
    assert stage.grid[3] == ['Z', '.', 'Z']
    # The top two lines should be empty
    assert stage.grid[0] == ['.', '.', '.']
    assert stage.grid[1] == ['.', '.', '.']