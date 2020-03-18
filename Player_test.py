import unittest
import logging
import sys
from Player import Player

deck = [0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8]
hand = []

class Player_Test(unittest.TestCase):

    ## Default step for every function
    def setUp(self):
        self.activePlayer = Player("Active")
        self.opponentPlayer = Player("Opponent")

    def testName(self):
        log = logging.getLogger("testName")
        log.debug("Testing names...")
        ##Testing if the names are correct
        self.assertEqual(self.activePlayer.name, 'Active')
        self.assertEqual(self.opponentPlayer.name, 'Opponent')

    def testHealth(self):
        log = logging.getLogger("testHealth")
        log.debug("Testing healths...")
        ##Testing if health equal to 30 for starting
        self.assertEqual(self.activePlayer.health, 30)
        self.assertEqual(self.opponentPlayer.health, 30)

    def testMana(self):
        log = logging.getLogger("testMana")
        log.debug("Testing players' mana...")
        ##Testing if mana equal to 0 for starting
        self.assertEqual(self.activePlayer.mana, 0)
        self.assertEqual(self.opponentPlayer.mana, 0)

    def testDeck(self):
        log = logging.getLogger("testDeck")
        log.debug("Testing decks...")
        ##Testing if deck is full for starting
        self.assertEqual(self.activePlayer.deck, deck)
        self.assertEqual(self.opponentPlayer.deck, deck)

    def testHand(self):
        log = logging.getLogger("testHand")
        log.debug("Testing hands...")
        ##Testing if hand is empty for starting
        self.assertEqual(self.activePlayer.hand, [])
        self.assertEqual(self.opponentPlayer.hand, [])

    def testManaSlots(self):
        log = logging.getLogger("testManaSlots")
        log.debug("Testing manaSlots...")
        ##Testing if manaSlots equal to 0 for starting
        self.assertEqual(self.activePlayer.manaSlots, 0)
        self.assertEqual(self.opponentPlayer.manaSlots, 0)

    def testDraw(self):
        log = logging.getLogger("testDraw")
        log.debug("Testing getCard function...")

        ##Testing if it gets a card or not
        self.activePlayer.getCard()
        self.assertEqual(len(self.activePlayer.deck), 19)
        self.assertEqual(len(self.activePlayer.hand), 1)

        ##Overload
        log.debug("Testing Overload")
        self.activePlayer.deck = [9]
        self.activePlayer.hand = [1,2,3,4,5]
        self.activePlayer.getCard()
        ##Testing if it gets more than 5 card or not 
        self.assertEqual(len(self.activePlayer.hand), 5)
        ##Testing if 6th card is discarded 
        self.assertEqual(self.activePlayer.hand, [1,2,3,4,5])

        ##Bleeding Out
        log.debug("Testing Bleeding Out...")
        self.activePlayer.deck = []
        self.activePlayer.getCard()
        ##Testing if it receives 1 damage when deck is empty 
        self.assertEqual(self.activePlayer.health, 29)

    def testPlay(self):
        log = logging.getLogger("testMana")
        log.debug("Testing PlayCard function...")

        self.activePlayer.hand = [4,5,6]
        self.activePlayer.mana = 10
        self.activePlayer.playCard(4, self.opponentPlayer)
        ##Testing if opponent received damage
        self.assertEqual(self.opponentPlayer.health, 26)
        ##Testing if played card is removed
        self.assertEqual(len(self.activePlayer.hand), 2)
        ##Testing if played card reduced mana
        self.assertEqual(self.activePlayer.mana, 6)



if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()