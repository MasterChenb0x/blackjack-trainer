# this is the card class
class Card:
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    RANKS = ['Joker', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King']
    symbol = {'C': '♣', 'D': '♦', 'H': '♥', 'S': '♠'}

    # Face-side of card, setup for the .format command
    CARD_FACE = """
    ┌─────────┐
    │ {}      │
    │         │
    │    {}    │
    │         │
    │      {} │
    └─────────┘
    """

    # Back-side of card
    CARD_BACK = """
    ┌─────────┐
    │░░░░░░░░░│
    │░░░░░░░░░│
    │░░░░░░░░░│
    │░░░░░░░░░│
    │░░░░░░░░░│
    └─────────┘
    """

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
          >>> print(Card(2, 12))
          Queen of Hearts
        """
        return '{1} of {0}'.format(Card.SUITS[self.suit],
                                   Card.RANKS[self.rank])

    def print_vis_card(self):
        vis_suit = Card.SUITS[self.suit][:1]
        vis_rank = Card.RANKS[self.rank][:1]
        if vis_rank in [1, 11, 12, 13]:
            vis_rank = vis_rank[:1]
        if len(str(vis_rank)) < 2:
            vis_rank = ' ' + str(vis_rank)
        return Card.CARD_FACE.format(vis_rank, Card.symbol[vis_suit], vis_rank)


def __cmp__(self, other, suitcheck):
    # check the suits if this matters
    if suitcheck is True:
        if self.suit > other.suit:
            return 1
            if self.suit < other.suit:
                return -1
    # If suits are same, or not checking suits, check ranks
    else:
        if self.rank > other.rank:
            return 1
            if self.rank < other.rank:
                return -1
    # ranks are the same... it's a tie
    return 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return (len(self.cards) == 0)

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break   # break if out of cards
            card = self.pop()            # take the top card
            hand = hands[i % num_hands]  # whose turn is next?
            hand.add(card)               # add the card to the hand


class Hand(Deck):
    def __init__(self, name=""):
        self.name = name
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = self.name + "'s hand"
        if self.is_empty():
            s = s + " is empty\n"
        else:
            s = s + " contains\n"
        return s + Deck.__str__(self)


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


# Personal test code
class BlackJackHand(Hand):
    def __str__(self):
        s = self.name + "'s hand"
        if self.is_empty():
            s = s + " is empty\n"
        else:
            s = s + " contains\n"
        return s + Deck(self)


# class BlackJack(CardGame):


# Testing the above features
# deck = Deck()
# deck.shuffle()
# hand = Hand("frank")
# deck.deal([hand], 5)
# print(hand)
# print("")
# print(Card.print_vis_card(Card(2, 12)))
