"""Fully functioning, abstracted Wordle."""
__author__ = "730661589"


def contains_char(main_string: str, character_search: str) -> bool:
    """This function checks if your string has the character requested."""
    assert len(character_search) == 1
    result: bool = False
    index: int = 0
    while index != len(main_string):
        if main_string[index] == character_search:
            result = True
            return result
        else:
            index += 1
    return result


def emojified(user_guess: str, secret_word: str) -> str:
    """This function creates the emoji string that indicates to the user how correct their guess is."""
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    result: str = ""
    while index != len(secret_word):
        """This while loop emojifies the results and makes it so we get a visual representation of how close we are."""
        if contains_char(secret_word, user_guess[index]) and user_guess[index] == secret_word[index]:
            result += GREEN_BOX
        elif contains_char(secret_word, user_guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def input_guess(expected_length: int) -> str:
    """This function lets you know if the guess is the expected length."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    if len(user_guess) == expected_length:
        return user_guess
    return user_guess


def main() -> None:
    """Main method where all of the logic is used."""
    current_turn: int = 1
    secret_word: str = "codes"
    user_guess: str = ""
    result: str = ""
    correct_length: int = len(secret_word)
    while current_turn <= 6 and user_guess != secret_word:
        """This following while loop contains the main logic of the main method."""
        print(f"=== Turn {current_turn}/6 ===")
        user_guess = input_guess(correct_length)
        if user_guess == secret_word:
            result = emojified(user_guess, secret_word)
            print(result)
            print(f"You won in {current_turn}/6 turns!")
        elif current_turn == 6:
            print(emojified(user_guess, secret_word))
            print("X/6 - Sorry, try again tomorrow!")
        else:
            print(emojified(user_guess, secret_word))
        current_turn += 1


if __name__ == "__main__":
    main()
