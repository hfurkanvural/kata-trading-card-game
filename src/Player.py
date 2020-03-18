import random

class Player:
    def __init__(self, name):
        self.name = name ## Player Name
        self.health = 30 ## Default health
        self.mana = 0 ## 0 mana can be playable, player can play if has 0 
        self.deck = [0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8] ##Deck will be static for starting
        self.hand = [] ## cards in players hand
        self.manaSlots = 0 ## mana range for turn


    ## string representation of the object.
    def __str__(self): 
        return "Player: " + self.name + "\n* * * * * * * * * *\n*"+("Health: "+ str(self.health)).center(17)+ "*\n*"+("Mana: "+ str(self.mana)+ "/"+ str(self.manaSlots)).center(17)+"*\n* * * * * * * * * *"

    ## object representation.
    def __repr__(self):
        return self.name

    ## Drawing card from deck to hand
    def getCard(self):
        if len(self.deck) == 0: ## checking for bleeding out 
            self.health-=1;  
        else:
            cardIndex = random.randint(0, len(self.deck)-1)
            card = self.deck.pop(cardIndex)
            if len(self.hand) < 5:  ## checking for overload
                self.hand.append(card) ## adding card to hand
            ## else card will be out of deck and not in hand

    ## Print cards
    def handCards(self):
        cards = "\n"+ "#####  " * len(self.hand)
        cards = cards + "\n" +  "#   #  " * len(self.hand) + "\n"
        for card in self.hand:
            cards = cards + ("#"+ str(card).center(3) + "#  ")
        cards = cards + "\n" +  "#   #  " * len(self.hand) 
        cards = cards + "\n" +  "#####  " * len(self.hand) 
        return cards

    ## Playing a card in turn        
    def playCard(self, card, target): ## target will be opponent 
        self.mana -= card ## mana decreasing by card number
        self.hand.remove(card) ## card removed from hand
        target.health -= card ## target damaged in amount of card
        
        if card > 0: ## checking for Dud card
            print(self.name, "gave", card, "damage to", target.name, "\n")
        else:
            print(self.name, "could'nt gave damage to", target.name, "\n")
    


        
