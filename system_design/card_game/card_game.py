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

    def __getitem__(self, position) -> Card:
        return self.__hand[position]

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
    def __init__(self, funds: int):
        self.dealer = Dealer(funds)
        self.__players = []

    def add_player(self) -> None:
        name = input("Please enter your name")
        funds = input("Please enter your starting funds")
        p = Player(name, funds)
        self.__players.append(p)
        print("Player added.")

    def get_players(self) -> list[Player]:
        return self.__players

    def start_new_game(self) -> None:
        print("Welcome to Blackjack")
        self.add_player()
        self.dealer.deal_hand(self.dealer, self.__deck)
        for p in self.players:
            self.dealer.deal_hand(p, self.__deck)
