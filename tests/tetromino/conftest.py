import pytest

from operator import add
from tetris.tetromino import TetrominoGenerator


@pytest.fixture(scope="function")
def mino_generator():
    return TetrominoGenerator()


@pytest.fixture(scope="function")
def create_mino():
    def _create_mino(mino_id, spawn_pos=(0, 0)):
        gen = TetrominoGenerator()
        return gen._create(mino_id, spawn_pos)
    return _create_mino


@pytest.fixture(scope="function")
def pos_to_pattern():
    def _pos_to_pattern(pos_list, pattern_size=(4, 4), offset=(1, 1)):
        pattern_map = [["□"] * pattern_size[0] for _ in range(pattern_size[1])]
        for pos in pos_list:
            pos = tuple(map(add, pos, offset))
            pattern_map[pos[1]][pos[0]] = "■"

        return tuple([" ".join(line) for line in pattern_map])
    return _pos_to_pattern


@pytest.fixture(scope="function")
def pattern_o_mino():
    return [("□ □ □ □",
             "□ ■ ■ □",
             "□ ■ ■ □",
             "□ □ □ □")]


@pytest.fixture(scope="function")
def pattern_i_mino():
    return [("□ □ □ □",
             "■ ■ ■ ■",
             "□ □ □ □",
             "□ □ □ □"),
            ("□ ■ □ □",
             "□ ■ □ □",
             "□ ■ □ □",
             "□ ■ □ □"),]


@pytest.fixture(scope="function")
def pattern_s_mino():
    return [("□ □ □ □",
             "■ ■ □ □",
             "□ ■ ■ □",
             "□ □ □ □"),
            ("□ ■ □ □",
             "■ ■ □ □",
             "■ □ □ □",
             "□ □ □ □"),]


@pytest.fixture(scope="function")
def pattern_z_mino():
    return [("□ □ □ □",
             "□ ■ ■ □",
             "■ ■ □ □",
             "□ □ □ □"),
            ("■ □ □ □",
             "■ ■ □ □",
             "□ ■ □ □",
             "□ □ □ □"),]


@pytest.fixture(scope="function")
def pattern_l_mino():
    return [("□ □ □ □",
             "□ □ ■ □",
             "■ ■ ■ □",
             "□ □ □ □"),
            ("□ □ □ □",
             "□ ■ □ □",
             "□ ■ □ □",
             "□ ■ ■ □"),
            ("□ □ □ □",
             "□ □ □ □",
             "■ ■ ■ □",
             "■ □ □ □"),
            ("□ □ □ □",
             "■ ■ □ □",
             "□ ■ □ □",
             "□ ■ □ □"),]


@pytest.fixture(scope="function")
def pattern_j_mino():
    return [("□ □ □ □",
             "■ □ □ □",
             "■ ■ ■ □",
             "□ □ □ □"),
            ("□ □ □ □",
             "□ ■ ■ □",
             "□ ■ □ □",
             "□ ■ □ □"),
            ("□ □ □ □",
             "□ □ □ □",
             "■ ■ ■ □",
             "□ □ ■ □"),
            ("□ □ □ □",
             "□ ■ □ □",
             "□ ■ □ □",
             "■ ■ □ □"),]


@pytest.fixture(scope="function")
def pattern_t_mino():
    return [("□ □ □ □",
             "□ ■ □ □",
             "■ ■ ■ □",
             "□ □ □ □"),
            ("□ □ □ □",
             "□ ■ □ □",
             "□ ■ ■ □",
             "□ ■ □ □"),
            ("□ □ □ □",
             "□ □ □ □",
             "■ ■ ■ □",
             "□ ■ □ □"),
            ("□ □ □ □",
             "□ ■ □ □",
             "■ ■ □ □",
             "□ ■ □ □"),]
