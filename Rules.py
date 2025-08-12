from Hand_Generator import Deck, Hand
import random

# This file contains rules for the card game.
# You can define rules for scoring, winning conditions, etc.

# Turning each card into a tuple of (suit, rank) for easier comparison
def card_to_tuple(hand: Hand):
    """Convert a card string to a tuple of (suit, rank)."""
    return [tuple(card.split(" of ")) for card in hand.hand]

# Rules for Crazy Eights
def comparison(card_top, card_played):
    """Compare two cards to determine if the played card is valid."""
    # The rank or suit is the same as the one on the top of the pile
    if card_top[0] == card_played[0] or card_top[1] == card_played[1]:
        return True
    # If the played card is an eight, it can be played on any card
    if card_played[1] == "Eight":
        return True
    return False

def make_decision(hand:Hand, card_top:tuple):
    """Make a decision based on the current hand and the top card."""
    valid_cards = []
    for card in hand.hand:
        if comparison(card_top, card):
            valid_cards.append(card)
    if valid_cards:
        print("Valid cards to play:", valid_cards)
        return random.choice(valid_cards)
    else:
        # If no valid cards, draw until a valid card is found
        print("No valid cards to play. Drawing until a valid card is drawn.")
        card = random.choice(hand.deck)
        while not comparison(card_top, card):
            hand.hand.append(card)
        return card

        
    