class Card:
    def __init__(self, rank, suit, value):
        self.value = value
        self.rank = rank
        self.suit = suit


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'S D C H'.split()

    def __init__(self):
        self.Cards = [Card(rank=rank,
                           suit=suit,
                           value=int(self.ranks.index(rank))) for suit in self.suits for rank in self.ranks]

    def set_trump(self, suit):
        for card in self.Cards:
            if card.suit == suit:
                card.value = card.value + 20

    def beat_cards(self, cards):
        cards = cards.split(' ')
        card1 = self._beat(arg=[cards[0][:2], cards[0][-1]] if len(cards[0]) >= 3 else [cards[0][:1], cards[0][-1]])
        card2 = self._beat(arg=[cards[1][:2], cards[1][-1]] if len(cards[1]) >= 3 else [cards[1][:1], cards[1][-1]])

        if card1[0] == card2[0]:
            if card1[2] > card2[2]:
                print('First')
            elif card1[2] < card2[2]:
                print('Second')
            else:
                print('Error')

        elif card1[0] != card2[0]:
            if card1[2] > 19 or card2[2] > 19:
                if card1[2] > card2[2]:
                    print('First')
                elif card1[2] < card2[2]:
                    print('Second')
            else:
                print('Error')

    def _beat(self, arg):
        for card in self.Cards:
            if card.suit == arg[1] and card.rank == arg[0]:
                return card.suit, card.rank, card.value


deck = Deck()


while True:
    a = input()
    b = input()
    deck.set_trump(b)
    deck.beat_cards(a)
