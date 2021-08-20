class Player():
    def __init__(self, info):
        self.__info = info

    def get_name(self):
        return self.__info['Name']

    def add_game(self, game_object):
        self.__info['Game'] = game_object

    def get_game(self):
        return self.__info['Game']

    def get_money(self):
        return self.__info['Money']

    def change_money(self, amount):
        self.__info['Money'] += amount
        print('money: ' + str(self.get_money()))

    def set_current_stake(self, amount):
        self.__info['Current Stake'] = amount

    def get_current_stake(self):
        return self.__info['Current Stake']

    def quit(self):
        self.get_game().get_players().pop(self)

    def place_bet(self, amount):
        self.change_money(-amount)
        self.get_game().get_current_round().change_pot(amount)

if __name__ == '__main__':
    pass
