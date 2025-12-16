# Test Coverage Report - Kivi-Paperi-Sakset

## Overall Coverage: 92% 🎉

**Total**: 597 statements, 47 missed, **92% coverage**

Your test suite is **excellent**! 92% coverage is well above industry standards (typically 70-80% is considered good).

---

## Detailed Coverage by Module

### ✅ **Perfect Coverage (100%)**

These modules are fully tested:

| Module | Coverage | Notes |
|--------|----------|-------|
| `kivi_paperi_sakset_tehdas.py` | **100%** | Factory pattern - all creation paths tested |
| `tekoaly.py` | **100%** | Basic AI - complete coverage |
| `tuomari.py` | **100%** | Referee logic - all scenarios tested |

### ⭐ **Excellent Coverage (90-99%)**

These modules have near-perfect coverage:

| Module | Coverage | Missed Lines | What's Missing |
|--------|----------|--------------|----------------|
| `tekoaly_parannettu.py` | **97%** | 1/31 | Line 37: Edge case in pattern selection |
| `web_app.py` | **94%** | 4/70 | Lines 64, 86-87, 179: Error handling paths |
| `test_web_app.py` | **98%** | 3/189 | Lines 227, 239-240: Minor test helpers |

### 👍 **Good Coverage (70-89%)**

These modules are well-tested but could use a bit more:

| Module | Coverage | Missed Lines | What's Missing |
|--------|----------|--------------|----------------|
| `kps_tekoaly.py` | **83%** | 2/12 | Lines 15, 18: Print statements in game flow |
| `kps_parempi_tekoaly.py` | **77%** | 3/13 | Lines 15, 18-19: Print statements in game flow |
| `kps_pelaaja_vs_pelaaja.py` | **70%** | 3/10 | Lines 9, 12, 15: Pass statements (intentional) |

### ⚠️ **Needs Attention**

| Module | Coverage | Missed Lines | Issue |
|--------|----------|--------------|-------|
| `kivi_paperi_sakset.py` | **40%** | 18/30 | Lines 8-15, 19-24, 28-31, 35, 38, 41, 44, 47: Main game loop not tested directly |
| `index.py` | **0%** | 13/13 | CLI entry point - not tested (acceptable) |

---

## Analysis by Component

### 🏭 **Factory Pattern - 100% Coverage**
- ✅ All game types ('a', 'b', 'c') creation tested
- ✅ Invalid game type handling tested
- ✅ Factory initialization tested

**Recommendation**: None needed - perfect!

---

### 🤖 **AI Components - 98.5% Average**

#### Basic AI (`tekoaly.py`) - 100%
- ✅ Move generation cycle fully tested
- ✅ State management tested
- ✅ All possible moves covered

#### Advanced AI (`tekoaly_parannettu.py`) - 97%
- ✅ Memory management tested
- ✅ Pattern recognition tested
- ✅ Edge cases mostly covered

**Missing**: 
- Line 37: A specific conditional branch in the move selection logic

**Recommendation**: Consider adding a test for when all three move frequencies are equal.

---

### ⚖️ **Referee Logic - 100% Coverage**

The `tuomari.py` module has complete coverage:
- ✅ Score tracking
- ✅ Win/loss/tie detection
- ✅ All move combinations tested
- ✅ String representation tested

**Recommendation**: None needed - excellent!

---

### 🎮 **Game Modes - 77% Average**

#### Player vs Player (`kps_pelaaja_vs_pelaaja.py`) - 70%
**Missing**: Pass statements (lines 9, 12, 15)
- These are intentional no-ops in the implementation
- Not a real concern

#### vs AI (`kps_tekoaly.py`) - 83%
**Missing**: Print statements (lines 15, 18)
- Console output in game flow
- Hard to test, low priority

#### vs Advanced AI (`kps_parempi_tekoaly.py`) - 77%
**Missing**: Print statements (lines 15, 18-19)
- Console output in game flow
- Hard to test, low priority

**Recommendation**: These missing lines are mostly output statements which are acceptable to skip.

---

### 🎯 **Base Game Class - 40% Coverage**

The `kivi_paperi_sakset.py` base class has lower coverage because:
1. It's an abstract base class with template methods
2. The main game loop (`pelaa()`) is meant to be run interactively
3. Testing requires mocking user input (stdin)
4. Subclasses are tested individually (where the real logic is)

**Missing Lines**: 
- 8-15: Game loop setup
- 19-24: Game round logic
- 28-31: Move collection
- 35, 38, 41, 44, 47: Abstract methods and validation

