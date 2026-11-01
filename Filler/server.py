# Andrey Vasilyev 4/21/24
import boards
import solve
import json
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__, static_folder='', template_folder='')

board = boards.Board()  # instantiate the board
board.create_random(seed=None)  # create a random board

depth = 2

current_move = False

@app.before_request
def load_game():
    global board, current_move
    from flask import g
    # Request-local boards avoid sharing state across players or workers.
    board_state = boards.Board()
    try:
        state = json.loads(request.cookies.get('filler_game', '{}'))
        cells, owners = state['board'], state['owners']
        assert len(cells) == len(owners) == 7
        assert all(len(row) == 8 for row in cells + owners)
        assert all(cell in board_state.tiles for row in cells for cell in row)
        assert all(owner in (None, 0, 1) for row in owners for owner in row)
        board_state.board, board_state.player_board = cells, owners
        g.turn = bool(state.get('turn', False))
    except (KeyError, ValueError, TypeError, AssertionError):
        board_state.create_random()
        g.turn = False
    g.board = board_state

@app.after_request
def save_game(response):
    from flask import g
    if hasattr(g, 'board'):
        response.set_cookie('filler_game', json.dumps({'board': g.board.board, 'owners': g.board.player_board, 'turn': g.turn}), httponly=True, samesite='Lax')
    return response

from werkzeug.local import LocalProxy
from flask import g
board = LocalProxy(lambda: g.board)

@app.route('/')
def index():
    return render_template('index.html', board=board.board)


@app.route('/handle_input', methods=['POST'])
def handle_input():
    data = request.json
    move = data.get('input')
    if move not in board.get_legal_moves(0):
        return render_template('index.html', board=board.board)
    g.board = board.add_move(move=move, player=0)  # add user move to the board
    solver = solve.Solver(player=1, maxdepth=depth)  # instantiate new solver
    opp_move, _ = solver.choose_move(board=board, depth=0)
    if opp_move is not None:
        g.board = board.add_move(move=opp_move, player=1)
    return render_template('index.html', board=board.board)


@app.route('/twoplayerinput', methods=['POST'])
def twoplayerinput():
    data = request.json
    move = data.get('input')
    if move not in board.get_legal_moves(int(g.turn)):
        return render_template('twoplayer.html', board=board.board)
    g.board = board.add_move(move=move, player=int(g.turn))
    g.turn = not g.turn
    return render_template('twoplayer.html', board=board.board)

@app.route('/fetch', methods=['GET'])
def fetch():
    return board.print_score()


@app.route('/info', methods=['GET'])
def info():
    return render_template('info.html')


@app.route('/two_player', methods=['GET'])
def two_player():
    return render_template('twoplayer.html', board=board.board)


@app.route('/play', methods=['POST'])
def play():
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
