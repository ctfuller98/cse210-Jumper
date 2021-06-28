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
        self.letters_guessed.append(guess)
        
        #check for the guess inside the target word
        on_track = False
        i = 0

        while i < len(targetword):
            new_storage = ""
            #If one piece of target word matches the guess, we are on_track, and we update the newly stored word to display
            if guess == targetword[i]:
                on_track = True
                new_storage = new_storage + guess
            #Whenever we don't find a new character, we put in an underscore.
            else:
                new_storage = new_storage + "_ "

            i = i + 1
            #If we are not on track, we have guessed incorrectly!
        if on_track == False:
            self.incorrect_letters = self.incorrect_letters + 1
            #Update the target word
        return new_storage



    def display_results(self):
        #For every incorrect guess, we print one less line of the chute array, to display how many guesses have been made.
        i = 0 + len(self.incorrect_letters)
        while i < len(self.chute):
            print(self.chute[i])
            i = i + 1