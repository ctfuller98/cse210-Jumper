from game.jumper import Jumper
from game.target import Target
from game.sabetour import Sabetour
class Director:
    def __init__(self):
        self.jumper = Jumper()
        self.target = Target()
        self.sabetour = Sabetour(len(self.target.get_word()))
        self.game_over = False
        self.word_list  = []
        self.guess = ""
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        Args:
            self (Director): an instance of Director.
        """
        while self.game_over == False:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the hunter to a new location.

        Args:
            self (Director): An instance of Director.
        """
        self.guess = self.jumper.get_letter()
    def do_updates(self):
        """Updates the important game information for each round of play
        Args:
            self (Director): An instance of Director.
        """
        self.sabetour.update_list(self.guess, self.target.get_word())
        print (self.sabetour.get_hint())

    def do_outputs(self):
        self.sabetour.display_results()