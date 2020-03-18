import random

class Game:
    def __init__(self, player1, player2):
        self.activePlayer = player1 ## Choosing starting player
        self.opponentPlayer = player2 ## Choosing second player
        print("\n",self.activePlayer.name, "is starting!\n") ## Starting Message
        self.isGameOver = False ## Flag for end of game

        for x in range(3):
            self.activePlayer.getCard()
            self.opponentPlayer.getCard()
        
        self.opponentPlayer.getCard() ## Additional card since opponent will start later.
        
    def checkMana(self):
        if (any(self.activePlayer.mana >= x for x in self.activePlayer.hand)):
            return True
        else:
            print(self.activePlayer.name, "has not enough mana to play a card from hand!", self.activePlayer.handCards())
            return False

    def play(self):
        while self.isGameOver == False:
            self.turnStart()
            self.turn()
            self.turnFinish()

    def turn(self):
        while self.checkMana():
            print(self.activePlayer,"\nWhich card do you want to play?", self.activePlayer.handCards())
            choice = input()
            try:
                chosenCard = int(choice, 10)
            except ValueError:
                print(choice, "is not a card number!")
                continue
            else:
                if chosenCard not in self.activePlayer.hand:
                    print("You don't have", chosenCard)
                    continue
                elif chosenCard > self.activePlayer.mana:
                    print("Not enough mana for", chosenCard, "\nMana:",self.activePlayer.mana)
                    continue
                else:
                    self.activePlayer.playCard(chosenCard, self.opponentPlayer)
                    continue

    def turnFinish(self):
        if self.opponentPlayer.health <= 0:
            self.isGameOver = True
            print(self.activePlayer.name , " wins!")
        else:
            print("Turn switched from", self.activePlayer.name,"to", self.opponentPlayer.name, "\n----------------------------------------")
            self.activePlayer, self.opponentPlayer = self.opponentPlayer, self.activePlayer
    
    def turnStart(self):
        self.activePlayer.manaSlots = self.activePlayer.manaSlots + 1 if self.activePlayer.manaSlots < 10 else 10
        self.activePlayer.mana = self.activePlayer.manaSlots
        self.activePlayer.getCard()