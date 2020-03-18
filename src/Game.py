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
        
    ## Checking if active player can play a card or not
    def checkMana(self):
        if (any(self.activePlayer.mana >= x for x in self.activePlayer.hand)):
            return True
        else:
            print(self.activePlayer.name, "has not enough mana to play a card from hand!", self.activePlayer.handCards())
            return False

    ## Playing game.
    def play(self):
        ## Check for if game is over. 
        # This will be changed if one of the player's health is 0 or below
        while self.isGameOver == False:
            ## 3 step of game round
            self.turnStart()
            self.turn()
            self.turnFinish()

    ## Playing round. Active player chooses a card.
    # Checks if it is a valid move.
    def turn(self):
        while self.checkMana():
            print(self.activePlayer,"\nWhich card do you want to play?", self.activePlayer.handCards())
            choice = input()
            try:
                ## Control for integer value
                card = int(choice)
            except ValueError: ## if int operation throws an value error, this will catch it.
                print(choice, "is not a card number!")
                continue
            ## if no error thrown
            else:  
                ## Check for card is in hand or not
                if card not in self.activePlayer.hand:
                    print("You don't have", card)
                    continue
                ## Check for player has enough mana to play
                elif card > self.activePlayer.mana:
                    print("Not enough mana for", card, "\nMana:",self.activePlayer.mana)
                    continue
                ## All conditions satisfied
                else:
                    ## Giving damage to opponent
                    self.activePlayer.playCard(card, self.opponentPlayer)
                    continue
    
    ## Round finish function.
    def turnFinish(self):
        ## Control for if opponent is dead
        if self.opponentPlayer.health <= 0:
            self.isGameOver = True
            print(self.activePlayer.name , " wins!")
        ## Opponents round.
        else:
            print("Turn switched from", self.activePlayer.name,"to", self.opponentPlayer.name, "\n----------------------------------------")
            ## easy switching
            self.activePlayer, self.opponentPlayer = self.opponentPlayer, self.activePlayer
    
    ## Starting round for active player.
    def turnStart(self):
        ## Increasing mana slot.
        self.activePlayer.manaSlots = self.activePlayer.manaSlots + 1 if self.activePlayer.manaSlots < 10 else 10
        ## Fulling manaslot.
        self.activePlayer.fillMana()
        ## Getting card from deck
        self.activePlayer.getCard()