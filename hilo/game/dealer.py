from game.player import Player
from random import randint

class Dealer:

    def __init__(self):
        self.current_card = 0
        self.next_card = 0
        self.correct = True
        self.player = Player()

    def choose_card(self):
        if self.current_card == 0:
            self.current_card = randint(1, 13)
        return self.current_card

    def choose_next_card(self):
        self.next_card = randint(1, 13)
        while self.next_card == self.current_card:
            self.next_card = randint(1, 13)
        return self.next_card

    def check_guess(self, current_card, next_card, guess):
        if guess == 'l' and (current_card > next_card):
            self.correct = True
        elif guess == 'h' and (current_card < next_card):
            self.correct = True
        else:
            self.correct = False

        self.player.earn_points(self.correct)

    def start_game(self):
        while self.player.will_continue:
            print(self.choose_card())
            self.player.make_guess()
            print(self.choose_next_card())

            self.check_guess(self.current_card, self.next_card, self.player.guess)
            print(f"\nYour score is: {self.player.points}")
            self.player.keep_playing()
            self.current_card = self.next_card
