#!flask/bin/python
from flask import Flask, jsonify, request
import lib.dice
import lib.gamestatestate
import backgammon

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to backgammon."

@app.route('/start/')
def roll_die():
    die = dice.oneDie(6)
    gf = die.goesFirst()

    t = gf[0]
    r = gf[1]

    st = state.state(t, r)
    print st.board
    return jsonify({"state": st.board.tolist()})

@app.route('/move/', methods=['POST'])
def return_comp_move():
    incoming_state = request.json['state']
    comp_move = backgammon.playStrategicCompTurn(state.state(incoming_state))
    return jsonify({"state":comp_move.board.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
