from Hand_Generator import Deck, Hand, Card
import random

# This file contains rules for the card game.
# You can define rules for scoring, winning conditions, etc.

# Rules for Crazy Eights
class Crazy_Eight_Rules:

    def __init__(self):
        self.hand_size = 5
    
    def comparison(self, card_top: Card, card_played: Card) -> bool:
        """Compare two cards to determine if the played card is valid."""
        # The rank or suit is the same as the one on the top of the pile
        if card_top.rank == card_played.rank or card_top.suit == card_played.suit:
            return True
        # If the played card is an eight, it can be played on any card
        if card_played.rank == "8":
            return True
        return False

    def make_decision(self, hand: Hand, card_top: Card, deck: Deck, discards: Deck) -> Card:
        """Make a decision based on the current hand and the top card."""
        valid_cards = []
        for card in hand.hand:
            if self.comparison(card_top, card):
                valid_cards.append(card)
        if valid_cards:
            print("Valid cards to play:", valid_cards)
            return random.choice(valid_cards)
        else:
            # If no valid cards, draw until a valid card is found
            print("No valid cards to play. Drawing until a valid card is drawn.")
            card = hand.deck.deck[0]
            hand.deck.deck.remove(card)
            hand.hand.append(card)
            while not self.comparison(card_top, card) and len(hand.deck.deck) > 0:
                card = hand.deck.deck[0]
                hand.deck.deck.remove(card)
                hand.hand.append(card)
                if len(hand.deck.deck) == 0:
                    if len(deck) <= 0:
                        deck.deck = discards.deck[:-1]
                        discards.deck = [discards.deck[-1]]
                        deck.shuffle_deck()

            else:
                return card

        
    