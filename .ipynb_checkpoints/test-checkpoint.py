import unittest
from cards.deck52 import Face, Suit, Card
from winconditions.poker import check_sf, check_straight

class TestPokerHands(unittest.TestCase):

#   def test_straight(self):
#       # Straight: 5-6-7-8-9 (Mixed Suits)
#       hand = [
#           Card(Face.FIVE, Suit.HEARTS),
#           Card(Face.SIX, Suit.CLUBS),
#           Card(Face.SEVEN, Suit.SPADES),
#           Card(Face.EIGHT, Suit.DIAMONDS),
#           Card(Face.NINE, Suit.HEARTS)
#       ]
#       hand, straight = check_straight(hand)
#       hand, sf = check_sf(hand)
#       self.assertTrue(straight)
#       self.assertFalse(sf)

#   def test_straight_flush(self):
#       # Straight Flush: 10-J-Q-K-A (All Spades)
#       hand = [
#           Card(Face.TEN, Suit.SPADES),
#           Card(Face.JACK, Suit.SPADES),
#           Card(Face.QUEEN, Suit.SPADES),
#           Card(Face.KING, Suit.SPADES),
#           Card(Face.ACE, Suit.SPADES)
#       ]
#       hand, straight = check_straight(hand)
#       hand, sf = check_sf(hand)
#       self.assertTrue(straight)
#       self.assertTrue(sf)

#   def test_not_straight(self):
#       # Non-Straight: 2-4-5-6-7 (Gap in values)
#       hand = [
#           Card(Face.TWO, Suit.HEARTS),
#           Card(Face.FOUR, Suit.CLUBS),
#           Card(Face.FIVE, Suit.SPADES),
#           Card(Face.SIX, Suit.DIAMONDS),
#           Card(Face.SEVEN, Suit.HEARTS)
#       ]
#       hand, straight = check_straight(hand)
#       hand, sf = check_sf(hand)
#       self.assertFalse(straight)
#       self.assertFalse(sf)

#   def test_not_straight_flush(self):
#       # Not a Straight Flush: 3-4-5-6-7 (Different suits)
#       hand = [
#           Card(Face.THREE, Suit.HEARTS),
#           Card(Face.FOUR, Suit.HEARTS),
#           Card(Face.FIVE, Suit.HEARTS),
#           Card(Face.SIX, Suit.HEARTS),
#           Card(Face.SEVEN, Suit.CLUBS)  # Breaks flush
#       ]
#       hand, straight = check_straight(hand)
#       hand, sf = check_sf(hand)
#       self.assertTrue(straight)
#       self.assertFalse(sf)

    def test_low_ace_straight(self):
        # Low Ace Straight: A-2-3-4-5 (Mixed Suits)
        hand = [
            Card(Face.ACE, Suit.HEARTS),
            Card(Face.TWO, Suit.CLUBS),
            Card(Face.THREE, Suit.SPADES),
            Card(Face.FOUR, Suit.DIAMONDS),
            Card(Face.FIVE, Suit.HEARTS)
        ]
        # print("Hello")
        hand, straight = check_straight(hand)
        # print('hand after straight: ', hand)
        hand, sf = check_sf(hand)
        # print('hand after straight flush: ', hand)
        self.assertTrue(straight)
        self.assertFalse(sf)

#   def test_low_ace_straight_flush(self):
#       # Low Ace Straight Flush: A-2-3-4-5 (All Clubs)
#       hand = [
#           Card(Face.ACE, Suit.CLUBS),
#           Card(Face.TWO, Suit.CLUBS),
#           Card(Face.THREE, Suit.CLUBS),
#           Card(Face.FOUR, Suit.CLUBS),
#           Card(Face.FIVE, Suit.CLUBS)
#       ]
#       hand, straight = check_straight(hand)
#       hand, sf = check_sf(hand)
#       self.assertTrue(straight)
#       self.assertTrue(sf)

if __name__ == "__main__":
    unittest.main()

