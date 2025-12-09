from flask import Flask, render_template, request, jsonify, session
import secrets
from kivi_paperi_sakset_tehdas import KiviPaperiSaksetTehdas
from tuomari import Tuomari

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Store active games in memory
games = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/new_game', methods=['POST'])
def new_game():
    """Start a new game with the selected mode."""
    data = request.json
    game_type = data.get('game_type')
    
    # Create a unique game ID for this session
    game_id = secrets.token_hex(8)
    
    # Create game using the factory
    tehdas = KiviPaperiSaksetTehdas()
    peli = tehdas.luo_peli(game_type)
    
    if peli is None:
        return jsonify({'error': 'Invalid game type'}), 400
    
    # Create a fresh Tuomari to avoid shared state issues
    fresh_tuomari = Tuomari()
    peli._tuomari = fresh_tuomari
    
    # Store game state
    games[game_id] = {
        'peli': peli,
        'tuomari': fresh_tuomari,
        'game_type': game_type,
        'game_over': False,
        'first_move': True
    }
    
    return jsonify({
        'game_id': game_id,
        'game_type': game_type,
        'message': 'Game started!'
    })

@app.route('/api/make_move', methods=['POST'])
def make_move():
    """Process a player's move."""
    data = request.json
    game_id = data.get('game_id')
    player_move = data.get('move')
    
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    game_state = games[game_id]
    
    if game_state['game_over']:
        return jsonify({'error': 'Game is over'}), 400
    
    # Validate move
    if player_move not in ['k', 'p', 's']:
        game_state['game_over'] = True
        return jsonify({
            'game_over': True,
            'message': 'Invalid move. Game over!',
            'final_scores': {
                'player1': game_state['tuomari'].ekan_pisteet,
                'player2': game_state['tuomari'].tokan_pisteet,
                'ties': game_state['tuomari'].tasapelit
            }
        })
    
    peli = game_state['peli']
    
    # Get computer/player2 move
    if game_state['game_type'] == 'a':
        # Player vs Player - validate move2
        computer_move = data.get('move2', 'k')
        if computer_move not in ['k', 'p', 's']:
            game_state['game_over'] = True
            return jsonify({
                'game_over': True,
                'message': 'Invalid move by player 2. Game over!',
                'final_scores': {
                    'player1': game_state['tuomari'].ekan_pisteet,
                    'player2': game_state['tuomari'].tokan_pisteet,
                    'ties': game_state['tuomari'].tasapelit
                }
            })
    else:
        # AI move
        computer_move = peli.tokan_siirto()
    
    # Record the move
    game_state['tuomari'].kirjaa_siirto(player_move, computer_move)
    
    # Update AI state if needed
    if game_state['game_type'] == 'c':
        peli._tekoaly.aseta_siirto(player_move)
    
    # Check if either player has won 5 rounds
    player1_score = game_state['tuomari'].ekan_pisteet
    player2_score = game_state['tuomari'].tokan_pisteet
    
    if player1_score >= 5 or player2_score >= 5:
        game_state['game_over'] = True
        return jsonify({
            'player_move': player_move,
            'computer_move': computer_move,
            'game_over': True,
            'message': 'Game over! A player won 5 rounds!',
            'final_scores': {
                'player1': player1_score,
                'player2': player2_score,
                'ties': game_state['tuomari'].tasapelit
            }
        })
    
    # Prepare response
    response = {
        'player_move': player_move,
        'computer_move': computer_move,
        'scores': {
            'player1': player1_score,
            'player2': player2_score,
            'ties': game_state['tuomari'].tasapelit
        },
        'game_over': False
    }
    
    return jsonify(response)

@app.route('/api/end_game', methods=['POST'])
def end_game():
    """End the current game."""
    data = request.json
    game_id = data.get('game_id')
    
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    game_state = games[game_id]
    game_state['game_over'] = True
    
    return jsonify({
        'message': 'Game ended',
        'final_scores': {
            'player1': game_state['tuomari'].ekan_pisteet,
            'player2': game_state['tuomari'].tokan_pisteet,
            'ties': game_state['tuomari'].tasapelit
        }
    })

@app.route('/api/game_state/<game_id>', methods=['GET'])
def get_game_state(game_id):
    """Get current game state."""
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    game_state = games[game_id]
    
    return jsonify({
        'game_type': game_state['game_type'],
        'game_over': game_state['game_over'],
        'scores': {
            'player1': game_state['tuomari'].ekan_pisteet,
            'player2': game_state['tuomari'].tokan_pisteet,
            'ties': game_state['tuomari'].tasapelit
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
