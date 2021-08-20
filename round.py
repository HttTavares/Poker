from deck import Deck
from player import Player

### bet = largest stake from a player, starts as big blind = small blind * 2.
### stake = current amount a player is gonna give to the pot once the round ends.
#Once a player stakes money, it can only be recovered if this player wins the pot.
### pot = amount of money collected on the round by bets.

class Round():
    def __init__(self, info):
        self.__info = info
        self.end = False

    def get_players(self):
        return self.__info['Players']

    def get_game(self):
        return self.__info['Game']

    def get_info(self, info_name):
        return self.__info[info_name]

    def get_current_turn(self):
        return self.__info['Current Turn']

    def get_number_players(self):
        return len(self.__info['Players'])

    def get_current_player(self):
        return self.__info['Current Player']

    def get_current_bet(self):
        return self.__info['Current Bet']

    def get_pot(self):
        return self.__info['Pot']

    def next_player(self):
        # print(len(self.get_players()))
        current = self.get_current_player()
        self.perform_move()

    def pass_player(self):
        current = self.get_current_player()
        index = self.get_players().index( current )
        if current == self.get_players()[-1]:
            self.__info['Current Player'] = self.get_players()[0]
        else:
            self.__info['Current Player'] = self.get_players()[ index + 1 ]

    def fold_move(self):
        if len(self.get_players()) <= 1:
            pass
        current = self.get_current_player()
        self.pass_player()
        player_name = current.get_name()
        self.remove_player(player_name)
        if len(self.get_players()) <= 1:
            self.end_round()

    def remove_player(self, player_name):
        for pl in self.get_players():
            if pl.get_name() == player_name:
                self.get_players().remove(pl)

    def check_move(self):
        self.pass_player()

    def set_bet(self, amount):
        self.__info['Current Bet'] = amount

    def raise_move(self):
        amount = int(input('how much to raise: '))
        player = self.get_current_player()
        stake = player.get_current_stake()
        bet = self.get_current_bet()
        if (amount > 0):
            if (stake + amount > bet):
                print('amount: ' + str(amount))
                print('stake: ' + str(stake))
                print('bet: ' + str(bet))
                player.place_bet( amount )
                player.set_current_stake( amount + stake )
                self.set_bet( amount + stake )
                print('amount: ' + str(amount))
                print('stake: ' + str(stake))
                print('bet: ' + str(bet))
                self.pass_player()
            else:
                print('you have to raise more money')
                self.raise_move()
        else:
            print('please type a positive number')
            self.raise_move()

    def call_move(self):
        player = self.get_current_player()
        stake = player.get_current_stake()
        bet = self.get_current_bet()
        print('stake: ' + str(stake))
        print('bet: ' + str(bet))
        print('money: ' + str( player.get_money() ))
        # print('stake: ' + str())
        if stake < bet:
            player.place_bet( bet - stake )
            player.set_current_stake( bet )
        self.pass_player()

    def quit_move(self):
        player_name = self.get_current_player().get_name()
        self.pass_player()
        self.get_game().remove_player(player_name)
        self.game.remove_player(player_name)
        self.remove_player(player_name)
        if len(self.game.get_players()) <= 1:
            self.end_round()

    def perform_move(self):
        print(self.get_game().get_rounds())
        print('Current player is: ' + self.get_current_player().get_name())
        move = input('Action: ')
        index = self.get_players().index(self.__info['Current Player'])
        if move == 'q':
            self.quit_move()
        elif move == 'f':
            self.fold_move()
        elif move == 'h':
            self.check_move()
        elif move == 'a':
            self.call_move()
        elif move == 'r':
            self.raise_move()
        else:
            print('choose among q, f, ch, ca, r')
            self.perform_move()

    def get_current_round(self):
        return self.__info['Current Round']

    def next_player_turn(self):
        self.next_player()
        print('turn: ' + str( self.get_current_turn() ))

    def end_round(self):
        self.end = True
        print(f"Round {self.get_current_round()} has ended" )
        # del self

    def start(self, game_object):
        self.add_game(game_object)
        while self.end == False:
            self.perform_move()

    def change_pot(self, amount):
        pot = self.get_pot()
        pot += amount

    def add_game(self, game_object):
        self.game = game_object

    def get_player(self, player_name):
        for player in self.get_players():
            if player.get_name() == player_name:
                return player

    def define_winner(self, player_name):
        player = self.get_player(player_name)

if __name__ == '__main__':
    pass
