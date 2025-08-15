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
                self.deck.append(Card(card[1], card[0]))
    
    def __len__(self):
        """
        Returns the number of cards left in the deck
        """
        return len(self.deck)
    
    def __repr__(self):
        """
        Returns a string representation of the deck
        """
        string =  "This deck contains the following cards:\n"
        for card in self.deck:
            string += repr(card) + "\n"
        return string
    
    def remove_card(self, card):
        """
        Removes a card from the deck.
        """
        self.deck.remove(card)
    
class Hand:

    def __init__(self, size: int, deck: Deck):
        self.hand = []
        self.deck = deck

        for i in range(size):
            card = random.choice(self.deck.deck)
            while card in self.hand:
                card = random.choice(self.deck.deck)
            self.hand.append(card)
        
        # When a hand is created, remove the cards from the deck
        for card in self.hand:
            self.deck.remove_card(card)

    def __repr__(self):
        string = "This hand contains the following cards:\n"
        # Convert Card objects to string representation
        for card in self.hand:
            string += repr(card) + "\n"
        return string

    def remove_card(self, card):
        """
        Removes a card from the hand.
        """
        self.hand.remove(card)

    def __len__(self):
        """
        Returns the number of cards left in the deck
        """
        return len(self.deck)

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    
    def __lt__(self, other):
        return self.rank < other.rank
    
# Test code
# my_deck = Deck("Classic_Deck.txt")
# my_hand = Hand(HAND_SIZE, my_deck)
# print(my_deck)
# print(my_hand)