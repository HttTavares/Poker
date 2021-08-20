import random
card_names = 'a23456789tjqk'
# card_suits = ['clubs', 'spades', 'hearts', 'diamonds']
card_suits = 'cshd'

class Deck():

    def __init__(self):
        self.cards = []
        self.create_cards()
        self.shuffle_deck_1()

    def create_cards(self):
        for suit in card_suits:
            for card_name in card_names:
                self.cards.append(f"{card_name}{suit}")

    def shuffle_deck_1(self):
        new_deck_order = []
        deck_copy = self.cards.copy()
        while len(new_deck_order) < 52:
            number = random.randint(0, len(deck_copy) - 1)
            new_deck_order.append(deck_copy[number])
            deck_copy.pop(number)
        self.cards = new_deck_order
        print(len(self.cards))

if __name__ == '__main__':
    deck = Deck()
    print(deck.cards)
    deck.shuffle_deck_1()
    print(deck.cards)
