from cards.deck52 import *
from winconditions.poker import *


# deals hands for players
def deal_hand(deck):
    hand = []
    i = 0
    num_cards = 2
    while i < num_cards:
        card = deck.pop_card()
        hand.append(card)
        i += 1
    return hand

# first iteration of showing cards aka, The Flop
def flop(deck):
    table = []
    deck.pop_card()
    i = 0
    flop = 3
    while i < flop:
        card = deck.pop_card()
        table.append(card)
        i += 1
    return table

# second and third deal to the table, The Turn and Up the River respectively
def the_turn(deck):
    deck.pop_card()
    return deck.pop_card()

# dedicated function for checking win conditions
def check_win(cards):

    fullHouse = False

    cards, straightFlush = check_sf(cards)
    if straightFlush:
        print("Player has a straight flush")
        return True

#   print("\nWe passed straight flush\n")

    cards, pair = check_pair(cards)

    if pair == 4:
        return True

#   print("\nWe passed 4 of a kind\n")

    if pair == 3:
        cards, fullHouse = check_fh(cards)

    if fullHouse:
        print("Player has a Full House")
        return True

#   print("\nWe passed full house\n")

    cards, straight = check_straight(cards)

    if straight:
        print("Player has a straight")
        return True

#   print("\nWe passed straight\n")

    cards, flush = check_flush(cards)

    if flush:
        return True
    
#   print("\nWe passed flush\n")

    if pair == 3:
        print("Player has a three of a kind")
        return True

#   print("\nWe passed 3 pair\n")

    if pair == 2:
        cards, twoPair = check_two_pair(cards)
        if twoPair == True:
            print("Player has two pair")
            return True

#       print("\nWe passed two pair\n")

        print("Player has a pair")
        return True
    
#   print("\nWe passed two pair\n")

    cards = sort_face(cards)
    print(f"Player has {str(cards[0].face)[5:].capitalize()} high") 

if __name__ == "__main__":
    print("Creating a standard 52-card deck...")
    deck = Deck()

    print("\nShuffling the deck...")

    print("\nDealing two hands of cards each...")

    hand1 = deal_hand(deck)
    # hand1 = [Card(Face.NINE, Suit.DIAMONDS)]
    hand2 = deal_hand(deck)

    print("\nHand 1:", hand1)
    print("\nHand 2:", hand2)

    table = flop(deck)

    table.append(the_turn(deck))

    table.append(the_turn(deck))

#   table = [Card(Face.TWO, Suit.HEARTS), Card(Face.FOUR, Suit.HEARTS), Card(Face.FIVE,
#             Suit.HEARTS), Card(Face.ACE, Suit.HEARTS), Card(Face.THREE, Suit.HEARTS)]

    print("\nThe cards after the river:")
    print(table)

    player1 = check_win(hand1 + table)
    player2 = check_win(hand2 + table)
