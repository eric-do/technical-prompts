from card_game import Deck, Card, Dealer, Hand, BlackJackHand


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
        assert hand.get_score() == 21

        hand.add_card(Card('A', 'Diamonds'))
        assert hand.get_score() == 12

        hand.add_card(Card('5', 'Spades'))
        assert hand.get_score() == 17

        hand.add_card(Card('A', 'Hearts'))
        assert hand.get_score() == 18


class TestPlayer:
    pass


class TestDealer:
    pass


class TestGame:
    pass
