from unittest import TestCase
import json
from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<table class="board">', html)
            self.assertIn('<table', html)
            self.assertIn('boggle homepage. used in testing', html)
            # test that you're getting a template

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            response = client.get('/api/new-game')
            response_json = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("gameId", response_json)
            parsed_json = json.loads(response_json)
            self.assertEqual(type(parsed_json["gameId"]), str)
            self.assertEqual(type(parsed_json["board"]), list)
            self.assertEqual(type(parsed_json["board"][0]), list)

            # write a test for this route

    def test_api_score_word(self):
        """Test scoring a word"""

        with self.client as client:
            response = client.get('/api/new-game')
            response_json = response.get_json()
            game_id = response_json["gameId"]
            game = games[game_id]
            game.board[0] = ["A", "A","A","A","A"]
            game.board[1] = ["D", "O","G","A","A"]
            game.board[2] = ["A", "A","A","A","A"]
            game.board[3] = ["A", "A","A","A","A"]
            game.board[4] = ["A", "A","A","A","A"]

            response = client.post('/api/score-word', json={"gameId":game_id, "word": "AAAA"})
            self.assertEqual(response.get_json(), {"result":"not-word"})
            response = client.post('/api/score-word', json={"gameId":game_id, "word": "dog"})
            self.assertEqual(response.get_json(), {"result": "ok"})
            response = client.post('/api/score-word', json={"gameId":game_id, "word": "CAT"})
            self.assertEqual(response.get_json(), {"result":"not-on-board"})

                    #inside of the games dictionary, there is a instance of BoggleGame with a board and a game_id
                    # we can manualy change the board to include a word and test for test for that word.
