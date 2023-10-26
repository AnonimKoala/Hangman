from player import Player
from hangman import Hangman
import frontend
import os
import time

REWARD_P = 100
NEGATIVE_P = 50     # Have to be positive number


def start():
    frontend.intro()
    frontend.login()

    Player.loadPlayers()
    Player.login()

    os.system("cls")
    frontend.letsplay()
    time.sleep(2.5)
    os.system("cls")


def save():
    Player.save()





lifes =  7

def lossLife():
    global lifes
    lifes -= 1


def screen(word):
    os.system("cls")
    frontend.intro()

    if(lifes < 7):
        print(frontend.HANGMAN_IMG[7-lifes-1])

    print(f"\nKategoria: {word.category.title()} - {word.subcategory.title()}")
    print(word.hashed)

def game():
    word = Hangman()
    global lifes

    

    

    while ('_' in word.hashed and lifes > 0):
        
        
        for player in Player.LOGGED:
            screen(word)


            if '_' not in word.hashed or lifes < 1:
                break

            letter = str(input(f"{player['name']}, podaj literę: ")).lower()[0]

            if letter not in word.guessedLetter_Arr:
                response = word.checkLetter(letter)

                if(response):
                    player["score"] += REWARD_P
                    print(word.hashed)
                else: 
                    player["score"] -= NEGATIVE_P
                    lossLife()

            else:
                print(f"Litera {letter} została już podana!")
            
            
    
    if(lifes < 1):
        screen(word)
        time.sleep(2)
        os.system("cls")
        frontend.intro()
        frontend.gameOver()
        print(f"Nieodgadnięte hasło: {word.word.title()}\n")

        for player in Player.LOGGED:
            print(f"{player['name']}: {player['score']} 💎")

        exit()
    else:
        save()
        lifes = 7

        frontend.congrats()
        for player in Player.LOGGED:
            print(f"{player['name']}: {player['score']} 💎")


        time.sleep(3)
        game()
    
    