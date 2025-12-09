import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import web_app
from web_app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    # Clear games dict before each test
    web_app.games.clear()
    with app.test_client() as client:
        yield client
    # Clear again after test
    web_app.games.clear()


class TestWebApp:
    """Tests for the Flask web application."""

    def test_index_page(self, client):
        """Test that index page loads."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Kivi-Paperi-Sakset' in response.data

    def test_new_game_player_vs_player(self, client):
        """Test creating a player vs player game."""
        response = client.post('/api/new_game',
                               json={'game_type': 'a'})
        assert response.status_code == 200
        data = response.get_json()
        assert 'game_id' in data
        assert data['game_type'] == 'a'
        assert 'message' in data

    def test_new_game_vs_ai(self, client):
        """Test creating a game vs AI."""
        response = client.post('/api/new_game',
                               json={'game_type': 'b'})
        assert response.status_code == 200
        data = response.get_json()
        assert 'game_id' in data
        assert data['game_type'] == 'b'

    def test_new_game_vs_improved_ai(self, client):
        """Test creating a game vs improved AI."""
        response = client.post('/api/new_game',
                               json={'game_type': 'c'})
        assert response.status_code == 200
        data = response.get_json()
        assert 'game_id' in data
        assert data['game_type'] == 'c'

    def test_new_game_invalid_type(self, client):
        """Test creating game with invalid type."""
        response = client.post('/api/new_game',
                               json={'game_type': 'x'})
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data

    def test_make_move_rock(self, client):
        """Test making a rock move."""
        # Create game first
        response = client.post('/api/new_game',
                               json={'game_type': 'b'})
        game_id = response.get_json()['game_id']

        # Make move
        response = client.post('/api/make_move',
                               json={'game_id': game_id, 'move': 'k'})
        assert response.status_code == 200
        data = response.get_json()
        assert data['player_move'] == 'k'
        assert data['computer_move'] in ['k', 'p', 's']
        assert 'scores' in data

    def test_make_move_paper(self, client):
        """Test making a paper move."""
        response = client.post('/api/new_game',
                               json={'game_type': 'b'})
        game_id = response.get_json()['game_id']

        response = client.post('/api/make_move',
                               json={'game_id': game_id, 'move': 'p'})
        assert response.status_code == 200
        data = response.get_json()
        assert data['player_move'] == 'p'

    def test_make_move_scissors(self, client):
        """Test making a scissors move."""
        response = client.post('/api/new_game',
                               json={'game_type': 'b'})
        game_id = response.get_json()['game_id']

        response = client.post('/api/make_move',
                               json={'game_id': game_id, 'move': 's'})
        assert response.status_code == 200
        data = response.get_json()
        assert data['player_move'] == 's'

    def test_make_move_invalid(self, client):
        """Test making an invalid move ends the game."""
        response = client.post('/api/new_game',
                               json={'game_type': 'b'})
        game_id = response.get_json()['game_id']

        response = client.post('/api/make_move',
                               json={'game_id': game_id, 'move': 'x'})
        assert response.status_code == 200
        data = response.get_json()
        assert data['game_over'] is True
        assert 'final_scores' in data

    def test_make_move_nonexistent_game(self, client):
        """Test making move for non-existent game."""
        response = client.post('/api/make_move',
                               json={'game_id': 'fake_id', 'move': 'k'})
        assert response.status_code == 404

    def test_score_tracking(self, client):
        """Test that scores are tracked correctly."""
        response = client.post('/api/new_game',
                               json={'game_type': 'b'})
        game_id = response.get_json()['game_id']

        # Make several moves
        for _ in range(3):
            response = client.post('/api/make_move',
                                   json={'game_id': game_id, 'move': 'k'})
            data = response.get_json()
            assert 'scores' in data
            scores = data['scores']
            assert 'player1' in scores
            assert 'player2' in scores
            assert 'ties' in scores
            # Verify scores are non-negative integers
            assert scores['player1'] >= 0
            assert scores['player2'] >= 0
            assert scores['ties'] >= 0

    def test_end_game(self, client):
        """Test ending a game."""
        response = client.post('/api/new_game',
                               json={'game_type': 'b'})
        game_id = response.get_json()['game_id']

        # Make a move
        client.post('/api/make_move',
                    json={'game_id': game_id, 'move': 'k'})

        # End game
        response = client.post('/api/end_game',
                               json={'game_id': game_id})
        assert response.status_code == 200
        data = response.get_json()
        assert 'final_scores' in data
        assert 'message' in data

    def test_end_nonexistent_game(self, client):
        """Test ending non-existent game."""
        response = client.post('/api/end_game',
                               json={'game_id': 'fake_id'})
        assert response.status_code == 404

    def test_get_game_state(self, client):
        """Test getting game state."""
        response = client.post('/api/new_game',
                               json={'game_type': 'c'})
        game_id = response.get_json()['game_id']

        response = client.get(f'/api/game_state/{game_id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['game_type'] == 'c'
        assert data['game_over'] is False
        assert 'scores' in data

    def test_get_nonexistent_game_state(self, client):
        """Test getting state of non-existent game."""
        response = client.get('/api/game_state/fake_id')
        assert response.status_code == 404

    def test_multiple_games(self, client):
        """Test creating and managing multiple games."""
        # Create two different games
        response1 = client.post('/api/new_game',
                                json={'game_type': 'b'})
        game_id1 = response1.get_json()['game_id']

        response2 = client.post('/api/new_game',
                                json={'game_type': 'c'})
        game_id2 = response2.get_json()['game_id']

        assert game_id1 != game_id2

        # Make moves in both games
        response1 = client.post('/api/make_move',
                                json={'game_id': game_id1, 'move': 'k'})
        assert response1.status_code == 200

        response2 = client.post('/api/make_move',
                                json={'game_id': game_id2, 'move': 'p'})
        assert response2.status_code == 200

    def test_full_game_flow(self, client):
        """Test a complete game flow."""
        # Start game
        response = client.post('/api/new_game',
                               json={'game_type': 'b'})
        assert response.status_code == 200
        game_id = response.get_json()['game_id']

        # Play several rounds (but not enough to win)
        moves = ['k', 'p', 's', 'k']
        for move in moves:
            # Check if game is already over before making move
            state_response = client.get(f'/api/game_state/{game_id}')
            if state_response.get_json()['game_over']:
                break
                
            response = client.post('/api/make_move',
                                   json={'game_id': game_id, 'move': move})
            
            # If game is still going, should be 200
            # If game ended due to 5 wins, that's ok too
            if response.status_code == 200:
                data = response.get_json()
                # Only check game_over status if we got valid response
                if data.get('game_over'):
                    # Game ended at 5 wins
                    assert 'final_scores' in data
                    break

        # If game isn't over yet, end it manually
        state_response = client.get(f'/api/game_state/{game_id}')
        if not state_response.get_json()['game_over']:
            response = client.post('/api/end_game',
                                   json={'game_id': game_id})
            assert response.status_code == 200
            assert 'final_scores' in response.get_json()

    def test_player_vs_player_mode(self, client):
        """Test player vs player mode with both moves."""
        response = client.post('/api/new_game',
                               json={'game_type': 'a'})
        game_id = response.get_json()['game_id']

        # Make move with both players
        response = client.post('/api/make_move',
                               json={'game_id': game_id, 
                                     'move': 'k', 
                                     'move2': 'p'})
        assert response.status_code == 200
        data = response.get_json()
        assert data['player_move'] == 'k'
        assert data['computer_move'] == 'p'

    def test_game_ends_at_five_wins(self, client):
        """Test that game automatically ends when a player wins 5 rounds."""
        response = client.post('/api/new_game',
                               json={'game_type': 'a'})
        game_id = response.get_json()['game_id']

        # Player 1 wins 5 rounds
        for i in range(5):
            response = client.post('/api/make_move',
                                   json={'game_id': game_id, 
                                         'move': 'k',  # rock
                                         'move2': 's'})  # scissors - player 1 wins
            data = response.get_json()
            
            if i < 4:
                # First 4 wins, game continues
                assert data['game_over'] is False, f"Game ended too early at round {i}: {data}"
                assert data['scores']['player1'] == i + 1
            else:
                # 5th win, game ends
                assert data['game_over'] is True
                assert 'final_scores' in data
                assert data['final_scores']['player1'] == 5
                assert 'message' in data

    def test_game_ends_when_player2_wins_five(self, client):
        """Test that game automatically ends when player 2 wins 5 rounds."""
        response = client.post('/api/new_game',
                               json={'game_type': 'a'})
        game_id = response.get_json()['game_id']

        # Player 2 wins 5 rounds
        for i in range(5):
            response = client.post('/api/make_move',
                                   json={'game_id': game_id, 
                                         'move': 's',  # scissors
                                         'move2': 'k'})  # rock - player 2 wins
            data = response.get_json()
            
            if i < 4:
                # First 4 wins, game continues
                assert data['game_over'] is False, f"Game ended too early at round {i}: {data}"
                assert data['scores']['player2'] == i + 1
            else:
                # 5th win, game ends
                assert data['game_over'] is True
                assert 'final_scores' in data
                assert data['final_scores']['player2'] == 5

    def test_game_continues_with_ties(self, client):
        """Test that ties don't count toward the 5-win requirement."""
        response = client.post('/api/new_game',
                               json={'game_type': 'a'})
        game_id = response.get_json()['game_id']

        # Multiple ties
        for _ in range(3):
            response = client.post('/api/make_move',
                                   json={'game_id': game_id, 
                                         'move': 'k',
                                         'move2': 'k'})  # tie
            data = response.get_json()
            assert data['game_over'] is False
            assert data['scores']['ties'] > 0

        # Player 1 wins 4 rounds (not enough to win)
        for _ in range(4):
            response = client.post('/api/make_move',
                                   json={'game_id': game_id, 
                                         'move': 'k',
                                         'move2': 's'})
            data = response.get_json()
            assert data['game_over'] is False

