from enum import Enum

from src import console


class Board:

    class Block(Enum):
        WALL = -1
        EMPTY = 0
        PUT = 1

    class Display:
        BLOCK = "■"
        WALL = "□"

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._board = []
        self._board += [[self.Block.EMPTY] * (width + 2)]
        self._board += [[self.Block.WALL] +
                        [self.Block.EMPTY] * width +
                        [self.Block.WALL] for _ in range(height)]
        self._board += [[self.Block.WALL] * (width + 2)]
        console.cursor_hyde()

    def __del__(self):
        console.cursor_show()

    def put_mino(self, mino):
        for pos in mino.abs_pos:
            if self._board[pos[1] + 1][pos[0] + 1] != self.Block.EMPTY:
                return False
        for pos in mino.abs_pos:
            self._board[pos[1] + 1][pos[0] + 1] = self.Block.PUT
        return True

    def clear_mino(self, mino):
        for pos in mino.abs_pos:
            self._board[pos[1] + 1][pos[0] + 1] = self.Block.EMPTY

    def clear_line(self):
        for i in range(len(self._board) - 1, 0, -1):
            n_empty = sum([1 for j in range(1, self._width + 1)
                           if self._board[i][j] == self.Block.PUT])
            if n_empty < self._width:
                continue
            for j in range(i, 0, -1):
                for k in range(1, self._width + 1):
                    self._board[j][k] = self._board[j - 1][k]

    def draw(self, is_gameover=False):
        def convert(x):
            if x == self.Block.WALL:
                return f"{self.Display.WALL} "
            elif x == self.Block.PUT:
                return f"{self.Display.BLOCK} "
            else:
                return "  "

        def gameover_message():
            message = "<G A M E  O V E R!>"
            return f"{self.Display.WALL} {message} {self.Display.WALL}"

        for i, line in enumerate(self._board):
            if not is_gameover or i != self._height // 2:
                display_line = [convert(token) for token in line]
            else:
                display_line = gameover_message()
            print("".join(display_line))

        console.cursor_up(len(self._board))
