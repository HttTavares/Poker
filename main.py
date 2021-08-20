def init_flask_server():
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return '<h1>Hello SUP World!</h1>'
    @app.route('/seila')
    def hello_world2():
        return '<h1>SUP</h1>'

from game import Game
from player import Player

game = Game({
    'Players': [],
    'Rounds': [],
    'Small Blind': 5,

    # 'Pot': [],
})
for i in range(5):
    player = Player({
        'Name': str(i),
        'Money': 1000,
        'Current Hand': [],
        'Current Stake': 0,
        'Game': game
    })
    game.add_player(player)

# print(game.get_players())
# game.remove_player('3')
# print(game.get_players())
game.start()
