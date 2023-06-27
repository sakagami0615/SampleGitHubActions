import time
from dataclasses import dataclass
from copy import deepcopy

from src.tetris.tetromino import TetrominoGenerator
from src.tetris.board import Board
from src.tetris.setting import FPS

try:
    from src.tetris.key_windows import getkey
except ImportError:
    from src.tetris.key_unix import getkey


def fps_decorator(func):
    def wrapper(*args, **kwargs):
        begin_time = time.perf_counter()
        func(*args, **kwargs)
        while time.perf_counter() - begin_time < 1 / FPS:
            pass
    return wrapper


@dataclass
class TetrisParam:
    WIDTH: int = 10
    HEIGHT: int = 20
    SPAWN_POS: tuple = (4, 0)
    FALL_CYCLE_FRAME: int = 20
    KEY_CYCLE_FRAME: int = 10
    KEY_MOVE_LEFT: int = 97     # a (ascii code)
    KEY_MOVE_RIGHT: int = 100   # d (ascii code)
    KEY_MOVE_DOWN: int = 115    # s (ascii code)
    KEY_ROTATE: int = 119       # w (ascii code)


class Tetris(TetrisParam):

    def __init__(self):
        super(Tetris, self).__init__()

        self._generator = TetrominoGenerator()
        self._board = Board(self.WIDTH, self.HEIGHT)

        self._curr_mino = None
        self._is_continue = True

        self._fall_frame_cnt = 0
        self._key_frame_cnt = 0
        self._fall_available = False
        self._key_available = True

    def _spawn_mino(self):
        if self._curr_mino is None:
            self._curr_mino = self._generator.generate(self.SPAWN_POS)
            if not self._board.put_mino(self._curr_mino):
                self._is_continue = False
            self._fall_frame_cnt = 0

    def _move_mino(self, pos):
        prev_mino = deepcopy(self._curr_mino)
        self._board.clear_mino(self._curr_mino)
        self._curr_mino.move(pos)
        if not self._board.put_mino(self._curr_mino):
            self._board.put_mino(prev_mino)
            self._curr_mino = prev_mino
            return False
        else:
            return True

    def _rotate_mino(self, rot):
        prev_mino = deepcopy(self._curr_mino)
        self._board.clear_mino(self._curr_mino)
        self._curr_mino.rotate(rot)
        if not self._board.put_mino(self._curr_mino):
            self._board.put_mino(prev_mino)
            self._curr_mino = prev_mino
            return False
        else:
            return True

    def _fall_mino(self):
        if not self._move_mino((0, 1)):
            self._board.clear_line()
            self._curr_mino = None

        self._fall_frame_cnt = 0
        self._fall_available = False

    def _control_mino(self):
        key = getkey()
        if key == self.KEY_MOVE_LEFT:
            self._move_mino((-1, 0))
        elif key == self.KEY_MOVE_RIGHT:
            self._move_mino((1, 0))
        elif key == self.KEY_ROTATE:
            self._rotate_mino(1)
        elif key == self.KEY_MOVE_DOWN:
            self._fall_mino()
        self._key_available = False

    def _update(self):
        if not self._key_available:
            self._key_frame_cnt += 1
            if self._key_frame_cnt % self.KEY_CYCLE_FRAME == 0:
                self._key_available = True
                self._key_frame_cnt = 0

        self._fall_frame_cnt += 1
        if self._fall_frame_cnt % self.FALL_CYCLE_FRAME == 0:
            self._fall_available = True
            self._fall_frame_cnt = 0

    @fps_decorator
    def _process(self):
        # calculate
        if self._curr_mino is None:
            self._spawn_mino()
        else:
            if self._key_available:
                self._control_mino()
            if self._fall_available:
                self._fall_mino()
        # draw
        self._board.draw()
        # update
        self._update()

    def exec(self):
        while self._is_continue:
            self._process()
        self._board.draw("GAME OVER!")
