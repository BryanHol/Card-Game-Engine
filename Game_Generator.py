from Hand_Generator import Deck, Hand
from Rules import Crazy_Eight_Rules as CERules

class Game:
    def __init__(self, deck_filename: str, ruleset: CERules):
        self.ruleset = ruleset
        self.deck = Deck(deck_filename)
        self.discard_pile = Deck()
        self.players = []

    def play(self):
        self.players = self.ruleset.start_state(self.deck, self.discard_pile)
        win_con = self.ruleset.check_win(self.players)

        while not win_con:
            for player in self.players:
                if player.human:
                    self.manual_play(player.name, player.hand)
                else:
                    print(f"Computer's ({player.name}) turn...")
                    self.auto_play(player.name, player.hand)
                win_con = self.ruleset.check_win(self.players)
                if win_con:
                    break

    def manual_play(self, player: str, hand: Hand):
        """
        This function is for manual play, where players can input their moves.
        """
        print(f"{player}'s turn. {hand}") 
        card = self.ruleset.process_choice(hand, self.deck, self.discard_pile)
        self.ruleset.play_card(hand, card, player, self.discard_pile)

    def auto_play(self, player: str, hand: Hand):
        """
        This function is for automatic play, where the game plays itself.
        """
        print(f"{player}'s turn. {hand}")
        card = self.ruleset.make_decision(hand, self.deck, self.discard_pile)
        self.ruleset.play_card(hand, card, player, self.discard_pile)


crazy_eights_game = Game("Classic_Deck.txt", CERules())
crazy_eights_game.play()