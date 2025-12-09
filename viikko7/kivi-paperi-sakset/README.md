# Kivi-Paperi-Sakset (Rock-Paper-Scissors)

A comprehensive Rock-Paper-Scissors game implementation with multiple game modes, available both as a command-line interface and web application.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Modes](#game-modes)
- [Running the Application](#running-the-application)

## Features

- **Multiple Game Modes**:
  - Player vs Player
  - Player vs Basic AI
  - Player vs Advanced AI (with memory)
- **Two Interfaces**:
  - Command-line interface (CLI)
  - Web interface (Flask-based)
- **Smart AI**:
  - Basic AI with predictable patterns
  - Advanced AI that learns from your moves

## Project Structure

```
kivi-paperi-sakset/
├── src/
│   ├── index.py                      # CLI entry point
│   ├── web_app.py                    # Flask web application
│   ├── kivi_paperi_sakset.py         # Base game class (abstract)
│   ├── kivi_paperi_sakset_tehdas.py  # Factory pattern implementation
│   ├── kps_pelaaja_vs_pelaaja.py     # Player vs Player mode
│   ├── kps_tekoaly.py                # Player vs Basic AI mode
│   ├── kps_parempi_tekoaly.py        # Player vs Advanced AI mode
│   ├── tuomari.py                    # Referee/score keeper
│   ├── tekoaly.py                    # Basic AI implementation
│   ├── tekoaly_parannettu.py         # Advanced AI with memory
│   ├── templates/
│   │   └── index.html                # Web UI template
│   ├── static/
│   │   └── style.css                 # Web UI styles
│   └── tests/                        # Unit tests
├── pyproject.toml                    # Poetry dependencies
└── README.md                         # This file
```

## Architecture

The application follows several design patterns for maintainability and extensibility:

### 1. Factory Pattern
**File**: `kivi_paperi_sakset_tehdas.py`

The `KiviPaperiSaksetTehdas` class creates different game mode instances based on user selection:
```python
factory = KiviPaperiSaksetTehdas()
game = factory.luo_peli('a')  # Creates Player vs Player game
```

### 2. Template Method Pattern
**Base Class**: `kivi_paperi_sakset.py`

The base class `KiviPaperiSakset` defines the game flow, with subclasses implementing specific behaviors:
- `pelaa()`: Main game loop (template method)
- `tokan_siirto()`: Must be overridden by subclasses
- `siirron_asettaminen()`: Must be overridden by subclasses

### 3. Strategy Pattern
**AI Implementations**: `tekoaly.py`, `tekoaly_parannettu.py`

Different AI strategies can be plugged into the game:
- **Basic AI** (`Tekoaly`): Cycles through moves predictably (rock → paper → scissors)
- **Advanced AI** (`TekoalyParannettu`): Remembers player's previous moves and predicts next move

### Class Diagram

```
┌─────────────────────────────┐
│   KiviPaperiSakset          │  (Abstract Base Class)
│  ─────────────────────────  │
│  - _tuomari: Tuomari        │
│  ─────────────────────────  │
│  + pelaa()                  │
│  + tee_siirrot()            │
│  + ekan_siirto()            │
│  # tokan_siirto()*          │  * = Must override
│  # siirron_asettaminen()*   │
└─────────────────────────────┘
           △
           │
           │ (inherits)
    ┌──────┴──────────────────┬──────────────────────┐
    │                         │                      │
┌───────────────────┐  ┌──────────────┐  ┌────────────────────┐
│KPSPelaajaVsPelaaja│  │ KPSTekoaly   │  │KPSParempiTekoaly   │
│───────────────────│  │──────────────│  │────────────────────│
│                   │  │- _tekoaly    │  │- _tekoaly          │
│                   │  │  :Tekoaly    │  │  :TekoalyParannettu│
└───────────────────┘  └──────────────┘  └────────────────────┘

┌─────────────────────┐       ┌──────────────────────┐
│      Tuomari        │       │  Tekoaly             │
│─────────────────────│       │──────────────────────│
│- ekan_pisteet: int  │       │- _siirto: int        │
│- tokan_pisteet: int │       │──────────────────────│
│- tasapelit: int     │       │+ anna_siirto(): str  │
│─────────────────────│       │+ aseta_siirto(str)   │
│+ kirjaa_siirto()    │       └──────────────────────┘
└─────────────────────┘                △
                                       │
                              ┌────────┴─────────────┐
                              │ TekoalyParannettu    │
                              │──────────────────────│
                              │- _muisti: list       │
                              │- _vapaa_muisti_      │
                              │  indeksi: int        │
                              │──────────────────────│
                              │+ anna_siirto(): str  │
                              │+ aseta_siirto(str)   │
                              └──────────────────────┘
```

### Component Responsibilities

#### Core Components

1. **Tuomari (Referee)**
   - Tracks scores for both players
   - Counts ties
   - Determines round winners
   - Displays game statistics

2. **KiviPaperiSakset (Base Game)**
   - Manages game flow and main loop
   - Validates moves (k/p/s)
   - Coordinates between players and referee

3. **Game Mode Implementations**
   - **KPSPelaajaVsPelaaja**: Both moves come from user input
   - **KPSTekoaly**: Second player is basic AI
   - **KPSParempiTekoaly**: Second player is advanced AI

4. **AI Strategies**
   - **Tekoaly**: Simple cycling algorithm
   - **TekoalyParannettu**: Pattern recognition with memory buffer

## Installation

### Prerequisites
- Python 3.12 or higher
- Poetry (Python package manager)

### Setup

1. Clone the repository or navigate to the project directory:
```bash
cd /home/saara/projects/ohtu/palautusrepositorio/viikko7/kivi-paperi-sakset
```

2. Install dependencies using Poetry:
```bash
poetry install
```

## How to Play

### Game Rules

Rock-Paper-Scissors is a simple hand game with three possible moves:
- **k** (kivi/rock): Beats scissors
- **p** (paperi/paper): Beats rock
- **s** (sakset/scissors): Beats paper

### Move Selection

In each round:
1. Player 1 selects their move (k, p, or s)
2. Player 2 (or AI) selects their move
3. The referee determines the winner:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
   - Same moves = Tie

### Winning

- **CLI Mode**: Game continues until an invalid move is entered
- **Web Mode**: First player to win 5 rounds wins the game

### Valid Moves
- `k` = Kivi (Rock) 🪨
- `p` = Paperi (Paper) 📄
- `s` = Sakset (Scissors) ✂️

Any other input ends the game in CLI mode.

## Game Modes

### Mode A: Player vs Player
Both players enter their moves. Best for playing with a friend on the same device.

### Mode B: Player vs Basic AI
Play against a simple AI that cycles through moves predictably:
- Round 1: Rock
- Round 2: Paper
- Round 3: Scissors
- (repeats)

**Strategy Tip**: The pattern is predictable - you can easily win once you figure it out!

### Mode C: Player vs Advanced AI
Play against an AI with memory that learns from your patterns:
- Remembers your last 10 moves (configurable)
- Predicts your next move based on past behavior
- Adapts its strategy to counter your patterns

**Strategy Tip**: Try to be random and unpredictable to beat this AI!

## Running the Application

### Command-Line Interface (CLI)

Run the CLI version:
```bash
poetry run python src/index.py
```

You'll see:
```
Valitse pelataanko
 (a) Ihmistä vastaan
 (b) Tekoälyä vastaan
 (c) Parannettua tekoälyä vastaan
Muilla valinnoilla lopetetaan
```

Enter `a`, `b`, or `c` to select a game mode, then follow the prompts.

**Example CLI Session:**
```
Valitse pelataanko
 (a) Ihmistä vastaan
 (b) Tekoälyä vastaan
 (c) Parannettua tekoälyä vastaan
Muilla valinnoilla lopetetaan
> b

Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s
Ensimmäisen pelaajan siirto: k
Tietokone valitsi: k
Pelitilanne: 0 - 0
Tasapelit: 1

Ensimmäisen pelaajan siirto: p
Tietokone valitsi: p
Pelitilanne: 0 - 0
Tasapelit: 2

Ensimmäisen pelaajan siirto: k
Tietokone valitsi: s
Pelitilanne: 1 - 0
Tasapelit: 2
```

### Web Interface

Run the Flask web application:
```bash
poetry run flask --app src/web_app run
```

Or with auto-reload for development:
```bash
FLASK_APP=src/web_app FLASK_DEBUG=1 poetry run flask run
```

Then open your browser to:
```
http://127.0.0.1:5000/
```

**Web Interface Features:**
- Visual button interface for selecting moves
- Real-time score tracking
- Move history display
- Automatic game-over detection (first to 5 wins)
- Clean, responsive design

### Running Tests

Run the test suite:
```bash
poetry run pytest
```

Run tests with coverage:
```bash
poetry run pytest --cov=src
```

## API Documentation (Web App)

The web application provides a REST API:

### POST `/api/new_game`
Start a new game.

**Request Body:**
```json
{
  "game_type": "a"  // "a", "b", or "c"
}
```

**Response:**
```json
{
  "game_id": "unique_game_id",
  "game_type": "a",
  "message": "Game started!"
}
```

### POST `/api/make_move`
Make a move in the current game.

**Request Body:**
```json
{
  "game_id": "unique_game_id",
  "move": "k",      // "k", "p", or "s"
  "move2": "p"      // Only for mode "a" (player vs player)
}
```

**Response:**
```json
{
  "player_move": "k",
  "computer_move": "p",
  "scores": {
    "player1": 0,
    "player2": 1,
    "ties": 0
  },
  "game_over": false
}
```

### GET `/api/game_state/<game_id>`
Get current game state.

**Response:**
```json
{
  "game_type": "b",
  "game_over": false,
  "scores": {
    "player1": 2,
    "player2": 1,
    "ties": 1
  }
}
```

## Development

### Adding New Game Modes

1. Create a new class inheriting from `KiviPaperiSakset`
2. Implement required methods: `tokan_siirto()`, `siirron_asettaminen()`
3. Register in `KiviPaperiSaksetTehdas`

### Adding New AI Strategies

1. Create a new class with `anna_siirto()` method
2. Optionally implement `aseta_siirto()` for learning
3. Use in a new game mode class

## License

MIT

## Authors

- Matti Luukkainen
