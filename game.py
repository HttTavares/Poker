# from gamewindow import GameWindow
from round import Round

class Game():
    def __init__(self, info):
        self.__info = info
        self.start()

    def add_player(self, player_object):
        self.get_players().append(player_object)
        player_object.add_game(self)

    def remove_player(self, player_name):
        for pl in self.get_players():
            if pl.get_name() == player_name:
                self.get_players().remove(pl)

    def get_small_blind(self):
        return self.__info['Small Blind']

    def get_rounds(self):
        return self.__info['Rounds']

    def get_current_round(self):
        return self.__info['Rounds'][-1]

    def add_round(self):
        self.get_rounds().append(Round({
            'Players': self.get_players().copy(),
            'Current Player': self.get_players()[0],
            'Current Round': len(self.get_rounds()) + 1,
            'Game': self,
            'Pot': 0,
            'Current Bet': self.get_small_blind()*2
        }))

    def start(self):
        while self.get_number_players() > 1:
            # round = Round({
            #     'Players': self.get_players().copy(),
            #     'Current Player': self.get_players()[0],
            #     'Current Round': 1,
            #     'Game': self,
            #     'Pot': 0,
            #     'Current Bet': self.get_small_blind()*2
            # })
            # round.start(self)
            self.add_round()
            self.get_current_round().start(self)
        print('game is over')

        # if self.__info['Current Player'] == 'User':
        #     round = Round({
        #         'Number of Players':
        #     })

        # show_hands = False
        # game_window = GameWindow()
        # while show_hands == False:
        #     self.next_player_turn()

    def get_players(self):
        return self.__info['Players']

    def get_number_players(self):
        return len(self.__info['Players'])

    def next_round(self):
        pass

    def end():
        pass



if __name__ == '__main__':
    game = Game({
        # 'Current Player': 'User',
        'Current Round': 0,
        'Number of Players': 4
    })
