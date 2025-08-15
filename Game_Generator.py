from Hand_Generator import Deck, Hand, Card
from Rules import Crazy_Eight_Rules as CERules
import random

HAND_SIZE = 5
crazy_eights = CERules()

def get_valid_card(card_input: str, hand_length: int) -> int:
    while not card_input.isdigit() or int(card_input) < 0 or\
    int(card_input) >= hand_length:
        card_input = input("Invalid input. Please enter a valid card number: ")
    return int(card_input)

class Game:
    def __init__(self, deck_filename: str, ruleset, hand_size= HAND_SIZE):
        self.deck = Deck(deck_filename)
        self.player1_hand = Hand(hand_size, self.deck)
        self.player2_hand = Hand(hand_size, self.deck)
        self.ruleset = ruleset

    def play(self):
        self.shuffle_deck()
        print("Both players drawing hands...")

        top_card = self.deck.deck[0]
        print("Top card is:", top_card)
        win_con = self.check_win()
        while not win_con:
            # Player 1's turn
            # print("Player 1's turn:")
            # print("Player 1's hand:", self.player1_hand)
            # played_card = get_valid_card(input("Which card do you want to play? " \
            #     "Please enter the number of the card in your hand: "), len(self.player1_hand.hand))
            # played_card = self.player1_hand.hand[played_card]

            # while not self.ruleset.comparison(top_card, played_card):
            #     played_card = get_valid_card(input("Card breaks rules. " \
            #         "Please choose a valid card: "), len(self.player1_hand.hand))
            #     played_card = self.player1_hand.hand[played_card]

            # print(f"Player 1 played: {played_card}")
            # top_card = played_card
            # self.player1_hand.remove_card(played_card)

            print("Player 1's turn:")
            print("Player 1's hand:", self.player1_hand)
            played_card = crazy_eights.make_decision(self.player1_hand, top_card)
            print(f"Player 1 played: {played_card}")
            top_card = played_card
            self.player1_hand.remove_card(played_card)

            # Player 2's turn
            print("Player 2's turn:")
            print("Player 2's hand:", self.player2_hand)
            played_card = crazy_eights.make_decision(self.player2_hand, top_card)
            print(f"Player 2 played: {played_card}")
            top_card = played_card
            self.player2_hand.remove_card(played_card)

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

crazy_eights_game = Game("Classic_Deck.txt", CERules(), HAND_SIZE)
crazy_eights_game.play()