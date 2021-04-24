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
    json_as_dict = request.get_json()
    word = json_as_dict["word"].upper()
    game_id = json_as_dict["gameId"]
    print("game_id= ", game_id)
    print("word= ", word)
    in_list = games[game_id].is_word_in_word_list(word)
    on_board = games[game_id].check_word_on_board(word)
    if not in_list:
        result = "not-word"
    if not on_board:
        result = "not-on-board"
    if in_list and on_board:
        result = "ok"
    return jsonify(result=result)
