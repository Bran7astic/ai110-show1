from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

# --- parse_guess tests ---

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_whitespace_only():
    # Edge case: whitespace-only should say "Enter a guess.", not "That is not a number."
    ok, value, err = parse_guess("   ")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_integer_with_whitespace():
    # Edge case: leading/trailing whitespace around a valid number
    ok, value, err = parse_guess("  42  ")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_float_truncates():
    # "3.9" should become 3 via int(float(...))
    ok, value, err = parse_guess("3.9")
    assert ok is True
    assert value == 3
    assert err is None

def test_parse_guess_float_whole_number():
    ok, value, err = parse_guess("50.0")
    assert ok is True
    assert value == 50
    assert err is None

def test_parse_guess_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None

def test_parse_guess_letters():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_mixed_alphanum():
    ok, value, err = parse_guess("12abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_infinity():
    # Edge case: "inf" parses as float but int(float("inf")) raises OverflowError
    ok, value, err = parse_guess("inf")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


# --- get_range_for_difficulty tests ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_unknown_difficulty_defaults_to_hard_range():
    # Any unrecognized difficulty should fall back to (1, 100)
    low, high = get_range_for_difficulty("Extreme")
    assert low == 1
    assert high == 100

def test_empty_string_difficulty_defaults():
    low, high = get_range_for_difficulty("")
    assert low == 1
    assert high == 100

def test_case_sensitive_easy():
    # "easy" (lowercase) is not "Easy" — should fall back to default
    low, high = get_range_for_difficulty("easy")
    assert low == 1
    assert high == 100


# --- check_guess tests ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High" and message prompt lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low" and message prompt higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- update_score tests ---

def test_win_first_attempt_scores_100():
    # A correct guess on attempt 1 should add exactly 100 points
    assert update_score(0, "Win", 1) == 100

def test_win_second_attempt_scores_90():
    assert update_score(0, "Win", 2) == 90

def test_win_score_minimum_is_10():
    # After many attempts the bonus should floor at 10, not go negative
    assert update_score(0, "Win", 100) == 10

def test_win_adds_to_existing_score():
    assert update_score(50, "Win", 1) == 150

def test_too_high_even_attempt_adds_5():
    # On an even attempt number "Too High" is rewarded with +5
    assert update_score(20, "Too High", 2) == 25

def test_too_high_odd_attempt_subtracts_5():
    # On an odd attempt number "Too High" is penalized with -5
    assert update_score(20, "Too High", 3) == 15

def test_too_low_subtracts_5():
    assert update_score(20, "Too Low", 1) == 15

def test_unknown_outcome_unchanged():
    assert update_score(40, "Unknown", 1) == 40
