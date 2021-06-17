import random
class Target: 
    '''This class holds a list of words and chooses one to use for the game.
    Attributes: word_list (list)
    '''
    def __init__(self):
        self.word_list =  ["happy", "behind", "jump", "town", "mend", "amazing", "terrify","afternoon", "poor", "shrill"]
    def get_word(self, word_list):
        game_word = random.choice(word_list)
        print(f"The word is {game_word}")
        return game_word