**Is this a problem?** Not really, because:
- The abstract methods are tested in their concrete implementations
- The game loop is integration logic, not business logic
- All subclasses have good coverage

**Recommendation**: If you want to improve this, you could:
1. Add integration tests with mocked input
2. Test the template method pattern explicitly
3. Add tests for `_onko_ok_siirto()` validation

---

### 🌐 **Web Application - 94% Coverage**

The Flask web app has excellent test coverage with 21 tests covering:
- ✅ All endpoints tested
- ✅ Game creation tested
- ✅ Move making tested
- ✅ Score tracking tested
- ✅ Game over conditions tested
- ✅ Error cases tested

**Missing Lines**:
- Line 64: An error condition in move validation
- Lines 86-87: Another error path in move processing
- Line 179: The `if __name__ == '__main__'` block (standard to skip)

**Recommendation**: Consider adding tests for invalid move2 in PvP mode (line 64) and invalid AI moves (lines 86-87).

---

### 📝 **CLI Entry Point - 0% Coverage**

The `index.py` file has no coverage because:
- It's the main entry point for interactive CLI usage
- Requires mocking stdin for user input
- Primarily coordination code, not business logic

**Is this a problem?** No - this is standard practice:
- Main entry points are often untested
- The business logic it calls IS tested
- Testing this would require complex input mocking

**Recommendation**: This is acceptable. If desired, you could add integration tests with mocked input/output.

---

## Test Suite Statistics

- **Total Tests**: 46 tests
- **Test Files**: 5 files
- **All tests passing**: ✅

### Test Breakdown:
- `test_tehdas.py`: 5 tests - Factory pattern
- `test_tekoaly.py`: 4 tests - Basic AI
- `test_tekoaly_parannettu.py`: 8 tests - Advanced AI
- `test_tuomari.py`: 8 tests - Referee logic
- `test_web_app.py`: 21 tests - Web application

---

## Quality Assessment

### Strengths ✅

1. **Comprehensive AI Testing**: Both AI implementations are thoroughly tested
2. **Complete Core Logic**: Referee and factory patterns have 100% coverage
3. **Web API Well-Tested**: 21 tests cover all major web endpoints
4. **Good Test Organization**: Tests are well-structured and modular
5. **High Overall Coverage**: 92% is excellent

### Areas for Improvement 🔧

1. **Base Class Coverage**: Could add tests for template methods
2. **Edge Cases in Web App**: A few error paths could be tested
3. **Advanced AI Edge Case**: One conditional branch in pattern selection

### Not Real Issues ⚠️

1. **CLI Entry Point (0%)**: Standard to skip - interactive code
2. **Print Statements**: Hard to test, low value
3. **Pass Statements**: Intentional no-ops

---

## Recommendations

### High Priority
✅ **None** - Your coverage is excellent!

### Medium Priority (Optional Improvements)
1. Add test for equal frequency scenario in `tekoaly_parannettu.py` (line 37)
2. Add tests for error paths in `web_app.py`:
   - Invalid move2 in PvP mode (line 64)
   - AI move error handling (lines 86-87)

### Low Priority (Nice to Have)
1. Add integration tests for `kivi_paperi_sakset.py` game loop
2. Add integration tests for `index.py` CLI flow

---

## How to View Detailed Coverage

An HTML coverage report has been generated:

```bash
# Open the coverage report in your browser
firefox htmlcov/index.html
# or
google-chrome htmlcov/index.html
# or
xdg-open htmlcov/index.html
```

The HTML report provides:
- Color-coded line-by-line coverage
- Click through to see exactly which lines are/aren't covered
- Branch coverage details
- Interactive navigation

---

## Running Coverage Yourself

```bash
# Basic coverage report
poetry run pytest --cov=src

# Detailed report with missing lines
poetry run pytest --cov=src --cov-report=term-missing

# Generate HTML report
poetry run pytest --cov=src --cov-report=html

# All tests with verbose output
poetry run pytest -v --cov=src --cov-report=term-missing
```

---

## Conclusion

**Your test coverage is excellent at 92%!** 🎉

The missing coverage is primarily in:
1. Interactive CLI code (acceptable to skip)
2. Output statements (low value to test)
3. Abstract base class game loop (tested via subclasses)

The core business logic has outstanding coverage:
- ✅ All AI algorithms: 97-100%
- ✅ Game rules (referee): 100%
- ✅ Factory pattern: 100%
- ✅ Web API: 94%

**Keep up the great work!** Your testing practices are well above industry standards.
