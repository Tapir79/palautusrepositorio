# Architecture Documentation

## Overview

The Kivi-Paperi-Sakset application is built using several design patterns to ensure maintainability, extensibility, and clean separation of concerns.

## Design Patterns

### 1. Factory Pattern

**Purpose**: Create game instances without exposing creation logic to the client.

**Implementation**: `KiviPaperiSaksetTehdas` class

```python
class KiviPaperiSaksetTehdas():
    """Pelitehdasluokka, joka osaa luoda eri pelejä."""

    def __init__(self):
        self._pelit = {
            'a': KPSPelaajaVsPelaaja,
            'b': KPSTekoaly,
            'c': KPSParempiTekoaly
        }

    def luo_peli(self, tyyppi):
        if tyyppi in self._pelit:
            return self._pelit[tyyppi]() 
        return None
```

**Benefits**:
- Easy to add new game modes
- Client code doesn't need to know concrete classes
- Centralized game creation logic

### 2. Template Method Pattern

**Purpose**: Define the skeleton of an algorithm, letting subclasses override specific steps.

**Implementation**: `KiviPaperiSakset` base class

```python
class KiviPaperiSakset:
    def pelaa(self):
        """Template method - defines game flow"""
        ekan_siirto, tokan_siirto = self.tee_siirrot()
        self.toisen_pelaajan_eka_valinta(tokan_siirto)
        
        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.pelikierros()
        
        print("Kiitos!")
        print(self._tuomari)
    
    # Abstract methods to be overridden
    def tokan_siirto(self):
        raise IndexError("Tämä metodi pitää korvata aliluokassa")
    
    def siirron_asettaminen(self, tokan_siirto, ekan_siirto):
        raise IndexError("Tämä metodi pitää korvata aliluokassa")
```

**Benefits**:
- Game flow is consistent across all modes
- Subclasses only implement what's different
- Reduces code duplication

### 3. Strategy Pattern

**Purpose**: Define a family of algorithms, encapsulate each one, and make them interchangeable.

**Implementation**: AI strategy classes (`Tekoaly`, `TekoalyParannettu`)

```python
# Basic strategy
class Tekoaly:
    def anna_siirto(self):
        # Simple cycling algorithm
        ...

# Advanced strategy
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = [None] * muistin_koko
    
    def anna_siirto(self):
        # Pattern recognition algorithm
        ...
    
    def aseta_siirto(self, siirto):
        # Learn from player's moves
        ...
```

**Benefits**:
- AI algorithms can be swapped easily
- New AI strategies can be added without modifying game logic
- AI behavior is encapsulated and testable

### 4. Dependency Injection

**Purpose**: Provide dependencies from outside rather than creating them internally.

**Implementation**: Constructor injection for `Tuomari` and AI strategies

```python
class KiviPaperiSakset:
    def __init__(self, tuomari=Tuomari()):
        self._tuomari = tuomari

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly=Tekoaly()):
        super().__init__()
        self._tekoaly = tekoaly
```

**Benefits**:
- Easier testing (can inject mocks)
- More flexible and configurable
- Reduces tight coupling

## System Architecture

### Layered Architecture

```
┌─────────────────────────────────────────────┐
│         Presentation Layer                   │
│  ┌──────────────┐    ┌──────────────┐       │
│  │   CLI (CLI)  │    │ Flask Web UI │       │
│  │  index.py    │    │  web_app.py  │       │
│  └──────────────┘    └──────────────┘       │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│         Business Logic Layer                 │
│  ┌──────────────────────────────────────┐   │
│  │   Factory (KiviPaperiSaksetTehdas)  │   │
│  └──────────────────────────────────────┘   │
│                    │                         │
│                    ▼                         │
│  ┌──────────────────────────────────────┐   │
│  │      Game Implementations            │   │
│  │  - KPSPelaajaVsPelaaja               │   │
│  │  - KPSTekoaly                        │   │
│  │  - KPSParempiTekoaly                 │   │
│  └──────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│         Domain Layer                         │
│  ┌──────────┐    ┌──────────────────────┐   │
│  │ Tuomari  │    │   AI Strategies      │   │
│  │ (Scores) │    │  - Tekoaly           │   │
│  └──────────┘    │  - TekoalyParannettu │   │
│                  └──────────────────────┘   │
└─────────────────────────────────────────────┘
```

### Component Interactions

```
User Input
    │
    ▼
┌──────────────┐
│ index.py or  │
│ web_app.py   │
└──────────────┘
    │
    ▼
┌──────────────────────┐
│ KiviPaperiSakset     │──────┐
│ Tehdas               │      │
└──────────────────────┘      │
    │                         │
    ▼ creates                 │
┌──────────────────────┐      │
│ KPS* (Game Mode)     │      │
└──────────────────────┘      │
    │                         │
    ├─────────────────────────┤
    │ uses                uses│
    ▼                         ▼
┌──────────┐          ┌──────────────┐
│ Tuomari  │          │  Tekoaly*    │
│          │          │  (Strategy)  │
└──────────┘          └──────────────┘
```

## Class Relationships

### Inheritance Hierarchy

```
KiviPaperiSakset (Abstract Base)
    │
    ├── KPSPelaajaVsPelaaja
    ├── KPSTekoaly
    └── KPSParempiTekoaly
```

