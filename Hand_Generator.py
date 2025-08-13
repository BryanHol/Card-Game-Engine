import random

CLASSIC = ["Clubs", "Spades", "Hearts", "Diamonds"]
HAND_SIZE = 5

class Deck:

    def __init__(self, filename):

        self.deck = []

        with open(filename, "r") as file:
            file.readline()  # Skip the header line
            for line in file:
                card = line.strip("\n").split(" of ")
                card = Card(card[1], card[0])
                self.deck.append(card)
    
    def __len__(self): # Returns the number of cards left in the deck
        return len(self.deck)
    
    def __repr__(self):
        string =  "This deck contains the following cards:\n"
        for card in self.deck:
            string += repr(card) + "\n"
        return string
    
    def remove_card(self, card):
        self.deck.remove(card)
    
class Hand:

    def __init__(self, deck: Deck):
        self.hand = []
        self.deck = deck.deck

        for i in range(HAND_SIZE):
            card = random.choice(self.deck)
            while card in self.hand:
                card = random.choice(self.deck)
            self.hand.append(card)
        
        # When a hand is created, remove the cards from the deck
        for card in self.hand:
            deck.remove_card(card)

    def __repr__(self):
        string = "This hand contains the following cards:\n"
        # Convert Card objects to string representation
        for card in self.hand:
            if isinstance(card, Card):
                string += repr(card) + "\n"
        return string

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit and self.rank == other.rank
        return False
    
my_deck = Deck("Classic_Deck.txt")
my_hand = Hand(my_deck)
print(my_deck)
print(my_hand)