from player import Player
from hangman import Hangman

REWARD_P = 100
NEGATIVE_P = 50     # Have to be positive number

def start():
    Player.loadPlayers()
    Player.login()

def save():
    Player.save()





lifes =  5

def lossLife():
    global lifes
    lifes -= 1
    print("Pozostało żyć: ", lifes)
    # TODO: Rys Hangman


def game():
    word = Hangman()
    global lifes
    print(word.hashed)
    

    while ('_' in word.hashed and lifes > 0):
        for player in Player.LOGGED:
            letter = str(input(f"{player['name']}, podaj literę: ")).lower()[0]
            response = word.checkLetter(letter)
            
            if(response):
                player["score"] += REWARD_P
                print(word.hashed)
            else: 
                player["score"] -= NEGATIVE_P
                lossLife()
    
    if(lifes == 0):
        print("GAME OVER")
        print("Hasło: ", word.word)
        exit()
    else:
        save()
        lifes = 5
        game()
    
    