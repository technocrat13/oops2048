import random
import pickle
import re


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

        try:
            with open('highscorepickle.pkl', 'rb') as file:
                h = pickle.load(file)
                print(h)
                try:
                    self.high_score = h[self.player]
                except KeyError:
                    h[self.player] = 0

        except FileNotFoundError:
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
        print('                                                   score: ', self.score)

    def transpose(self):
        interim_board = [[self.gameboard[j][i] for j in range(4)] for i in range(4)]
        self.gameboard = interim_board


    def reverse(self):
        interim_board = [row[::-1] for row in self.gameboard]
        self.gameboard = interim_board
    



    def slam_left(self):
        for j in range(4):
            for _ in range(3):
                for i in range(3):
                    if self.gameboard[j][i] == 0:
                        self.gameboard[j][i] = self.gameboard[j][i + 1]
                        self.gameboard[j][i + 1] = 0


    def compress_left(self):

        for j in range(4):
            for i in range(3):
                if self.gameboard[j][i] != 0 and self.gameboard[j][i] == self.gameboard[j][i + 1]:
                    self.gameboard[j][i] = self.gameboard[j][i] * 2
                    self.score = self.score + self.gameboard[j][i]
                    #print('score: ' + str(score))
                    if self.score > self.high_score:
                        self.high_score = self.score
                        
                        h = {}
                        with open('highscorepickle.pkl', 'rb') as file:
                            h = pickle.load(file)
                            #print(h)
                            
                        h[self.player] = self.high_score

                        with open('highscorepickle.pkl', 'wb') as file:
                            #h = pickle.load(file)
                            print(h)
                            
                            pickle.dump(h, file)

                    self.gameboard[j][i + 1] = 0

    def move_left(self):

        self.slam_left()
        self.compress_left()
        self.slam_left()


    def move_up(self):

        self.transpose()
        self.move_left()
        self.transpose()


    def move_down(self):

        self.transpose()
        self.reverse()
        self.move_left()
        self.reverse()
        self.transpose()


    def move_right(self):

        self.reverse()
        self.move_left()
        self.reverse()

    def is_game_over(self):

        #print_gameboard()
        for i in self.gameboard:
            if 2048 in i:
                return True

        return False

    def game_loop(self):
        
        self.print_gameboard()
        while not self.is_game_over():
            char = input('[wasd]: ').rstrip()

            if char == 'w':
                self.move_up()
            elif char == 's':
                self.move_down()
            elif char == 'd':
                self.move_right()
            elif char == 'a':
                self.move_left()
            else:
                print('enter valid move [wasd] and press enter')
                continue

            self.pick_random_tile()
            self.print_gameboard()
    
def input_validation(input_string):
    if re.match("^[a-zA-Z0-9_.-]+$", input_string):
        return input_string
    return True



if __name__ == "__main__":
    input_string = input("enter username: ")
    while input_validation(input_string) is True:
        input_string = input("enter only alphanumeric and ._-: ")

    game = gameboard(input_string)
    print('high score 2048 is: ' + str(game.high_score))

    game.game_loop()

