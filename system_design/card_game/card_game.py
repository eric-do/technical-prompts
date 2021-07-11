# Design the data structures for a generic deck of cards.
# Explain how you would subclass the data structuers to implement Blackjack.

# Restatement
# Implement Blackjack using OOP

from collections import namedtuple
from typing import NamedTuple
from random import shuffle

# Card = namedtuple('Card', ['rank', 'suit'])


class Card(NamedTuple):
    rank: str
    suit: str

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


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

    def __getitem__(self, position) -> Card:
        return self.__hand[position]

    def __repr__(self) -> str:
        return '\n'.join([str(c) for c in self.__hand])

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
        cards = [self.values[rank] for rank, _ in self.get_hand()]
        aces = [self.values[rank] for rank, _ in self.get_hand()
                if rank == "A"]
        score += sum(cards)
        for _ in aces:
            if score > 21:
                score -= 10
        return score

    def is_busted(self) -> bool:
        return self.get_score() > 21


class Player:
    def __init__(self, name: str = "Player", funds: int = 0):
        self.name = name
        self.__hand = BlackJackHand()
        self.__funds = funds

    def add_card(self, c: Card) -> None:
        self.__hand.add_card(c)

    def get_hand(self) -> list[Card]:
        return self.__hand

    def get_score(self) -> int:
        return self.__hand.get_score()

    def get_funds(self) -> int:
        return self.__funds


class Dealer(Player):
    def __init__(self, funds: int):
        super().__init__("Dealer", funds)

    def deal_hand(self, p: Player, d: Deck) -> None:
        for i in range(2):
            p.add_card(d.remove_card())

    def deal_card(self, p: Player, d: Deck) -> None:
        p.add_card(d.remove_card())

    def peak_card(self) -> Card:
        return self.get_hand()[0]


class Game:
    def __init__(self, funds: int = 1000000):
        self.dealer = Dealer(funds)
        self.is_active = False

    def add_player(self) -> None:
        name = input("Please enter your name:\n")
        funds = input("Please enter your starting funds: \n")
        p = Player(name, funds)
        self.player = p
        print("Player added.")

    def create_deck(self) -> None:
        self.__deck = Deck()

    def deal_hands(self) -> None:
        self.dealer.deal_hand(self.dealer, self.__deck)
        self.dealer.deal_hand(self.player, self.__deck)
        print('Your hand:')
        print(self.player.get_hand())

    def start_new_game(self) -> None:
        self.is_active = True
        print("Welcome to Blackjack")
        self.add_player()
        self.create_deck()
        self.__deck.shuffle()
        self.deal_hands()


# game = Game()
# game.start_new_game()
