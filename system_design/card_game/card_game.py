# Design the data structures for a generic deck of cards.
# Explain how you would subclass the data structuers to implement Blackjack.

# Restatement
# Implement Blackjack using OOP

from collections import namedtuple
from random import shuffle

Card = namedtuple('Card', ['rank', 'suit'])


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = "diamonds clubs hearts spades".split()

    def __init__(self):
        self.__cards = [Card(rank, suit) for rank in self.ranks
                        for suit in self.suits]

    def __len__(self):
        return len(self.__cards)

    def get_cards(self):
        return self.__cards

    def shuffle(self) -> None:
        shuffle(self.__cards)

    def remove_card(self) -> Card:
        return self.__cards.pop(0)

    def deal_hand(self) -> list[Card]:
        return [self.deal_card() for i in range(2)]


class Hand:
    def __init__(self):
        self.__hand = []

    def __len__(self):
        return len(self.__hand)

    def get_hand(self) -> list[Card]:
        return self.__hand

    def add_card(self, c: Card) -> None:
        self.__hand.append(c)

    def remove_card(self, i: int) -> Card:
        return self.__hand.pop(i)


class BlackJackHand(Hand):
    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }

    def __init__(self):
        super().__init__()

    def get_score(self) -> int:
        score = 0
        ace_count = 0

        for rank, _ in self.get_hand():
            score += self.values[rank]
            if rank == "A":
                ace_count += 1

        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
        return score


class Player:
    def __init__(self, funds=0):
        self.__hand = BlackJackHand()
        self.__funds = funds
        self.hit = self.add_card

    def add_card(self, c: Card) -> None:
        self.__hand.add_card(c)

    def get_hand(self) -> list[Card]:
        return self.__hand

    def get_score(self) -> int:
        return self.__hand.get_score()

    def get_funds(self) -> int:
        return self.__funds


class Dealer(Player):
    def __init__(self, funds):
        super().__init__(funds)

    def deal_hand(p: Player, d: Deck) -> None:
        for i in range(2):
            p.add_card(d.remove_card())

    def deal_card(p: Player, d: Deck) -> None:
        p.add_card(d.remove_card())
