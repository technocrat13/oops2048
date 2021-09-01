import random
import pickle

'''
gameboard = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

global high_score
global score

score = 0
'''
class gameboard():

    def __init__(self, player_name):
        self.gameboard = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]

        self.score = 0
        self.player = player_name
        self.high_score = 0
        self.load_high_score()
        self.pick_random_tile()
        self.pick_random_tile()


    def load_high_score(self):

        with open('highscorepickle.pkl', 'rb') as file:
            h = pickle.load(file)
            try:
                self.high_score = h[self.player]
            except:
                h[self.player] = 0
            
            return
        
        self.high_score = 0
        with open('highscorepickle.pkl', 'wb') as file:
            h = {}
            h[self.player] = 0
            pickle.dump(h, file)
            
    def pick_random_tile(self):

        valid = []
        for j in range(4):
            for i in range(4):
                if self.gameboard[j][i] == 0:
                    valid.append((j, i))

        try:
            pos = random.choice(valid)
            n = random.random()
            if n >= 0.7:  # difficulty selector
                self.gameboard[pos[0]][pos[1]] = 4
            else:
                self.gameboard[pos[0]][pos[1]] = 2

        except:
            print('try another move')
    
    def print_gameboard(self):
        for i in self.gameboard:
            print(i)
        print()


    

'''
try:
    high_score_pickle = open('highscorepickle.pkl', 'rb')
    h = pickle.load(high_score_pickle)
    high_score = h['score']
    high_score_pickle.close()
except FileNotFoundError:
    high_score = 0
    h = {}
    h['score'] = high_score
    high_score_pickle = open('highscorepickle.pkl', 'wb')
    pickle.dump(h, high_score_pickle)
    high_score_pickle.close()
'''

def print_gameboard():
    for i in gameboard:
        print(i)
    print()


def pick_random_tile():

    valid = []
    for j in range(4):
        for i in range(4):
            if gameboard[j][i] == 0:
                valid.append((j, i))

    try:
        pos = random.choice(valid)
        n = random.random()
        if n >= 0.7:  # difficulty selector
            gameboard[pos[0]][pos[1]] = 4
        else:
            gameboard[pos[0]][pos[1]] = 2

    except:
        print('try another move')

    


def transpose(board):
    interim_board = [[board[j][i] for j in range(4)] for i in range(4)]
    return interim_board


def reverse(board):
    interim_board = [row[::-1] for row in board]
    return interim_board


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
                global score
                global high_score
                score = score + gameboard[j][i]
                #print('score: ' + str(score))
                if score > high_score:
                    high_score = score
                    h = {}
                    h['score'] = high_score
                    high_score_pickle = open('highscorepickle.pkl', 'wb')
                    pickle.dump(h, high_score_pickle)
                    #print(high_score)
                    high_score_pickle.close()

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


def move_down():

    global gameboard
    gameboard = transpose(gameboard)
    gameboard = reverse(gameboard)
    move_left()
    gameboard = reverse(gameboard)
    gameboard = transpose(gameboard)


def move_right():

    global gameboard
    gameboard = reverse(gameboard)
    move_left()
    gameboard = reverse(gameboard)

def is_game_over():

    #print_gameboard()
    for i in gameboard:
        if 2048 in i:
            return True
    
    return False

def init_gameboard():
    pick_random_tile()
    pick_random_tile()
    print_gameboard()




if __name__ == "__main__":

    print('high score 2048 is: ' + str(high_score))
    init_gameboard()

    while not is_game_over():
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



