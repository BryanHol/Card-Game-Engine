from Hand_Generator import Deck, Hand, Card
from Rules import Crazy_Eight_Rules as CERules
import random

crazy_eights = CERules()

class Game:
    def __init__(self, deck_filename: str, ruleset: CERules):
        self.ruleset = ruleset
        self.hand_size = self.ruleset.hand_size
        self.deck = Deck(deck_filename)
        self.player1_hand = Hand(self.hand_size, self.deck)
        self.player2_hand = Hand(self.hand_size, self.deck)
        self.deck.shuffle_deck()
        print("Both players drawing hands...")
        self.top_card = self.deck.deck[0]
        self.discard_pile = Deck()
        self.max_players = self.ruleset.max_players

    def play(self):
        print("Top card is:", self.top_card)
        self.ruleset.start_state(self.deck, self.discard_pile, self.top_card)
        num_players = int(input("How many players? (0, 1, or 2): "))
        player_list = []
        player_hands = []
        for player in player_list:
            player_hands.append(Hand(self.hand_size, self.deck))

        win_con = self.check_win(player_hands)
        for i in range(num_players): #Real players
            player_list.append("Real " + str(i+1))
        for i in range(self.max_players - num_players): #Auto players
            player_list.append("Auto " + str(i+1))
        
        if num_players == 1:
            player_list[1] = "Auto 2"

        while not win_con:
            for player in player_list:
                if "Real" in player:
                    player_num = player.split(" ")[1]
                    self.manual_play(player_num, self.player1_hand if player_num == "1" else self.player2_hand)
                else:
                    player_num = player.split(" ")[1]
                    print(f"Computer's ({player}) turn...")
                    self.auto_play(player_num, self.player1_hand if player_num == "1" else self.player2_hand)
                win_con = self.check_win(player_hands)
                if win_con:
                    break

    def check_win(self, players: list) -> bool:
        if len(self.player1_hand.hand) == 0:
            print("Player 1 wins!")
            return True
        elif len(self.player2_hand.hand) == 0:
            print("Player 2 wins!")
            return True
        return False

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
            played_card = crazy_eights.get_valid_card(input("Which card do you want to play? " \
                "Enter the number of the card (Enter draw to draw a card): "),\
                    len(hand.hand))
            while played_card == -1:
                print("Drawing a card...")
                card = hand.deck.deck[0]
                hand.deck.deck.remove(card)
                hand.hand.append(card)
                print("You drew:", card)
                self.ruleset.check_deck(self.deck, self.discard_pile)
                played_card = crazy_eights.get_valid_card(input("Do you want to play a card or draw again?"), len(hand.hand))
            played_card = hand.hand[played_card]
        else:
            while not valid_cards:
                print("No valid cards to play. Drawing a card...")
                card = hand.deck.deck[0]
                hand.deck.deck.remove(card)
                hand.hand.append(card)
                print("You drew:", card)
                self.ruleset.check_deck(self.deck, self.discard_pile)
                if self.ruleset.comparison(self.top_card, card):
                    valid_cards.append(card)
            played_card = crazy_eights.get_valid_card(input("Which card do you want to play? " \
                "Enter the number of the card (Enter draw to draw a card): "),\
                    len(hand.hand))
            while played_card == -1:
                print("Drawing a card...")
                card = hand.deck.deck[0]
                hand.deck.deck.remove(card)
                hand.hand.append(card)
                print("You drew:", card)
                self.ruleset.check_deck(self.deck, self.discard_pile)
                played_card = crazy_eights.get_valid_card(input("Do you want to play a card or draw again?"), len(hand.hand))
            played_card = hand.hand[played_card]


        while not self.ruleset.comparison(self.top_card, played_card):
            played_card = crazy_eights.get_valid_card(input("Card breaks rules. " \
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
        
crazy_eights_game = Game("Classic_Deck.txt", CERules())
crazy_eights_game.play()