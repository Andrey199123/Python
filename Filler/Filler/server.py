# Andrey Vasilyev 4/21/24
import boards
import solve
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__, static_folder='', template_folder='')

board = boards.Board()  # instantiate the board
board.create_random(seed=None)  # create a random board

depth = None


@app.route('/')
def index():
    return render_template('index.html', board=board.board)


@app.route('/handle_input', methods=['POST'])
def handle_input():
    global board
    data = request.json
    move = data.get('input')
    if move not in board.get_legal_moves(0):
        return render_template('index.html', board=board.board)
    if move == "q":
        return "Game over!"
    board = board.add_move(move=move, player=0)  # add user move to the board
    solver = solve.Solver(player=1, maxdepth=depth)  # instantiate new solver
    opp_move, _ = solver.choose_move(board=board, depth=depth)  # choose move for opponent
    board = board.add_move(move=opp_move, player=1)  # add opponent move to the board
    return render_template('index.html', board=board.board)


@app.route('/fetch', methods=['GET'])
def fetch():
    return board.print_score()


@app.route('/info', methods=['GET'])
def info():
    return render_template('info.html')


@app.route('/play', methods=['POST'])
def play():
    app.run(debug=True)


depth = int(input("Choose your difficulty 1-10: "))
if not 0 < depth < 11:
    depth = 10
play()
