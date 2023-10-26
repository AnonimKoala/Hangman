import random, re

# Zwraca indexy litery
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

CATEGORIES = {
    "animals": ["africa", "endangered", "underwater", "general", "extinct"],
    "countries": ["europe"],
    "hardware": ["computer"],
    "professions": ["popular"]
}

class Hangman:
    def __init__(self):
        self.category = random.choice(list(CATEGORIES))
        self.subcategory = random.choice(CATEGORIES[self.category])
        path = f".\\data\\categories\\{self.category}\\{self.subcategory}.txt"
        f = open(path,"r",encoding='UTF-8')
        lines = f.readlines()
        words = []
        for l in lines:
            words.append(l.strip('\n'))
        
        self.word = random.choice(words).lower()

        self.hashed = re.sub(r'[a-zA-Z]', r'_', self.word)
        self.length = len(self.word)

        self.guessedLetter_Arr = []

    def checkLetter(self, letter):
        response = find(self.word, letter)
        if response:
            for i in response:
                if self.word[i] == letter:
                    self.hashed = self.hashed[:i] + letter + self.hashed[i+1:]
                    self.guessedLetter_Arr.append(letter)
            return len(response)
        else:
            return False
        

