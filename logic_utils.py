def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


# FIX: refactored parse_guess into logic_utils.py using claude code
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (ValueError, OverflowError):
        return False, None, "That is not a number."

    return True, value, None

# FIX: refactored check_guess into logic_utils.py using copilot
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    """  # outcome examples: "Win", "Too High", "Too Low"
    # try to coerce both values to integers for numeric comparison
    try:
        guess_val = int(guess)
        secret_val = int(secret)
    except Exception:
        # fall back to original values (strings or other types)
        guess_val = guess
        secret_val = secret

    # check for equality first
    if guess_val == secret_val:
        return "Win", "🎉 Correct!"

    # if both values are numeric we can do a numeric comparison
    if isinstance(guess_val, (int, float)) and isinstance(secret_val, (int, float)):
        if guess_val > secret_val:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"

    # final fallback: compare as strings
    guess_str = str(guess)
    secret_str = str(secret)
    if guess_str == secret_str:
        return "Win", "🎉 Correct!"
    if guess_str > secret_str:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

# FIX: Had Claude refactor into logic_utils.py and update logic so that a first-try guess results in a score of 100
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
