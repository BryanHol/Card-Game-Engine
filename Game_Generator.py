from Hand_Generator import Deck, Hand, Card
from Rules import Crazy_Eight_Rules as CERules
import random

HAND_SIZE = 5
crazy_eights = CERules()

def get_valid_card(card_input: str, hand_length: int) -> int:
    if card_input.lower() == "draw":
        return -1
    while not card_input.isdigit() or int(card_input) < 0 or\
    int(card_input) >= hand_length:
        card_input = input("Invalid input. Please enter a valid card number (enter draw to draw a card): ")
    return int(card_input)

class Game:
    def __init__(self, deck_filename: str, ruleset, hand_size= HAND_SIZE):
        self.deck = Deck(deck_filename)
        self.player1_hand = Hand(hand_size, self.deck)
        self.player2_hand = Hand(hand_size, self.deck)
        self.ruleset = ruleset
        self.top_card = self.deck.deck[0]
        self.discard_pile = Deck()

    def play(self):
        self.shuffle_deck()
        print("Both players drawing hands...")

        self.top_card = self.deck.deck[0]
        print("Top card is:", self.top_card)
        self.discard_pile.deck.append(self.top_card)
        self.deck.remove_card(self.top_card)
        win_con = self.check_win()

        num_players = int(input("How many players? (0, 1, or 2): "))
        if num_players == 0:
            while not win_con:
                self.auto_play("1", self.player1_hand)
                win_con = self.check_win()
                if not win_con:
                    self.auto_play("2", self.player2_hand)
                    win_con = self.check_win()
        if num_players == 1:
            while not win_con:
                self.manual_play("1", self.player1_hand)
                win_con = self.check_win()
                if not win_con:
                    print("Computer's turn...")
                    self.auto_play("2", self.player2_hand)
                    win_con = self.check_win()
        elif num_players == 2:
            while not win_con:
                self.manual_play("1", self.player1_hand)
                win_con = self.check_win()
                if not win_con:
                    self.manual_play("2", self.player2_hand)
                    win_con = self.check_win()

    def check_win(self):
        if len(self.player1_hand.hand) == 0:
            print("Player 1 wins!")
            return True
        elif len(self.player2_hand.hand) == 0:
            print("Player 2 wins!")
            return True
        return False
    
    def shuffle_deck(self):
        random.shuffle(self.deck.deck)
        print("Deck shuffled.")

    def manual_play(self, player: str, hand: Hand):
        """
        This function is for manual play, where players can input their moves.
        """
        valid_cards = []
        for card in hand.hand:
            if self.ruleset.comparison(self.top_card, card):
                valid_cards.append(card)
        print(f"Player {player}'s turn:")
        print(f"Player {player}'s hand:", hand)
        if valid_cards:
            played_card = get_valid_card(input("Which card do you want to play? " \
                "Enter the number of the card (Enter draw to draw a card): "),\
                    len(hand.hand))
            while played_card == -1:
                print("Drawing a card...")
                card = hand.deck.deck[0]
                hand.deck.deck.remove(card)
                hand.hand.append(card)
                print("You drew:", card)
                self.check_deck()
                played_card = get_valid_card(input("Do you want to play a card or draw again?"), len(hand.hand))
            played_card = hand.hand[played_card]
        else:
            while not valid_cards:
                print("No valid cards to play. Drawing a card...")
                card = hand.deck.deck[0]
                hand.deck.deck.remove(card)
                hand.hand.append(card)
                print("You drew:", card)
                self.check_deck()
                if self.ruleset.comparison(self.top_card, card):
                    valid_cards.append(card)
            played_card = get_valid_card(input("Which card do you want to play? " \
                "Enter the number of the card (Enter draw to draw a card): "),\
                    len(hand.hand))
            while played_card == -1:
                print("Drawing a card...")
                card = hand.deck.deck[0]
                hand.deck.deck.remove(card)
                hand.hand.append(card)
                print("You drew:", card)
                self.check_deck()
                played_card = get_valid_card(input("Do you want to play a card or draw again?"), len(hand.hand))
            played_card = hand.hand[played_card]


        while not self.ruleset.comparison(self.top_card, played_card):
            played_card = get_valid_card(input("Card breaks rules. " \
                "Please choose a valid card: "), len(hand.hand))
            played_card = hand.hand[played_card]

        print(f"Player {player} played: {played_card}")
        self.top_card = played_card
        hand.remove_card(played_card)
        self.discard_pile.deck.append(played_card)

    def auto_play(self, player: str, hand: Hand):
        """
        This function is for automatic play, where the game plays itself.
        """
        print(f"Player {player}'s turn:")
        print(f"Player {player}'s hand:", hand)
        played_card = crazy_eights.make_decision(hand, self.top_card, self.deck, self.discard_pile)
        print(f"Player {player} played: {played_card}")
        self.top_card = played_card
        hand.remove_card(played_card)
        self.discard_pile.deck.append(played_card)

    def check_deck(self):
        if len(self.deck) <= 0:
            print("Deck is empty. Reshuffling discard pile into deck.")
            self.deck.deck = self.discard_pile.deck[:-1]
            self.discard_pile.deck = [self.discard_pile.deck[-1]]
            self.shuffle_deck()
        

crazy_eights_game = Game("Classic_Deck.txt", CERules(), HAND_SIZE)
crazy_eights_game.play()