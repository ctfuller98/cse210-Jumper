class Sabetour:
    '''This class is responsible for 'cutting the jumper's chute'. He keeps track 
    of the letters that the jumper has guessed and he displays the results. '''
    '''Attributes: letters_guessed (list) -- A way to store what letters have been guessed
    Methods: display_results'''
    def __init__(self, word_length):
        self.letters_guessed = []
        self.incorrect_letters = 0
        self._hint = "_" * word_length
        self._guesses = []

        #array to hold the lines of the parachute
        self.chute = [
            "   ___  ",
            "  /___\ ",
            "  \   / ",
            "   \ /  ",
            "    0   ",
            "   /|\  ",
            "   / \  ",
            "^^^^^^^^^"
        ]

    def update_list(self, guess: str, targetword: str):
        self._guesses.append(guess)
        new_hint = ""

        # Check if the guess is not in the target word.
        if (targetword.rfind(guess) < 0):
            # Increment our incorrect guesses counter.
            self.incorrect_letters += 1
        
        # Correct guess!
        else:
            # Iterate over target word
            for i in range(len(targetword)):
                # Everytime we find a letter that matches our guess
                # replace the "_" in our _hint
                if targetword[i] == guess:
                    new_hint += guess
                else:
                    new_hint += self._hint[i]

            self._hint = new_hint
            
    def get_hint(self):
        return self._hint

    def display_results(self):
        #For every incorrect guess, we print one less line of the chute array, to display how many guesses have been made.
        i = self.incorrect_letters
        while i < len(self.chute):
            print(self.chute[i])
            i = i + 1