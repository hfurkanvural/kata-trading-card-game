import unittest
import mock
import logging
import sys
from src.Player import Player
from src.Game import Game


class Game_Test(unittest.TestCase):

    def setUp(self):
        self.TestGame = Game(Player("p1"), Player("p2"))


    def testStarting(self):
        log = logging.getLogger("testStarting")
        log.debug("Testing starting steps...")

        ##Testing if players got cards from deck
        log.debug("Checking activePlayer.")
        self.assertEqual(len(self.TestGame.activePlayer.hand), 3)
        self.assertEqual(len(self.TestGame.activePlayer.deck), 17)
        log.debug("Checking opponentPlayer.")
        self.assertEqual(len(self.TestGame.opponentPlayer.hand), 4)
        self.assertEqual(len(self.TestGame.opponentPlayer.deck), 16)

    def testTurnStart(self):
        log = logging.getLogger("testTurnStart")
        log.debug("Testing turnStart function...")

        ##Default value check for manaslots and mana
        log.debug("Checking default value.")
        self.TestGame.turnStart()
        self.assertEqual(self.TestGame.activePlayer.manaSlots, 1)
        self.assertEqual(self.TestGame.activePlayer.mana, 1)

        ##Checking deck and hand cards for default start (if it gets 4th card or not)
        log.debug("Checking active player.")
        self.assertEqual(len(self.TestGame.activePlayer.deck), 16)
        self.assertEqual(len(self.TestGame.activePlayer.hand), 4)

        ##Max value check for manaslots
        log.debug("Checking maximum value.")
        self.TestGame.activePlayer.manaSlots = 10
        self.TestGame.turnStart()
        self.assertEqual(self.TestGame.activePlayer.manaSlots, 10)
        self.assertEqual(self.TestGame.activePlayer.mana, 10)

    def testTurnFinish(self):
        log = logging.getLogger("testTurnFinish")
        log.debug("Testing turnFinish function...")

        ##Checking if turn switched or not
        log.debug("Checking turn switch.")
        self.TestGame.turnFinish()
        self.assertEqual(self.TestGame.activePlayer.name, "p2")
    
    def testTurn(self):
        log = logging.getLogger("testTurn")
        log.debug("Testing turn function...")

        ##Playing a turn
        log.debug("Testing succesfull move.")
        self.TestGame.activePlayer.hand = [3,4,5]
        self.TestGame.activePlayer.mana = 5
        with mock.patch('builtins.input', return_value="3"):
            self.TestGame.turn()
            ##Checking the mana left
            log.debug("Checking mana.")
            self.assertEqual(self.TestGame.activePlayer.mana, 2)
            ##Checking the hand
            log.debug("Checking if the card is played.")      
            self.assertEqual(self.TestGame.activePlayer.hand, [4,5])
            ##Checkin opponent health
            log.debug("Checking if opponentPlayer gets damage.")
            self.assertEqual(self.TestGame.opponentPlayer.health, 27)

    def testTurnFinish(self):
        log = logging.getLogger("testTurnFinish")
        log.debug("Testing turnFinish function...")

        
        log.debug("Testing finishing move.")
        self.TestGame.activePlayer.hand = [3,4,5]
        self.TestGame.activePlayer.mana = 5
        self.TestGame.opponentPlayer.health = 3
        with mock.patch('builtins.input', return_value="4"):
            ##Playing a turn
            self.TestGame.turn()
            ##Finishing a turn
            self.TestGame.turnFinish()
            ##Checking if game is over
            log.debug("Checking if game is over.")
            self.assertEqual(self.TestGame.isGameOver, True)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()