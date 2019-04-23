"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        move_to_play = random.randrange(3)
        return moves[move_to_play]

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = "none"

    def move(self):
        if self.last_move == "none":
            move_to_play = random.randrange(3)
            return moves[move_to_play]
        else:
            return self.last_move

    def learn(self, my_move, their_move):
        self.last_move = their_move

#https://docs.python.org/3.4/library/itertools.html
class CyclePlayer(Player):
    def __init__(self):
        self.cycle = 0

    def move(self):
        if self.cycle == 0:
            self.cycle += 1
            return moves[0]
        elif self.cycle == 1:
            self.cycle += 1
            return moves[1]
        elif self.cycle == 2:
            self.cycle = 0
            return moves[2]

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        throw = input('rock, paper, scissors?')
        while throw != 'rock' and throw != 'paper' and throw != 'scissors':
            print('Invalid choice. Please try again.')
            throw = input('rock, paper, scissors?')
        return(throw)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        winning_player = None
        winner = beats(move1, move2)
        if move1 == move2:
            print("DRAW!")
            return [self.p1_score, self.p2_score]
        if winner:
            winning_player = "p1"
            self.p1_score += 1
        else:
            winning_player = "p2"
            self.p2_score += 1
        print(f"Player 1: {move1}  Player 2: {move2}")
        print("Winner : ", winning_player)
        print("p1Pts:" + str(self.p1_score) + "|p2Pts:" + str(self.p2_score))
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        return [self.p1_score, self.p2_score]

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            scores = self.play_round()
        print("Game over!")

        if scores[0] > scores[1]:
            winner = "Player 1"
        elif scores[0] < scores[1]:
            winner = "Player 2"
        elif scores[0] == scores[0]:
            winner = "DRAW!"

        print("p1 score:" + str(scores[0]))
        print("| p2 score:" + str(scores[1]))
        print("WINNER: " + winner)


if __name__ == '__main__':
    game = Game(ReflectPlayer(), HumanPlayer())
    game.play_game()
