from tetris.block import IBlock, OBlock, TBlock

def test_iblock_initialization():
    block = IBlock()
    assert block.color == "cyan"
    assert block.rotation == 0
    assert block.shape == [
        ['.', 'X', '.', '.'],
        ['.', 'X', '.', '.'],
        ['.', 'X', '.', '.'],
        ['.', 'X', '.', '.']
    ]

def test_iblock_rotation():
    block = IBlock()
    block.rotate()
    assert block.rotation == 1
    assert block.shape == [
        ['.', '.', '.', '.'],
        ['X', 'X', 'X', 'X'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.']
    ]
    block.rotate()
    assert block.rotation == 0 # Cycles back to initial

def test_oblock_initialization():
    block = OBlock()
    assert block.color == "yellow"
    assert block.rotation == 0
    assert block.shape == [
        ['X', 'X'],
        ['X', 'X']
    ]

def test_oblock_rotation():
    block = OBlock()
    block.rotate()  # Should not change
    assert block.rotation == 0
    assert block.shape == [
        ['X', 'X'],
        ['X', 'X']
    ]

def test_tblock_initialization():
    block = TBlock()
    assert block.color == "purple"
    assert block.rotation == 0
    assert block.shape == [
        ['.', 'X', '.'],
        ['X', 'X', 'X'],
        ['.', '.', '.']
    ]

def test_tblock_rotation():
    block = TBlock()
    block.rotate()
    assert block.rotation == 1
    assert block.shape == [
        ['.', 'X', '.'],
        ['.', 'X', 'X'],
        ['.', 'X', '.']
    ]
    block.rotate()
    assert block.rotation == 2
    assert block.shape == [
        ['.', '.', '.'],
        ['X', 'X', 'X'],
        ['.', 'X', '.']
    ]
    block.rotate()
    assert block.rotation == 3
    assert block.shape == [
        ['.', 'X', '.'],
        ['X', 'X', '.'],
        ['.', 'X', '.']
    ]
    block.rotate()
    assert block.rotation == 0 # Cycles back to initial

def test_get_shape_coordinates():
    block = IBlock()
    block.x = 1
    block.y = 0
    # Initial IBlock shape: X at (1,0), (1,1), (1,2), (1,3) relative to block's internal shape matrix
    # Global coordinates when block.x=1, block.y=0: (1+1, 0+0), (1+1, 0+1), (1+1, 0+2), (1+1, 0+3)
    expected_coords = [(2,0), (2,1), (2,2), (2,3)]
    assert sorted(block.get_shape_coordinates()) == sorted(expected_coords)

    block.rotate() # Horizontal IBlock
    block.x = 0
    block.y = 1
    # Rotated IBlock shape: X at (0,1), (1,1), (2,1), (3,1) relative to block's internal shape matrix
    # Global coordinates when block.x=0, block.y=1: (0+0, 1+1), (0+1, 1+1), (0+2, 1+1), (0+3, 1+1)
    expected_coords = [(0,2), (1,2), (2,2), (3,2)]
    assert sorted(block.get_shape_coordinates()) == sorted(expected_coords)