# How to Play Kivi-Paperi-Sakset

A comprehensive guide to playing Rock-Paper-Scissors in Finnish (Kivi-Paperi-Sakset).

## Quick Start

### For the Impatient

**Command Line:**
```bash
poetry run python src/index.py
```
Type `b`, press Enter, then play `k`, `p`, or `s` each round!

**Web Browser:**
```bash
poetry run flask --app src/web_app run
```
Visit http://127.0.0.1:5000 and click buttons to play!

---

## The Basics

### What is Rock-Paper-Scissors?

Rock-Paper-Scissors is a classic hand game played between two players. Each player simultaneously chooses one of three options:

- 🪨 **Rock** (Kivi) - represented by **`k`**
- 📄 **Paper** (Paperi) - represented by **`p`**
- ✂️ **Scissors** (Sakset) - represented by **`s`**

### Who Wins?

The rules are simple:
- **Rock crushes Scissors** → Rock wins
- **Scissors cuts Paper** → Scissors wins
- **Paper covers Rock** → Paper wins
- **Same choice** → Tie (Tasapeli)

### Move Reference Table

| Your Move | Beats    | Loses To |
|-----------|----------|----------|
| k (Rock)  | s (Scissors) | p (Paper) |
| p (Paper) | k (Rock) | s (Scissors) |
| s (Scissors) | p (Paper) | k (Rock) |

---

## Command-Line Instructions

### Starting a Game

1. Open your terminal
2. Navigate to the project directory:
   ```bash
   cd /path/to/kivi-paperi-sakset
   ```
3. Run the game:
   ```bash
   poetry run python src/index.py
   ```

### Selecting a Game Mode

You'll see this menu:
```
Valitse pelataanko
 (a) Ihmistä vastaan
 (b) Tekoälyä vastaan
 (c) Parannettua tekoälyä vastaan
Muilla valinnoilla lopetetaan
```

**Type one of the following:**
- **`a`** - Play against another person (Player vs Player)
- **`b`** - Play against basic AI (Player vs Computer - Easy)
- **`c`** - Play against advanced AI (Player vs Computer - Hard)
- **Any other key** - Exit the game

### Playing a Round

1. When prompted `Ensimmäisen pelaajan siirto:`, type your move:
   - `k` for Rock (Kivi)
   - `p` for Paper (Paperi)
   - `s` for Scissors (Sakset)
2. Press Enter
3. The computer or second player makes their move
4. The score is displayed
5. Repeat!

### Example Game Session

```
Valitse pelataanko
 (a) Ihmistä vastaan
 (b) Tekoälyä vastaan
 (c) Parannettua tekoälyä vastaan
Muilla valinnoilla lopetetaan
b

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

Ensimmäisen pelaajan siirto: p
Tietokone valitsi: k
Pelitilanne: 2 - 0
Tasapelit: 2

Ensimmäisen pelaajan siirto: quit
Kiitos!
Pelitilanne: 2 - 0
Tasapelit: 2
```

### Ending the Game

To end a CLI game, type anything other than `k`, `p`, or `s`:
- Type `quit`, `exit`, or just press Enter
- The final score will be displayed
- You'll return to the main menu

---

## Web Interface Instructions

### Starting the Web App

1. Open your terminal
2. Navigate to the project directory:
   ```bash
   cd /path/to/kivi-paperi-sakset
   ```
3. Start the Flask server:
   ```bash
   poetry run flask --app src/web_app run
   ```
4. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

### Playing in the Browser

1. **Select Game Mode**
   - Click one of the three buttons:
     - "Ihmistä vastaan" (vs Human)
     - "Tekoälyä vastaan" (vs AI - Easy)
     - "Parannettua tekoälyä vastaan" (vs AI - Hard)

2. **Make Your Move**
   - Click one of the three move buttons:
     - 🪨 Kivi (Rock)
     - 📄 Paperi (Paper)
     - ✂️ Sakset (Scissors)

3. **See the Result**
   - Your move is displayed
   - Computer's move is shown
   - Scores are updated automatically
   - Move history is shown below

4. **Continue Playing**
   - Keep clicking move buttons for more rounds
   - Game automatically ends when someone reaches 5 wins

5. **Start a New Game**
   - Click "Uusi peli" (New Game) button
   - Or click "Lopeta" (End) to end current game

### Web Interface Features

- **Visual Feedback**: See both moves displayed clearly
- **Live Scoring**: Scores update in real-time
- **Move History**: See the last several moves
- **Auto-End**: Game ends when first player reaches 5 points
- **Responsive Design**: Works on desktop and mobile

---

## Game Modes Explained

### Mode A: Ihmistä vastaan (Player vs Player)

**Best for:** Playing with a friend on the same device

**How it works:**
- Player 1 enters their move
- Player 2 enters their move
- Both moves are revealed
- Score is updated

**Tips:**
- Try not to look when the other player types!
- Take turns sitting at the keyboard
- Honor system - no peeking!

---

### Mode B: Tekoälyä vastaan (vs Basic AI)

**Best for:** Learning the game, practicing, having fun

**How it works:**
The AI uses a simple pattern:
1. First move: Rock (k)
2. Second move: Paper (p)
3. Third move: Scissors (s)
4. Repeat...

**Strategy to Win:**
- Move 1: Play Paper (p) to beat Rock
- Move 2: Play Scissors (s) to beat Paper
- Move 3: Play Rock (k) to beat Scissors
- Repeat this pattern!

**Fun fact:** This AI is intentionally easy to beat once you figure out the pattern.