### Composition Relationships

- **KiviPaperiSakset** HAS-A **Tuomari** (referee for scoring)
- **KPSTekoaly** HAS-A **Tekoaly** (basic AI strategy)
- **KPSParempiTekoaly** HAS-A **TekoalyParannettu** (advanced AI strategy)
- **TekoalyParannettu** HAS-A **list** (memory for pattern recognition)

## Data Flow

### CLI Application Flow

```
1. User launches index.py
2. Display menu (a/b/c options)
3. User selects game mode
4. Factory creates appropriate game instance
5. Game loop starts:
   a. Request player 1 move
   b. Get player 2 move (input or AI)
   c. Tuomari evaluates moves
   d. Display scores
   e. Repeat until invalid move
6. Display final scores
7. Exit
```

### Web Application Flow

```
1. User visits / (index.html)
2. User selects game mode
3. POST /api/new_game
   └─> Factory creates game and stores in session
4. Game loop:
   a. User clicks move button
   b. POST /api/make_move
   c. Game processes move
   d. AI generates response (if applicable)
   e. Tuomari evaluates
   f. Return scores to client
   g. Update UI
5. Game ends when:
   - 5 rounds won by either player
   - User clicks "End Game"
6. Display final scores
```

## State Management

### CLI Application
- **State**: Stored in local variables within `pelaa()` method
- **Persistence**: None (game state lost after exit)
- **Scope**: Single game session

### Web Application
- **State**: Stored in server-side dictionary `games`
- **Key**: Unique game_id (generated token)
- **Persistence**: In-memory (lost on server restart)
- **Scope**: Multiple concurrent games supported

### Game State Structure (Web)
```python
games[game_id] = {
    'peli': <game_instance>,
    'tuomari': <tuomari_instance>,
    'game_type': 'a'|'b'|'c',
    'game_over': bool,
    'first_move': bool
}
```

## AI Algorithms

### Basic AI (Tekoaly)

**Algorithm**: Round-robin cycling
```
State: counter = 0
On each move:
    counter = (counter + 1) % 3
    return ['k', 'p', 's'][counter]
```

**Complexity**: O(1) time, O(1) space

**Predictability**: 100% predictable

### Advanced AI (TekoalyParannettu)

**Algorithm**: Pattern recognition with frequency analysis

```
State: 
    memory = circular buffer of size N
    pointer = current position

On player move:
    Store move in memory[pointer]
    pointer = (pointer + 1) % N

On AI move:
    last_move = memory[pointer - 1]
    
    # Find what player did after last_move in history
    for each occurrence of last_move in memory:
        count frequency of next move
    
    # Counter the most frequent next move
    if player_often_plays_rock_next:
        return 'p' (paper beats rock)
    elif player_often_plays_paper_next:
        return 's' (scissors beats paper)
    else:
        return 'k' (rock beats scissors)
```

**Complexity**: O(N) time, O(N) space (where N = memory size)

**Predictability**: Depends on player's pattern consistency

## Security Considerations

### Web Application

1. **Session Management**
   - Uses cryptographically secure tokens (`secrets.token_hex`)
   - Game IDs are unpredictable

2. **Input Validation**
   - All moves validated against ['k', 'p', 's']
   - Game ID existence checked before operations

3. **State Isolation**
   - Each game has isolated state
   - No cross-game data leakage

4. **Missing Protections** (for production)
   - No rate limiting
   - No authentication
   - No CSRF protection
   - In-memory storage (not persistent)
   - No input sanitization for XSS

## Testing Strategy

### Unit Testing
- **Tuomari**: Test scoring logic
- **AI Strategies**: Test move generation
- **Game Modes**: Test move handling

### Integration Testing
- Test factory creation
- Test game flow end-to-end

### Web API Testing
- Test all endpoints
- Test error conditions
- Test game state transitions

## Extensibility Points

### Adding New Game Modes

1. Create new class inheriting `KiviPaperiSakset`
2. Override `tokan_siirto()` and `siirron_asettaminen()`
3. Register in factory's `_pelit` dictionary
4. Update web UI and CLI menu

### Adding New AI Strategies

1. Create new class with `anna_siirto()` method
2. Optionally add `aseta_siirto()` for learning
3. Inject into new or existing game mode
4. No changes to game logic required

### Adding New Scoring Rules

1. Modify `Tuomari` class
2. Update `_eka_voittaa()` logic
3. Add new score tracking fields
4. Update display methods

## Performance Considerations

- **Memory**: O(N) per game where N = AI memory size (default 10)
- **CPU**: O(N) per move for advanced AI pattern matching
- **Scalability**: Limited by in-memory storage
- **Concurrent Games**: Supported (separate state per game_id)

## Future Improvements

1. **Persistent Storage**: Use database for game state
2. **Real-time Multiplayer**: WebSocket support
3. **Authentication**: User accounts and game history
4. **Statistics**: Win/loss tracking, leaderboards
5. **Tournament Mode**: Multiple players, brackets
6. **Configurable AI**: Adjustable difficulty/memory size
7. **Mobile App**: Native iOS/Android clients
8. **Machine Learning AI**: Neural network-based strategy
