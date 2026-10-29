"""Unit tests for TestProject's application logic."""

import pytest

import RPS_Game
from main import main


@pytest.mark.parametrize(
    ("user_choice", "computer_choice", "expected"),
    [
        ("rock", "rock", "It's a tie!"),
        ("rock", "scissors", "You win!"),
        ("paper", "rock", "You win!"),
        ("scissors", "paper", "You win!"),
        ("scissors", "rock", "Computer wins!"),
        ("rock", "paper", "Computer wins!"),
    ],
)
def test_determine_winner(user_choice, computer_choice, expected):
    assert RPS_Game.determine_winner(user_choice, computer_choice) == expected


def test_determine_winner_rejects_invalid_choice():
    with pytest.raises(ValueError):
        RPS_Game.determine_winner("lizard", "rock")


def test_get_user_choice_trims_spaces_and_ignores_case(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _prompt: "  ROCK  ")
    assert RPS_Game.get_user_choice() == "rock"


def test_get_user_choice_retries_invalid_input(monkeypatch, capsys):
    answers = iter(["water", "paper"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))

    assert RPS_Game.get_user_choice() == "paper"
    assert "Invalid input" in capsys.readouterr().out


def test_main_prints_environment_message(capsys):
    main()
    assert "Python environment is working." in capsys.readouterr().out
