class Sabetour:
    '''This class is responsible for 'cutting the jumper's chute'. He keeps track 
    of the letters that the jumper has guessed and he displays the results. '''
    '''Attributes: letters_guessed (list) -- A way to store what letters have been guessed
    Methods: display_results'''
    def __init__(self):
        self.letters_guessed = []
        self.incorrect_letters = 0
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

    def update_list(self, guess, targetword):
        hint = ""
        for x in word:
            if guesses.count(x)>0:
                hint+=x
            else:
                hint+="_"
        self.letters_guessed.append(guess)
        if target_word.count(guessed_letter)<=0:
            if incorrect_letters> 
            gussed_list.append
        else:
            for i in range(target_word.count):
        return new_storage



    def display_results(self):
        #For every incorrect guess, we print one less line of the chute array, to display how many guesses have been made.
        i = self.incorrect_letters
        while i < len(self.chute):
            print(self.chute[i])
            i = i + 1