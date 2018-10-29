## Do not change import statements.
import unittest
from SI508_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code. (That's okay!)
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

##########
class CardClassTests(unittest.TestCase):
    def test_card_variables(self):
        suits = str(["Diamonds", "Clubs", "Hearts", "Spades"])
        ranks = str([1,2,3,4,5,6,7,8,9,10,11,12,13])
        face = str({1: "Ace" , 11: "Jack" , 12: "Queen" , 13: "King"})
        self.assertEqual(str(Card.suit_names), suits)
        self.assertEqual(str(Card.rank_levels), ranks)
        self.assertEqual(str(Card.faces), face)
        cardex = Card()
        self.assertEqual(str(cardex), '2 of Diamonds')
    def test_card_suit(self):
        cardex = Card(1,6)
        self.assertEqual(str(cardex.suit), 'Clubs')
    def test_card_rank(self):
        cardex = Card(3, 12)
        self.assertEqual(str(cardex.rank), 'Queen')
    def test_card_rank_num(self):
        cardex = Card(2, 11)
        self.assertEqual(int(cardex.rank_num), 11)
    def test_card_output(self):
        cardex = Card(3, 13)
        self.assertEqual(str(cardex), 'King of Spades')

class DeckClassTests(unittest.TestCase):
    def test_deck_create(self):
        deck1 = Deck()
        self.assertIn('SI508_cards.Card object', deck1.cards)
        self.assertIn('Seven of Diamonds', deck1)
        self.assertIn('Jack of Spades', deck1)
    def test_deck(self):
        deck1 = Deck()
        lendeck = int(len(deck1.cards))
        self.assertEqual(lendeck, 52)
    def test_deck_shuffle(self):
        deck1 = Deck()
        shuffledeck = deck1.shuffle()
        self.assertNotEqual(deck1, shuffledeck)
    def test_pop_replace_card(self):
        testdeck1 = Deck()
        testdeck1_cards_short = testdeck1.cards[:-1]
        testdeck2 = Deck()
        testdeck2_cards = testdeck2.cards
        testdeck1.pop_card()
        testdeck1_cards = testdeck1.cards
        self.assertEqual(testdeck1_cards, testdeck1_cards_short)
        testdeck1.replace_card(Card(3,13))
        self.assertNotEqual(testdeck1_cards, testdeck1_cards_short)
        testdeck1.replace_card(Card(3,13))
        self.assertEqual(len(testdeck2_cards), len(testdeck1_cards))
        try:
            self.assertEqual((str(testdeck1)[-12:]), "King of Spades", "facecards working")
        except:
            self.assertEqual((str(testdeck1)[-12:]), "13 of Spades", "facecards not working")
        for i in range(52):
            testdeck1.pop_card()
        emptydeck = testdeck1.cards
        self.assertEqual(emptydeck, [])
    def test_sort_cards(self):
        deck1 = Deck()
        deck2 = Deck()
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        cards1 = deck1.cards
        sorteddeck = sorted(sorted(cards1, key = lambda x : x.suit_names), key = lambda x : x.rank_levels)
        testdeck = deck2.sort_cards
        self.assertEqual(sorteddeck, testdeck)
    def test_deal_hand(self):
        deck1 = Deck()
        try:
            hand2 = deck1.deal_hand(60)
            self.assertEqual(len(hand1), 60)
            self.assertEqual(type(hand1), type([]), "not failing as specified")
        except:
            hand1 = deck1.deal_hand(5)
            self.assertEqual(len(hand1), 5)
            self.assertEqual(type(hand1), type([]), "failing as specified")


class WarFunctionTests(unittest.TestCase):
    def test_play_war_game(self):
        a = play_war_game(True)
        b = play_war_game(True)
        self.assertNotEqual(a,b)
        self.assertEqual(type(play_war_game(True)[0]), type(""))
        self.assertEqual(type(play_war_game(True)[1]), type(5))
        self.assertEqual(type(play_war_game(True)[2]), type(5))

if __name__  == "__main__":
    unittest.main(verbosity=2)
