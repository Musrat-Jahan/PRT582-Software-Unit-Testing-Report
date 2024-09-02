"""
Scrabble score game.
"""
import time

LETTER_VALUES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1,
    'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}


def calculate_score(word):
    """Calculate the Scrabble score for a given word."""
    if not word.isalpha():
        return "Invalid input: Non-alphabet characters present."
    word = word.upper()  # Convert word to uppercase to match dictionary keys
    score = sum(LETTER_VALUES.get(letter, 0) for letter in word)
    return score


def is_valid_word(word):
    """Check if the word is valid (placeholder for dictionary check)."""
    valid_words = {"hello", "world", "python",
                   "scrabble", "shuvo"}  # Example dictionary
    return word.lower() in valid_words


def game_round(timer_seconds, required_length):
    """Simulate a game round with a timer and word length requirement."""
    start_time = time.time()
    word = input(f"Enter a word with {required_length} letters: ")
    elapsed_time = time.time() - start_time

    if elapsed_time > timer_seconds:
        return (0, "Time's up! You took too long.")
    if not word.isalpha():
        return (0, "Invalid input: Non-alphabet characters present.")
    if len(word) != required_length:
        return (
            0,
            f"Invalid length! The word should be {required_length} letters."
        )
    if not is_valid_word(word):
        return (0, "Invalid word. Please enter a valid word.")

    score = calculate_score(word)
    return (score, "Valid word.")


def main():
    """Main game loop."""
    total_score = 0
    rounds = 10  # Play 10 rounds
    timer_seconds = 15

    for i in range(rounds):
        print(f"Round {i+1} of {rounds}")
        required_length = 5  # This can be randomized or set as needed
        score, message = game_round(timer_seconds, required_length)
        print(message)
        total_score += score

    print(f"Game over! Your total score is: {total_score}")


if __name__ == "__main__":
    main()