---

### Mode C: Parannettua tekoälyä vastaan (vs Advanced AI)

**Best for:** A real challenge, testing your randomness

**How it works:**
- The AI remembers your last 10 moves
- It looks for patterns in your play style
- It predicts what you'll play next
- It plays the move that beats your predicted move

**Example:**
```
Your history: k, k, p, k, k, p, k...
AI notices: After playing "k" twice, you often play "p"
You just played: k, k
AI predicts: You'll play "p" next
AI plays: "s" (scissors beats paper)
```

**Strategy to Win:**
- **Be random!** Don't fall into patterns
- **Mix up your moves** unexpectedly
- **Don't repeat sequences** (like k-p-s-k-p-s)
- **Think like you're generating random numbers**

**Patterns to Avoid:**
- ❌ k-p-s-k-p-s (predictable cycle)
- ❌ k-k-k-k-k (all same)
- ❌ k-p-k-p-k-p (alternating)
- ✅ k-s-k-k-p-s-p-k-s-p (good randomness!)

---

## Score Keeping

### Understanding the Scoreboard

After each round, you'll see:
```
Pelitilanne: 2 - 1
Tasapelit: 1
```

This means:
- **Pelitilanne**: Current score (Player 1 - Player 2)
- **2**: Player 1 has won 2 rounds
- **1**: Player 2 has won 1 round
- **Tasapelit: 1**: There has been 1 tie

### Winning the Game

- **CLI Version**: Play as many rounds as you want! Game ends only when you enter an invalid move.
- **Web Version**: First player to win **5 rounds** wins the game.

---

## Troubleshooting

### CLI Issues

**Problem**: "Invalid move" or game ends unexpectedly
- **Solution**: Make sure you're typing exactly `k`, `p`, or `s` (lowercase)
- **Common mistakes**: Capital letters (K, P, S), extra spaces, typos

**Problem**: Can't start the game
- **Solution**: Make sure Poetry is installed and run `poetry install` first

**Problem**: Wrong Python version
- **Solution**: This requires Python 3.12+. Check with `python --version`

### Web Interface Issues

**Problem**: Can't connect to http://127.0.0.1:5000
- **Solution**: Make sure the Flask server is running in your terminal
- **Check**: Look for the message "Running on http://127.0.0.1:5000"

**Problem**: Buttons don't work
- **Solution**: Check browser console for errors (F12)
- **Solution**: Try refreshing the page
- **Solution**: Make sure JavaScript is enabled

**Problem**: Scores not updating
- **Solution**: Check that the game hasn't ended (5 points reached)
- **Solution**: Start a new game

---

## Tips and Strategies

### General Tips

1. **Against Basic AI**: Look for the pattern (it's there!)
2. **Against Advanced AI**: Be as random as possible
3. **Against Humans**: Try to predict their psychology
4. **Psychology**: People often throw Rock first (why? nobody knows!)
5. **After a Win**: People often stick with their winning move
6. **After a Loss**: People often switch to what would have won

### Advanced Strategies

#### The "Random" Approach
Best against Advanced AI
- Don't think too hard
- Choose quickly without planning
- Vary your moves unpredictably
- Avoid any repeating patterns

#### The "Pattern Breaking" Approach
Best against Basic AI
- Identify the AI's pattern (cycle: k→p→s→k)
- Play the counter to each predicted move
- Win consistently once you find the pattern

#### The "Psychological" Approach
Best against humans
- Watch what they play after wins/losses
- Notice if they favor a particular move
- Play the counter to their habits
- Mix in randomness so they can't read you

---

## Fun Facts

- Rock-Paper-Scissors has been played since ancient times
- In Japan, it's called "Jan-Ken-Pon"
- There are world championships for this game!
- Some people claim certain moves are "stronger" psychologically
- The game is often used to make fair decisions

---

## Keyboard Shortcuts (Web)

While the web interface uses buttons, you can also:
- Press `1` for Rock (if implemented)
- Press `2` for Paper (if implemented)
- Press `3` for Scissors (if implemented)

*(Note: Check if keyboard shortcuts are enabled in your version)*

---

## Getting Help

If you're stuck or confused:

1. **Read the prompts carefully** - they tell you what to do
2. **Check your spelling** - must be exactly `k`, `p`, or `s`
3. **Review the rules** - remember what beats what
4. **Try Mode B first** - it's the easiest to learn
5. **Practice!** - you'll get the hang of it quickly

---

## Have Fun!

Remember, it's just a game! Whether you're playing against the computer or a friend, the goal is to have fun. Don't worry too much about winning - even the advanced AI isn't unbeatable!

**Pro tip**: The best strategy is to enjoy yourself! 🎮

---

## Quick Reference Card

```
┌─────────────────────────────────────┐
│  MOVES                              │
│  k = Kivi (Rock)      🪨           │
│  p = Paperi (Paper)   📄           │
│  s = Sakset (Scissors) ✂️          │
├─────────────────────────────────────┤
│  WHAT BEATS WHAT                    │
│  Rock > Scissors                    │
│  Scissors > Paper                   │
│  Paper > Rock                       │
├─────────────────────────────────────┤
│  GAME MODES                         │
│  a = vs Human                       │
│  b = vs Easy AI (patterned)         │
│  c = vs Hard AI (learning)          │
├─────────────────────────────────────┤
│  WINNING                            │
│  CLI: Play until invalid input      │
│  Web: First to 5 points wins        │
└─────────────────────────────────────┘
```

Print this out and keep it handy! 📝
