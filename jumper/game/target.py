import random
class Target: 
    '''This class holds a list of words and chooses one to use for the game.
    Attributes: word_list (list)
    '''
    def __init__(self):
        self.word_list =  ["happy", "behind", "jump", "town", "mend", "amazing", "terrify","afternoon", "poor", "shrill"]
        self.game_word = random.choice(self.word_list)
        print(f"The word is {self.game_word}")
        self.word_storage = ""
        while len(self.word_storage) < len(self.game_word):
            self.word_storage = self.word_storage + "_"
        print (self.word_storage)
    
    def get_word(self):
        return self.game_word

    def get_storage(self):
        return self.word_storage