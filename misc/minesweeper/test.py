import minesweeper as ms

class TestGame:
    def test_generate_board(self):
        b3x3 = ms.Game.generate_board(3, 3, 0)
        assert b3x3 == [[0,0,0],[0,0,0],[0,0,0]]
        b3x1 = ms.Game.generate_board(3, 1, 0)
        assert b3x1 == [[0,0,0]]
        b1x3 = ms.Game.generate_board(1, 3, 0)
        assert b1x3 == [[0],[0],[0]]
        b3x3_mines = ms.Game.generate_board(3, 3, 1)
        assert b3x3_mines == [[1,1,1],[1,1,1],[1,1,1]]

