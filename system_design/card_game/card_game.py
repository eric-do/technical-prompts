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

    def score(self) -> int:
        cards = [self.values[rank] for rank, _ in self.get_hand()]
        aces = [self.values[rank] for rank, _ in self.get_hand()
                if rank == "A"]
        score = sum(cards)
        for _ in aces:
            if score > 21:
                score -= 10
        return score

    def is_busted(self) -> bool:
        return self.score() > 21


class Player:
    def __init__(self, name: str = "Player", funds: int = 0):
        self.name = name
        self.__hand = BlackJackHand()
        self.__funds = funds

    def add_card(self, c: Card) -> None:
        self.__hand.add_card(c)

    def get_hand(self) -> list[Card]:
        return self.__hand

    def get_funds(self) -> int:
        return self.__funds


class Dealer(Player):
    def __init__(self, funds: int):
        super().__init__("Dealer", funds)

    def deal_hand(self, p: Player, d: Deck) -> None:
        for i in range(2):
            self.deal_card(p, d)

    def deal_card(self, p: Player, d: Deck) -> None:
        p.add_card(d.remove_card())

    def play_game(self, deck) -> None:
        while self.get_hand().score() < 17:
            self.deal_card(self, deck)

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

    def get_player(self) -> Player:
        return self.player

    def create_deck(self) -> None:
        self.__deck = Deck()
        self.__deck.shuffle()

    def deal_hands(self) -> None:
        self.dealer.deal_hand(self.dealer, self.__deck)
        self.dealer.deal_hand(self.player, self.__deck)

    def game_loop(self) -> None:
        player_hand = self.player.get_hand()
        print('Your hand:')
        print(player_hand)
        print('Your score:', player_hand.score())
        if player_hand.is_busted():
            print('BUST')
        else:
            choice = input("Hit? [Y/N]\n").lower()
            if choice == 'y':
                self.dealer.deal_card(self.player, self.__deck)
                self.game_loop()
            else:
                self.dealer.play_game(self.__deck)
            self.show_result()
            exit()

    def show_result(self) -> None:
        player_score = self.player.get_hand().score()
        dealer_score = self.dealer.get_hand().score()
        print('Dealer score:', dealer_score)
        print('Player score:', player_score)
        if player_score == 21 and dealer_score == 21:
            print('DRAW')
        elif player_score <= 21 and \
            (dealer_score <= player_score or
                self.dealer.get_hand().is_busted()):
            print('YOU WIN')
        else:
            print('YOU LOSE')

    def start_new_game(self) -> None:
        self.is_active = True
        print("Welcome to Blackjack")
        self.add_player()
        self.create_deck()
        self.deal_hands()
        self.game_loop()


game = Game()
game.start_new_game()
