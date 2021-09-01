import backend2048

game2048 = backend2048.gameboard('test')


def test_slam_left():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 4]]

    game2048.slam_left()

    assert game2048.gameboard == [[2, 2, 0, 0],
                                  [8, 0, 0, 0],
                                  [4, 0, 0, 0],
                                  [2, 4, 0, 0]]

def test_compress_left():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.compress_left()

    assert game2048.gameboard == [[2, 0, 2, 0],
                                  [0, 0, 0, 8],
                                  [4, 0, 0, 0],
                                  [0, 0, 4, 0]]


def test_transpose():

    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 4]]
    game2048.transpose()
    assert game2048.gameboard == [[2, 0, 4, 0],
                                  [0, 0, 0, 0],
                                  [2, 0, 0, 2],
                                  [0, 8, 0, 4]]

def test_reverse():

    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 4]]

    game2048.reverse()

    assert game2048.gameboard == [[0, 2, 0, 2],
                                  [8, 0, 0, 0],
                                  [0, 0, 0, 4],
                                  [4, 2, 0, 0]]

def test_move_left():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.move_left()
    
    assert game2048.gameboard == [[4, 0, 0, 0],
                                  [8, 0, 0, 0],
                                  [4, 0, 0, 0],
                                  [4, 0, 0, 0]]


def test_move_up():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.move_up()

    assert game2048.gameboard == [[2, 0, 4, 8],
                                  [4, 0, 0, 2],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0]]


def test_move_right():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.move_right()

    assert game2048.gameboard == [[0, 0, 0, 4],
                                  [0, 0, 0, 8],
                                  [0, 0, 0, 4],
                                  [0, 0, 0, 4]]


def test_move_down():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.move_down()

    assert game2048.gameboard == [[0, 0, 0, 0],
                                  [0, 0, 0, 0],
                                  [2, 0, 0, 8],
                                  [4, 0, 4, 2]]

def test_scoring():
    game2048.score = 0
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.move_left()

    assert game2048.score == 8

def test_is_game_over():

    game2048.gameboard = [[2048, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    assert game2048.is_game_over() is True

def test_is_game_not_over():
    game2048.gameboard = [[16, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]
    
    assert game2048.is_game_over() is False
