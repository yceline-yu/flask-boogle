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
