'''to test backend2048.py'''

import backend2048

game2048 = backend2048.Gameboard('test')
#print(game2048.__module__)

def test_slam_left():
    '''testing slam left'''

    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 4]]

    game2048._Gameboard__slam_left()

    assert game2048.gameboard == [[2, 2, 0, 0],
                                  [8, 0, 0, 0],
                                  [4, 0, 0, 0],
                                  [2, 4, 0, 0]]

def test_compress_left():
    '''testing compress left'''

    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048._Gameboard__compress_left()

    assert game2048.gameboard == [[2, 0, 2, 0],
                                  [0, 0, 0, 8],
                                  [4, 0, 0, 0],
                                  [0, 0, 4, 0]]


def test_transpose():
    '''testsing transpose'''

    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 4]]
    game2048._Gameboard__transpose()
    assert game2048.gameboard == [[2, 0, 4, 0],
                                  [0, 0, 0, 0],
                                  [2, 0, 0, 2],
                                  [0, 8, 0, 4]]

def test_reverse():
    '''testing reverse'''

    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 4]]

    game2048._Gameboard__reverse()

    assert game2048.gameboard == [[0, 2, 0, 2],
                                  [8, 0, 0, 0],
                                  [0, 0, 0, 4],
                                  [4, 2, 0, 0]]


def test_raw_move_left():
    '''testing raw move left'''
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048._Gameboard__raw_move_left()

    assert game2048.gameboard == [[4, 0, 0, 0],
                                  [8, 0, 0, 0],
                                  [4, 0, 0, 0],
                                  [4, 0, 0, 0]]

def test_move_left():
    '''testing move left'''
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
    '''testing move up'''
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
    '''testing move right'''
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
    '''testing move down'''
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
    '''testing scoring alhorigthin'''
    game2048.score = 0
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.move_left()

    assert game2048.score == 8

def test_is_game_over():
    '''testing game over'''

    game2048.gameboard = [[2048, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    assert game2048.is_game_over() is True

def test_is_game_not_over():
    '''testing gameover for false'''
    game2048.gameboard = [[16, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    assert game2048.is_game_over() is False
