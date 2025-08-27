from Hand_Generator import Deck, Hand, Card
import random

# This file contains rules for the card game.
# You can define rules for scoring, winning conditions, etc.

# Rules for Crazy Eights
class Crazy_Eight_Rules:

    def __init__(self):
        self.hand_size = 5
        self.max_players = 2
    
    def comparison(self, card_top: Card, card_played: Card) -> bool:
        """
        In Crazy Eights, a card can be played if:
            - The card is an 8
            - The rank or suit matches the top card on the discard pile
        """
        if card_top.rank == card_played.rank or card_top.suit == card_played.suit:
            return True
        if card_played.rank == "8":
            return True
        return False

    def make_decision(self, hand: Hand, card_top: Card, deck: Deck, discards: Deck) -> Card:
        """
        Make a decision based on the current hand and the top card.
        In Crazy Eights, the decision is to play a valid card or draw a card.
        If there are no valid cards, the ONLY option is to draw a card until
        a valid card is drawn.    
        """
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
            drawn_card = self.draw_card(hand, discards)
            while not self.comparison(card_top, drawn_card):
                drawn_card = self.draw_card(hand, discards)
            return drawn_card
            
    def get_valid_card(self, card_input: str, hand_length: int) -> int:
        if card_input.lower() == "draw":
            return -1
        while not card_input.isdigit() or int(card_input) < 0 or\
        int(card_input) >= hand_length:
            card_input = input("Invalid input. Please enter a valid card number (enter draw to draw a card): ")
        return int(card_input)
    
    def check_deck(self, deck: Deck, discards: Deck):
        """
        In Crazy Eights, if the deck is empty, the deck is
        refilled with the discard pile (except the top card).
        """
        if len(deck) == 0:
            deck.deck = discards.deck[:-1]
            discards.deck = [discards.deck[-1]]
            deck.shuffle_deck()

    def draw_card(self, hand: Hand, discards: Deck) -> Card:
        """
        Draw a card from the deck and add it to the hand. Place in
        mother class when created.
        """
        card = hand.deck.deck[0]
        hand.deck.deck.remove(card)
        hand.hand.append(card)
        print("You drew:", card)
        self.check_deck(hand.deck, discards)
        return card
    
    def check_win(self):
        pass
    
    def start_state(self, deck: Deck, discards: Deck, top_card: Card):
        """
        In Crazy Eights, the game begins by drawing the top card from the deck.
        """
        discards.deck.append(top_card)
        deck.remove_card(top_card)

        

        
    