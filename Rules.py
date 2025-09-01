from Hand_Generator import Deck, Hand, Card
import random

# This file contains rules for the card game.
# You can define rules for scoring, winning conditions, etc.

class Player:
    def __init__(self, name: str, hand: Hand, human: bool = True):
        self.name = name
        self.hand = hand
        self.human = human

# Rules for Crazy Eights
class Crazy_Eight_Rules:

    def __init__(self):
        self.hand_size = 5
        self.max_players = 5
    
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
    
    def check_deck(self, deck: Deck, discards: Deck):
        """
        In Crazy Eights, if the deck is empty, the deck is
        refilled with the discard pile (except the top card).
        """
        if len(deck) == 0:
            deck.deck = discards.deck[:-1]
            discards.deck = [discards.deck[-1]]
            deck.shuffle_deck()
    
    def start_state(self, deck: Deck, discards: Deck) -> list[Player]:
        """
        In Crazy Eights, the game begins by drawing the top card from the deck.
        Every game can have up to 5 players; each player is dealt 5 cards.
        """
        discards.deck.append(deck.deck[0])
        deck.remove_card(deck.deck[0])

        players = []
        num_players = int(input("How many players? (0 to 5): "))
        for i in range(num_players):
            players.append(Player("Player " + str(i+1), Hand(self.hand_size, deck)))
        length = len(players)
        for i in range(self.max_players - length):
            players.append(Player("Player " + str(length + i + 1), Hand(self.hand_size, deck), human=False))
        
        print("Top card is:", discards.deck[-1])

        return players
    
    def check_win(self, players: list[Player]) -> bool:
        """
        In Crazy Eights, a player wins when they have no cards left.
        """
        for player in players:
            if len(player.hand.hand) == 0:
                print(f"{player.name} wins!")
                return True
        return False

    def find_valid_cards(self, hand: Hand, card_top: Card) -> list[Card]:
        """
        Finds all valid cards that can be played from the hand.
        """
        valids = []
        for card in hand.hand:
            if self.comparison(card_top, card):
                valids.append(card)
        return valids

    def determine_choices(self, hand: Hand, card_top: Card) -> list[int]:
        """
        Determines the valid choices a player can make.
        Returns a list of indices of valid cards in the hand, 
        plus -1 for drawing a card.
        """
        choices = [-1]  # -1 represents the option to draw a card
        valid_cards = self.find_valid_cards(hand, card_top)
        for card in valid_cards:
            choices.append(hand.hand.index(card))
        return choices
    
    def process_choice(self, hand: Hand, deck: Deck, discards: Deck) -> Card:
        """
        Make a manual decision based on the current hand and the top card.
        In Crazy Eights, the decision is to play a valid card or draw a card.
        If there are no valid cards, the ONLY option is to draw a card until
        a valid card is drawn.    
        """ 
        choices = self.determine_choices(hand, discards.deck[-1])
        print("Your choices are:", choices)
        choice = input("Enter the number of the card you want to play (or -1 to draw a card): ")
        while (choice != "-1" and not choice.isdigit()) or int(choice) not in choices:
            choice = input("Invalid choice. Please enter a valid choice: ")
        choice = int(choice)
        while choice == -1:
            self.draw(hand, deck, discards)
            choices = self.determine_choices(hand, discards.deck[-1])
            print("Your choices are:", choices)
            choice = input("Enter the number of the card you want to play (or -1 to draw a card): ")
            while (choice != "-1" and not choice.isdigit()) or int(choice) not in choices:
                choice = input("Invalid choice. Please enter a valid choice: ")
            choice = int(choice)
        return hand.hand[choice]
    
    def make_decision(self, hand: Hand, deck: Deck, discards: Deck) -> Card:
        """
        Make an automatic decision based on the current hand and the top card.
        In Crazy Eights, the decision is to play a valid card or draw a card.
        If there are no valid cards, the ONLY option is to draw a card until
        a valid card is drawn.    
        """ 
        choices = self.determine_choices(hand, discards.deck[-1])
        choice = random.choice(choices)
        while choice == -1:
            self.draw(hand, deck, discards)
            choices = self.determine_choices(hand, discards.deck[-1])
            choice = random.choice(choices)
        return hand.hand[choice]
    
    def draw(self, hand: Hand, deck: Deck, discards: Deck) -> Card:
        """
        Draws a card from the deck to the hand.
        """
        print("Drawing a card...")
        card = hand.deck.deck[0]
        hand.deck.deck.remove(card)
        hand.hand.append(card)
        print("You drew:", card)
        self.check_deck(deck, discards)
        return card

    def play_card(self, hand: Hand, card: Card, player: str, discards: Deck):
        """"
        Plays a card from the hand to the discard pile.
        """
        print(f"{player} played: {card}")
        hand.remove_card(card)
        discards.deck.append(card)
        return card