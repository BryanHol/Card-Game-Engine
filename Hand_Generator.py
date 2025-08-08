import random

CLASSIC = ["Clubs", "Spades", "Hearts", "Diamonds"]
HAND_SIZE = 5

class Deck:

    def __init__(self, SUITS):

        self.deck = []

        for i in range(1, 13):
            for element in SUITS:
                if i == 1:
                    face = "Ace"
                    self.deck.append(face + " of " + element)
                elif i == 10:
                    face = "Jack"
                    self.deck.append(face + " of " + element)
                elif i == 11:
                    face = "Queen"
                    self.deck.append(face + " of " + element)
                elif i == 12:
                    face = "King"
                    self.deck.append(face + " of " + element)
                else:
                    self.deck.append(str(i) + " of " + element)
    
    def __len__(self):
        return len(self.deck)
    
    def __repr__(self):
        return "This deck contains the following cards:\n" +\
                "\n".join(self.deck)
    
class Hand:

    def __init__(self, deck: Deck):
        self.hand = []
        self.deck = deck.deck

        for i in range(HAND_SIZE):
            card = random.choice(self.deck)
            while card in self.hand:
                card = random.choice(self.deck)
            self.hand.append(card)

    def __repr__(self):
        return "Your hand contains the following cards:\n" +\
                "\n".join(self.hand)

my_deck = Deck(CLASSIC)
my_hand = Hand(my_deck)
print(my_hand)