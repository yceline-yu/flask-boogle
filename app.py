from flask import Flask, request, render_template, jsonify, session
from uuid import uuid4
import json
from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.route("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.route("/api/new-game")
def new_game():
    """Start a new game and return JSON: {gameId, board}."""

    # get a unique id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    return jsonify({"gameId": game_id, "board": game.board})

@app.route("/api/score-word", methods=["POST"])
def check_word_is_legal():
    """check if word recieved from POST request is legal"""
    breakpoint()
    print("request.form = ", request.form)
    word = request.get_json("word")
    game_id = request.get_json("gameId")
    print("request.get_json is ", request.get_json)
    # got_json = request.get_json(force = True) #string still?
    # new_json = json.dumps(got_json)
    # game_id = new_json["gameId"]
    #need game_id from JSON and use that to index into the games dictionary 
    #for the game instance
    in_list = games[game_id].is_word_in_word_list(word)
    on_board = games[game_id].check_word_on_board(word)
    result = "hi"
    # if in_list and on_board:
    #     result = "ok"
    # if not in_list:
    #     result = "not-word"
    # if not on_board:
    #     result = "not-on-board"        
    return jsonify(result = result)
