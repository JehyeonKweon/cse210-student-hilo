class Player:

    def __init__(self):
        self.points = 300
        self.will_continue = True
        self.guess = ''

    def make_guess(self):
        self.guess = input("Higher or lower [h/l]? ")

    def keep_playing(self):
        # if game over
        if self.points <= 0:
            return False
        
        # keep playing?
        choice = input("Keep playing? [y/n] ")
        if choice.lower() == 'y':
            self.will_continue = True
        elif choice.lower() == 'n':
            self.will_continue = False

        return self.will_continue

    def earn_points(self, correct):
        if correct:
            self.points += 100
        else:
            self.points -= 75

        return self.points