
class jumper:
    '''
    Represents the player input in the game. 
    Responsible for parsing input from the user, which letter they are guessing.
    '''
    def __init__(self):
        #If we need anything in here, this will be the place for initialization
        pass

    def get_letter(self):
        guess = input("Guess a letter [a-z]: ")
        return guess