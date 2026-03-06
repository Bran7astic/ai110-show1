import sys
import os

# parse_guess lives in app.py which has top-level Streamlit calls.
# To avoid import errors, we extract it by patching streamlit before import.
import unittest.mock as mock
sys.modules.setdefault("streamlit", mock.MagicMock())

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import parse_guess

from logic_utils import check_guess

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

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
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

def test_parse_guess_special_characters():
    ok, value, err = parse_guess("!@#")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


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
