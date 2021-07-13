from card_game import Deck, Card, Dealer, Hand, BlackJackHand, Player, Game


class TestDeck:
    def test_deck_contains_full_deck(self):
        d = Deck()
        assert len(d.suits) == 4
        assert len(d.ranks) == 13
        assert len(d.get_cards()) == 52

    def test_shuffle(self):
        deck_1 = Deck()
        deck_2 = Deck()
        deck_2.shuffle()
        assert deck_1.get_cards() != deck_2.get_cards()

    def test_deal_cards(self):
        deck = Deck()
        count = len(deck)
        card = deck.remove_card()
        assert isinstance(card, Card)
        assert len(deck) == count - 1


class TestHand:
    def test_add_card_to_hand(self) -> None:
        hand = Hand()
        deck = Deck()
        hand.add_card(deck.remove_card())
        assert len(hand) == 1

    def test_remove_card_from_hand(self) -> None:
        hand = Hand()
        deck = Deck()

        for i in range(5):
            hand.add_card(deck.remove_card())

        count = len(hand)
        first_card = hand.get_hand()[0]
        removed_card = hand.remove_card(0)

        assert len(hand) == count - 1
        assert first_card is removed_card

    def test_remove_card_from_empty_hand(self) -> None:
        pass


class TestBlackJackHand:
    def test_calculates_score(self) -> None:
        hand = BlackJackHand()

        hand.add_card(Card('A', 'Spades'))
        hand.add_card(Card('K', 'Spades'))
        assert hand.score() == 21
        assert hand.is_busted() is False

        hand.add_card(Card('A', 'Diamonds'))
        assert hand.score() == 12

        hand.add_card(Card('5', 'Spades'))
        assert hand.score() == 17

        hand.add_card(Card('A', 'Hearts'))
        assert hand.score() == 18

        hand.add_card(Card('10', 'Hearts'))
        assert hand.score() == 28
        assert hand.is_busted() is True


class TestPlayer:

    def test_player_initialization(self):
        p = Player("Eric", 1000)
        assert p.name == "Eric"
        assert p.get_funds() == 1000
        assert len(p.get_hand()) == 0

    def test_deal_player(self):
        p = Player("Eric", 1000)
        p.add_card(Card('A', 'Spades'))
        p.add_card(Card('K', 'Spades'))
        assert p.get_hand().score() == 21
        assert len(p.get_hand()) == 2


class TestDealer:

    def test_dealer_initialization(self):
        d = Dealer(1000000)
        assert d.name == "Dealer"
        assert d.get_funds() == 1000000

    def test_deal_self_and_player(self):
        dealer = Dealer(1000000)
        player = Player("Eric", 1000)
        deck = Deck()
        count = len(deck)
        dealer.deal_hand(dealer, deck)
        dealer.deal_hand(player, deck)
        assert len(dealer.get_hand()) == 2
        assert len(player.get_hand()) == 2
        assert len(deck) == count - 4
        assert isinstance(dealer.peak_card(), Card)


class TestGame:

    def test_game_initialization(self):
        g = Game(1000000)
        assert isinstance(g.dealer, Dealer)
        assert g.is_active is False
