#FIX: Refactored logic into logic_utils.py using agent mode
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    Args:
        difficulty (str): Difficulty level. Accepted values are "Easy",
            "Normal", and "Hard". Any unrecognised value falls back to
            the Normal range.

    Returns:
        tuple[int, int]: A ``(low, high)`` pair representing the inclusive
            lower and upper bounds of the secret number range.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

#FIX: Refactored logic into logic_utils.py using agent mode
def parse_guess(raw: str):
    """Parse user input into an integer guess.

    Accepts plain integers and decimal strings (e.g. ``"7.9"``); decimals
    are truncated toward zero via ``int(float(raw))``.

    Args:
        raw (str): Raw string entered by the user. May be ``None`` or empty.

    Returns:
        tuple: A three-element tuple ``(ok, guess_int, error_message)`` where:

        - **ok** (*bool*): ``True`` if parsing succeeded, ``False`` otherwise.
        - **guess_int** (*int | None*): Parsed integer value, or ``None`` on
          failure.
        - **error_message** (*str | None*): Human-readable error description,
          or ``None`` on success.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIX: Refactored logic into logic_utils.py using agent mode
def check_guess(guess, secret):
    """Compare a player's guess to the secret number and return a result.

    Args:
        guess (int): The integer value guessed by the player.
        secret (int): The secret number to compare against.

    Returns:
        tuple[str, str]: A ``(outcome, message)`` pair where outcome is one
            of ``"Win"``, ``"Too High"``, or ``"Too Low"``, and message is a
            corresponding display string.

    Raises:
        TypeError: If ``guess`` and ``secret`` are of incompatible types that
            cannot be compared with ``>``.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    #FIX: Fixed hint being backwards and removed unncessary
    #  type conversion handling for simulated glitchy behavior.
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        raise

#FIX: Refactored logic into logic_utils.py using agent mode
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    Scoring rules:

    - **Win**: awards ``100 - 10 * (attempt_number + 1)`` points, with a
      minimum of 10.
    - **Too High**: adds 5 points on even attempts, subtracts 5 on odd.
    - **Too Low**: subtracts 5 points.
    - Any other outcome leaves the score unchanged.

    Args:
        current_score (int): The player's score before this attempt.
        outcome (str): Result of the guess. Expected values are ``"Win"``,
            ``"Too High"``, or ``"Too Low"``.
        attempt_number (int): The 0-based attempt count for the current guess.

    Returns:
        int: The updated score after applying the outcome.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
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
