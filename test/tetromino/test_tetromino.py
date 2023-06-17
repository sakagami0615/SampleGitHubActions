import pytest


@pytest.mark.parametrize("test_mino_id, expect_pattern", [
        (0, "pattern_o_mino"),
        (1, "pattern_i_mino"),
        (2, "pattern_s_mino"),
        (3, "pattern_z_mino"),
        (4, "pattern_l_mino"),
        (5, "pattern_j_mino"),
        (6, "pattern_t_mino"),
])
def test_tetromino_pattern(request, create_mino, pos_to_pattern, test_mino_id, expect_pattern):
    test_mino = create_mino(test_mino_id)
    test_pattern = [pos_to_pattern(p) for p in test_mino._pattern]
    assert test_pattern == request.getfixturevalue(expect_pattern)


@pytest.mark.parametrize("test_init_pos, test_move_dist, expect_pos", [
        ((5, 1), (-1, 0), (4, 1)),
        ((5, 1), (1, 0), (6, 1)),
        ((5, 1), (0, 1), (5, 2)),
])
def test_tetromino_move(create_mino, test_init_pos, test_move_dist, expect_pos):
    test_mino = create_mino(0, test_init_pos)
    test_mino.move(test_move_dist)
    assert test_mino._pos == expect_pos


@pytest.mark.parametrize("test_mino_id, test_rot, expect_pattern", [
        # check o mino rotate
        (0,  1, "pattern_o_mino"),
        (0, -1, "pattern_o_mino"),
        # check i mino rotate
        (1,  1, "pattern_i_mino"),
        (1, -1, "pattern_i_mino"),
        (1,  2, "pattern_i_mino"),
        (1, -2, "pattern_i_mino"),
        # check s mino rotate
        (2,  1, "pattern_s_mino"),
        (2, -1, "pattern_s_mino"),
        (2,  2, "pattern_s_mino"),
        (2, -2, "pattern_s_mino"),
        # check z mino rotate
        (3,  1, "pattern_z_mino"),
        (3, -1, "pattern_z_mino"),
        (3,  2, "pattern_z_mino"),
        (3, -2, "pattern_z_mino"),
        # check l mino rotate
        (4, -1, "pattern_l_mino"),
        (4,  1, "pattern_l_mino"),
        (4, -4, "pattern_l_mino"),
        (4,  4, "pattern_l_mino"),
        # check j mino rotate
        (5, -1, "pattern_j_mino"),
        (5,  1, "pattern_j_mino"),
        (5, -4, "pattern_j_mino"),
        (5,  4, "pattern_j_mino"),
        # check t mino rotate
        (6, -1, "pattern_t_mino"),
        (6,  1, "pattern_t_mino"),
        (6, -4, "pattern_t_mino"),
        (6,  4, "pattern_t_mino"),
])
def test_tetromino_rotate(request, create_mino, pos_to_pattern, test_mino_id, test_rot, expect_pattern):
    test_mino = create_mino(test_mino_id)
    test_mino.rotate(test_rot)

    test_pattern = pos_to_pattern(test_mino.rel_pos)
    assert test_pattern == request.getfixturevalue(expect_pattern)[test_mino._rot]
