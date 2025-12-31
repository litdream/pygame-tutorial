from unittest.mock import patch, MagicMock
from tetris.game import Game
from tetris.block import IBlock, OBlock, TBlock

@patch('tetris.game.Stage')
@patch('random.choice')
def test_game_initialization(mock_random_choice, mock_stage):
    mock_random_choice.side_effect = [OBlock, IBlock]
    game = Game(10, 20)

    mock_stage.assert_called_once_with(10, 20)
    assert isinstance(game.current_block, OBlock)
    assert isinstance(game.next_block, IBlock)
    assert game.score == 0
    assert not game.game_over
    assert game.block_x == 10 // 2 - 1
    assert game.block_y == 0

def test_move_block_valid():
    game = Game(10, 20)
    game.current_block = OBlock()
    game.block_x = 0
    game.block_y = 0
    game._is_valid_move = MagicMock(return_value=True)

    assert game.move_block(1, 0)
    assert game.block_x == 1
    assert game.block_y == 0
    assert game.move_block(0, 1)
    assert game.block_x == 1
    assert game.block_y == 1

def test_move_block_invalid():
    game = Game(10, 20)
    game.current_block = OBlock()
    game.block_x = 0
    game.block_y = 0
    game._is_valid_move = MagicMock(return_value=False)

    assert not game.move_block(1, 0)
    assert game.block_x == 0
    assert game.block_y == 0

def test_rotate_block_valid():
    game = Game(10, 20)
    game.current_block = TBlock()
    initial_shape = game.current_block.shape
    game._is_valid_move = MagicMock(return_value=True)

    assert game.rotate_block()
    assert game.current_block.shape != initial_shape
    assert game.current_block.rotation == 1

def test_rotate_block_invalid():
    game = Game(10, 20)
    game.current_block = TBlock()
    initial_shape = game.current_block.shape
    game._is_valid_move = MagicMock(return_value=False)

    assert not game.rotate_block()
    assert game.current_block.shape == initial_shape
    assert game.current_block.rotation == 0

@patch('random.choice')
def test_drop_block_and_lock(mock_random_choice):
    mock_random_choice.side_effect = [OBlock, IBlock, TBlock]
    game = Game(10, 4)
    game.current_block = OBlock()
    block_to_drop = game.current_block
    game.block_x = 0
    game.block_y = 0
    game.stage.is_valid_position = MagicMock(side_effect=[True, True, False, True])
    game.stage.add_block = MagicMock()
    game.stage.clear_lines = MagicMock(return_value=0)

    game.drop_block()

    # Assert that the block was added at the correct final position (y=2)
    game.stage.add_block.assert_called_once_with(block_to_drop, 0, 2)
    game.stage.clear_lines.assert_called_once()
    assert game.score == 0
    # Assert that the current block is now the *new* block
    assert isinstance(game.current_block, IBlock)

@patch('random.choice')
def test_lock_block_clears_lines_and_scores(mock_random_choice):
    mock_random_choice.side_effect = [OBlock, IBlock, TBlock]
    game = Game(10, 4)
    game.current_block = OBlock()
    game.block_x = 0
    game.block_y = 0
    game.stage.add_block = MagicMock()
    game.stage.clear_lines = MagicMock(return_value=2)

    game._lock_block()
    assert game.score == 200
    assert isinstance(game.current_block, IBlock)

@patch('random.choice')
def test_game_over_condition(mock_random_choice):
    mock_random_choice.side_effect = [OBlock, IBlock, TBlock]
    game = Game(2, 2)
    game.current_block = OBlock()
    game.block_x = 0
    game.block_y = 0
    # This mock should return False to trigger the game over condition in _lock_block
    game._is_valid_move = MagicMock(return_value=False)

    game._lock_block()
    assert game.game_over

def test_update_moves_block():
    game = Game(10, 20)
    game.current_block = OBlock()
    game.block_x = 0
    game.block_y = 0
    game.move_block = MagicMock(return_value=True)
    game._lock_block = MagicMock()

    game.update()
    game.move_block.assert_called_once_with(0, 1)
    game._lock_block.assert_not_called()

def test_update_locks_block():
    game = Game(10, 20)
    game.current_block = OBlock()
    game.block_x = 0
    game.block_y = 0
    game.move_block = MagicMock(return_value=False)
    game._lock_block = MagicMock()

    game.update()
    game.move_block.assert_called_once_with(0, 1)
    game._lock_block.assert_called_once()