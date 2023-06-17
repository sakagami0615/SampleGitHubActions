import random


class Tetromino:

    def __init__(self, pattern, spawn_pos):
        self._rot = 0
        self._pos = spawn_pos
        self._pattern = pattern
        self._n_pattern = len(pattern)

    def move(self, dist):
        self._pos = tuple([a + b for a, b in zip(self._pos, dist)])

    def rotate(self, rot):
        self._rot = (self._rot + rot) % self._n_pattern

    @property
    def abs_pos(self):
        pos_list = []
        for rel_pos in self._pattern[self._rot]:
            abs_pos = tuple([a + b for a, b in zip(self._pos, rel_pos)])
            pos_list.append(abs_pos)
        return pos_list

    @property
    def rel_pos(self):
        return self._pattern[self._rot]


class TetrominoGenerator:

    def __init__(self):
        # (x, y) rel pos list
        self._pattern_list = [
            # O
            # □ □ □ □
            # □ * ■ □
            # □ ■ ■ □
            # □ □ □ □
            [
                [(0, 0), (1, 0), (0, 1), (1, 1)],
            ],
            # I
            # □ □ □ □ | □ ■ □ □
            # ■ * ■ ■ | □ * □ □
            # □ □ □ □ | □ ■ □ □
            # □ □ □ □ | □ ■ □ □
            [
                [(0, 0), (-1, 0), (1, 0), (2, 0)],
                [(0, 0), (0, -1), (0, 1), (0, 2)],
            ],
            # S
            # □ □ □ □ | □ ■ □ □
            # ■ * □ □ | ■ * □ □
            # □ ■ ■ □ | ■ □ □ □
            # □ □ □ □ | □ □ □ □
            [
                [(0, 0), (-1, 0), (0, 1), (1, 1)],
                [(0, 0), (0, -1), (-1, 0), (-1, 1)],
            ],
            # Z
            # □ □ □ □ | ■ □ □ □
            # □ * ■ □ | ■ * □ □
            # ■ ■ □ □ | □ ■ □ □
            # □ □ □ □ | □ □ □ □
            [
                [(0, 0), (-1, 1), (0, 1), (1, 0)],
                [(0, 0), (-1, -1), (-1, 0), (0, 1)],
            ],
            # L
            # □ □ □ □ | □ □ □ □ | □ □ □ □ | □ □ □ □
            # □ * ■ □ | □ * □ □ | □ * □ □ | ■ * □ □
            # ■ ■ ■ □ | □ ■ □ □ | ■ ■ ■ □ | □ ■ □ □
            # □ □ □ □ | □ ■ ■ □ | ■ □ □ □ | □ ■ □ □
            [
                [(-1, 1), (0, 1), (1, 1), (1, 0)],
                [(0, 0), (0, 1), (0, 2), (1, 2)],
                [(-1, 1), (-1, 2), (0, 1), (1, 1)],
                [(0, 0), (-1, 0), (0, 1), (0, 2)],
            ],
            # J
            # □ □ □ □ | □ □ □ □ | □ □ □ □ | □ □ □ □
            # ■ * □ □ | □ * ■ □ | □ * □ □ | □ * □ □
            # ■ ■ ■ □ | □ ■ □ □ | ■ ■ ■ □ | □ ■ □ □
            # □ □ □ □ | □ ■ □ □ | □ □ ■ □ | ■ ■ □ □
            [
                [(-1, 0), (-1, 1), (0, 1), (1, 1)],
                [(0, 0), (0, 1), (0, 2), (1, 0)],
                [(-1, 1), (0, 1), (1, 1), (1, 2)],
                [(0, 0), (0, 1), (0, 2), (-1, 2)],
            ],
            # T
            # □ □ □ □ | □ □ □ □ | □ □ □ □ | □ □ □ □
            # □ * □ □ | □ * □ □ | □ * □ □ | □ * □ □
            # ■ ■ ■ □ | □ ■ ■ □ | ■ ■ ■ □ | ■ ■ □ □
            # □ □ □ □ | □ ■ □ □ | □ ■ □ □ | □ ■ □ □
            [
                [(0, 0), (-1, 1), (0, 1), (1, 1)],
                [(0, 0), (0, 1), (0, 2), (1, 1)],
                [(-1, 1), (0, 1), (0, 2), (1, 1)],
                [(0, 0), (-1, 1), (0, 1), (0, 2)],
            ],
        ]
        self._n_patterns = len(self._pattern_list)

    def _create(self, mino_id, spawn_pos):
        if mino_id < 0 or mino_id >= self._n_patterns:
            raise IndexError
        return Tetromino(self._pattern_list[mino_id], spawn_pos)

    def generate(self, spawn_pos):
        mino_id = random.randint(0, self._n_patterns - 1)
        return self._create(mino_id, spawn_pos)
