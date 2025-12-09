# UI Update: Player vs Player Mode

## Changes Made

Updated the web interface for the Player vs Player mode to use image buttons instead of text input for Player 2's moves.

## What Changed

### Before
- Player 1 selected moves using three image buttons (Rock, Paper, Scissors)
- Player 2 entered their move using a text input field (typing 'k', 'p', or 's')
- This was inconsistent and less user-friendly

### After
- Both Player 1 and Player 2 now use image buttons to select their moves
- The workflow is:
  1. Player 1 clicks their move button (Rock/Paper/Scissors)
  2. Player 1's button becomes highlighted to show selection
  3. Player 2's buttons appear below
  4. Player 2 clicks their move button
  5. Player 2's button becomes highlighted
  6. Both moves are submitted automatically
  7. Results are displayed
  8. The interface resets for the next round

## Technical Changes

### HTML (`src/templates/index.html`)
1. **Replaced text input with buttons**:
   - Removed: `<input type="text" id="player2-move">`
   - Added: Separate button groups for Player 1 and Player 2
   - Each group has three identical buttons (Rock, Paper, Scissors)

2. **Updated JavaScript logic**:
   - Added `player1Move` and `player2Move` variables to track selections
   - Split move handling into two functions:
     - `makeMove()`: For AI modes (immediate submission)
     - `makePvPMove()`: For Player vs Player (waits for both selections)
   - Added `highlightSelectedMove()`: Visual feedback for selections
   - Added `showPlayer2Buttons()` / `hidePlayer2Buttons()`: UI flow control
   - Added `resetMoveSelection()`: Clears selections after each round
   - Added `displayMoveResults()`: Centralized result display logic

### CSS (`src/static/style.css`)
1. **Added player section styling**:
   - `.player-label`: Headings for "Player 1" and "Player 2" sections
   - `#player2-moves`: Spacing and border for Player 2 section

2. **Added selection state styling**:
   - `.move-button.selected`: Highlighted state for chosen moves
   - Uses gradient background and shadow to show selection
   - White text for better contrast

## User Experience Improvements

1. **Consistency**: Both players use the same interface
2. **Visual Feedback**: Selected buttons are highlighted
3. **Clear Flow**: Player 2 buttons only appear after Player 1 selects
4. **No Typing**: Eliminates potential typing errors
5. **Mobile Friendly**: Buttons work better on touch devices than text input
6. **Intuitive**: Click-to-select is more natural than remembering letter codes

## How to Use

### Player vs Player Mode
1. Select "Pelaaja vs Pelaaja" from the main menu
2. Player 1 clicks their move (🪨 Kivi, 📄 Paperi, or ✂️ Sakset)
3. Player 1's button becomes highlighted
4. Player 2's move buttons appear
5. Player 2 clicks their move
6. Player 2's button becomes highlighted
7. Results are displayed automatically
8. Interface resets for the next round

### AI Modes (Unchanged)
- In AI modes (b and c), only Player 1's buttons are shown
- Click a move, and the AI responds immediately
- No change to existing behavior

## Running the Application

```bash
cd /home/saara/projects/ohtu/palautusrepositorio/viikko7/kivi-paperi-sakset
poetry run flask --app src/web_app run
```

Then visit: http://127.0.0.1:5000/ (or http://127.0.0.1:5001/ if port 5000 is busy)

## Files Modified

1. `src/templates/index.html` - Complete UI restructure
2. `src/static/style.css` - Added new styles for player sections and selection state

## Backwards Compatibility

- All AI modes (b and c) work exactly as before
- No changes to the backend API
- No changes to game logic
- Only the Player vs Player UI workflow changed
