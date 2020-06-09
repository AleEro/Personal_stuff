import collections
from random import choice

Card = collections.namedtuple('card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
# print(len(deck))
# print(deck[0])
# beer_card = Card('7', 'diamonds')
# print(beer_card)
# print(choice(deck))
# print(deck[:5])
# print(deck[12::13])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print('card', card)
    print('rank_value', rank_value)
    print('suit_values', len(suit_values))
    print('suit_values[card.suit]', suit_values[card.suit], end='\n\n\n')
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print('- '*10)
    print('card', card)
    print('rank_value', rank_value)
    print('suit_values', len(suit_values))
    print('suit_values[card.suit]', suit_values[card.suit], end='\n\n\n')
