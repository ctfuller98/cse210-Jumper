from game.jumper import Jumper
from game.target import Target
from game.sabetour import Sabetour
class Director:
    def __init__(self):
        self.jumper = Jumper()
        self.target = Target()
        self.sabetour = Sabetour()
        self.game_over = False
        self.word_list  = []
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
        guess = self.jumper.get_letter()
    def do_updates(self):
        """Updates the important game information for each round of play
        Args:
            self (Director): An instance of Director.
        """
        answer = self.target.get_word()
    def do_ouptuts(self):
        display = self.sabetour.display_results