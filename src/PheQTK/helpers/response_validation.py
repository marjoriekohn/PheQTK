"""
This file contains functions for validating user responses.
"""


# recursively asks for a valid response from the user
def validate_yes_no_response(user_input: str) -> bool:
    """Return True for yes, False for no; keep asking until valid."""
    while True:
        cleaned = (user_input or "").strip().lower()
        if cleaned in {"y", "yes"}:
            return True
        if cleaned in {"n", "no"}:
            return False
        user_input = input("Please enter 'y' or 'n': ")


# recursively asks for a valid number from the user
def validate_digit_response(user_input) -> int:
    """Return an integer; keep asking until valid."""
    try:
        return int(user_input)
    except ValueError:
        print(f"{user_input} is not a valid number.")
        new_response = input("Please enter a number.")
        return validate_digit_response(new_response)
