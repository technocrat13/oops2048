'''module for 2048 Gameboard using OOP concepts'''

import random
import pickle
import re


class Gameboard():
    '''class to hold the gameboard and all its functions'''

    def __init__(self, player_name):
        '''defult constuctor to build a new gameboard'''
        self.gameboard = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]

        self.score = 0
        self.player = player_name
        self.high_score = 0
        self.__load_high_score()
        self.pick_random_tile()
        self.pick_random_tile()

    def __str__(self):
        '''overloaded print gameboard along side the score'''
        output = ''
        for i in self.gameboard:
            output = output + str(i) + '\n'
        #print('                                                   score: ', self.score)
        return output

    def __load_high_score(self):
        '''uses a picklefile to maintain all scores'''

        try:
            with open('highscorepickle.pkl', 'rb') as file:
                high_score_pickle = pickle.load(file)
                print(high_score_pickle)
                try:
                    self.high_score = high_score_pickle[self.player]
                except KeyError:
                    high_score_pickle[self.player] = 0

        except FileNotFoundError:
            self.high_score = 0
            with open('highscorepickle.pkl', 'wb') as file:
                high_score_pickle = {}
                high_score_pickle[self.player] = 0
                pickle.dump(high_score_pickle, file)

    def pick_random_tile(self):
        '''builds a list of empty tiles and then choses one to either put a 2 or a 4 on it'''

        valid = []
        for j in range(4):
            for i in range(4):
                if self.gameboard[j][i] == 0:
                    valid.append((j, i))

        try:
            pos = random.choice(valid)
            if random.random() >= 0.7:  # difficulty selector
                self.gameboard[pos[0]][pos[1]] = 4
            else:
                self.gameboard[pos[0]][pos[1]] = 2

        except IndexError:
            print('try another move')

    def print_gameboard(self):
        '''to print gameboard along side the score'''
        for i in self.gameboard:
            print(i)
        print('                                                   score: ', self.score)

    def __transpose(self):
        '''transpose of a 2d matix'''
        interim_board = [[self.gameboard[j][i] for j in range(4)] for i in range(4)]
        self.gameboard = interim_board


    def __reverse(self):
        '''reverse of a 2d matix'''
        interim_board = [row[::-1] for row in self.gameboard]
        self.gameboard = interim_board


    def __slam_left(self):
        '''moving all elements to the left'''
        for j in range(4):
            for _ in range(3):
                for i in range(3):
                    if self.gameboard[j][i] == 0:
                        self.gameboard[j][i] = self.gameboard[j][i + 1]
                        self.gameboard[j][i + 1] = 0


    def __compress_left(self):
        '''joining all elements to the left'''
        for j in range(4):
            for i in range(3):
                if self.gameboard[j][i] != 0 and self.gameboard[j][i] == self.gameboard[j][i + 1]:
                    self.gameboard[j][i] = self.gameboard[j][i] * 2
                    self.score = self.score + self.gameboard[j][i]
                    #print('score: ' + str(score))
                    if self.score > self.high_score:
                        self.high_score = self.score

                        high_score_pickle = {}
                        with open('highscorepickle.pkl', 'rb') as file:
                            high_score_pickle = pickle.load(file)
                            #print(h)

                        high_score_pickle[self.player] = self.high_score

                        with open('highscorepickle.pkl', 'wb') as file:
                            #h = pickle.load(file)
                            print(high_score_pickle)

                            pickle.dump(high_score_pickle, file)

                    self.gameboard[j][i + 1] = 0

    def __raw_move_left(self):
        '''basic left move'''
        self.__slam_left()
        self.__compress_left()
        self.__slam_left()

    def move_left(self):
        '''left move'''

        self.__raw_move_left()


    def move_up(self):
        '''up move'''

        self.__transpose()
        self.__raw_move_left()
        self.__transpose()


    def move_down(self):
        '''down move'''

        self.__transpose()
        self.__reverse()
        self.__raw_move_left()
        self.__reverse()
        self.__transpose()


    def move_right(self):
        '''right move'''

        self.__reverse()
        self.__raw_move_left()
        self.__reverse()

    def is_game_over(self):
        '''check if 2048 has been made or not'''

        #print_gameboard()
        for i in self.gameboard:
            if 2048 in i:
                print('winner!!1!!!1!11!')
                return True

        return False

    def game_loop(self):
        '''game loop to run in console'''

        #self.print_gameboard()
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

def input_validation(input_to_validate):
    '''regex for username checking'''

    if re.match("^[a-zA-Z0-9_.-]+$", input_to_validate):
        return input_to_validate
    return True



if __name__ == "__main__":
    input_string = input("enter username: ")
    while input_validation(input_string) is True:
        input_string = input("enter only alphanumeric and ._-: ")

    game = Gameboard(input_string)
    print('high score 2048 is: ', game.high_score)
    print(game)

    game.game_loop()
