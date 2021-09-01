import random

gameboard = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

def print_gameboard():
    for i in gameboard:
        print(i)
    print()


def slam_left():
    for j in range(4):
        for _ in range(3):
            for i in range(3):
                if gameboard[j][i] == 0:
                    gameboard[j][i] = gameboard[j][i + 1]
                    gameboard[j][i + 1] = 0


def compress_left():
    for j in range(4):
        for i in range(3):
            if gameboard[j][i] != 0 and gameboard[j][i] == gameboard[j][i + 1]:
                gameboard[j][i] = gameboard[j][i] * 2
                gameboard[j][i + 1] = 0


def move_left():
    slam_left()
    compress_left()
    slam_left()


def move_up():
    global gameboard
    gameboard = transpose(gameboard)
    move_left()
    gameboard = transpose(gameboard)


def move_right():
    global gameboard
    gameboard = reverse(gameboard)
    move_left()
    gameboard = reverse(gameboard)


def move_down():
    global gameboard
    gameboard = transpose(gameboard)
    gameboard = reverse(gameboard)
    move_left()
    gameboard = reverse(gameboard)
    gameboard = transpose(gameboard)


def transpose(board):
    interim_board = [[board[j][i] for j in range(4)] for i in range(4)]
    return interim_board


def reverse(board):
    interim_board = [row[::-1] for row in board]
    return interim_board


def pick_random_tile():

    valid = []
    for j in range(4):
        for i in range(4):
            if gameboard[j][i] == 0:
                valid.append((j, i))

    pos = random.choice(valid)
    n = random.random()
    if n >= 0.7:
        gameboard[pos[0]][pos[1]] = 4
    else:
        gameboard[pos[0]][pos[1]] = 2


pick_random_tile()
pick_random_tile()
print_gameboard()
while 0 not in gameboard:
    char = input().rstrip()[0]
    
    if char == 'w':
        move_up()
    elif char == 's':
        move_down()
    elif char == 'd':
        move_right()
    elif char == 'a':
        move_left()
    
    pick_random_tile()
    print_gameboard()

    