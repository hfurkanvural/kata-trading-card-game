from Game import Game
from Player import Player

if __name__ == "__main__":

    print("Game has started!\n")

    p1name = input("Player1 - Enter your name : ")
    p2name = input("Player2 - Enter your name : ")

    currentGame = Game(Player(p1name), Player(p2name))
    currentGame.play()

