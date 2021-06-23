class Sabetour:
    '''This class is responsible for 'cutting the jumper's chute'. He keeps track 
    of the letters that the jumper has guessed and he displays the results. '''
    '''Attributes: letters_guessed (list) -- A way to store what letters have been guessed
    Methods: display_results'''
    def __init__(self):
        self.letters_guessed = []
        update_list()
        display_results()
    def update_list(self, letters_guessed):
        
    def display_results(self):
        print("_ _ _ _ _")
        print(" ___  ")
        print("/___\ " )       
        print("\   /")      
        print(" \ / ")         
        print("0")  
        print(" /|\  ")        
        print("/ \ ") 
        print("^^^^^^^")         