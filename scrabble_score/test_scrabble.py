""" Test case for Scrabble Game"""
import unittest
from unittest.mock import patch
from scrabble import calculate_score, game_round


class TestScrabble(unittest.TestCase):
    """
    Test case class for testing Scrabble-related functions.
    """

    def test_calculate_score(self):
        """
        Test cases for the calculate_score function with various inputs.
        """
        self.assertEqual(calculate_score("cabbage"), 14)
        self.assertEqual(calculate_score("hello"), 8)
        self.assertEqual(calculate_score("zoo"), 12)

    def test_case_insensitivity(self):
        """
        Test cases for the calculate_score
        function to ensure case insensitivity.
        """
        self.assertEqual(calculate_score("HELLO"), 8)
        self.assertEqual(calculate_score("hello"), 8)

    def test_input_validation(self):
        """
        Test cases for input validation in the calculate_score function.
        """
        self.assertEqual(calculate_score("hello1"),
                         "Invalid input: Non-alphabet characters present.")
        self.assertEqual(calculate_score("hello!"),
                         "Invalid input: Non-alphabet characters present.")
        self.assertEqual(calculate_score(""),
                         "Invalid input: Non-alphabet characters present.")

    @patch('builtins.input', side_effect=['jahan'])
    def test_game_round_valid_jahan(self, _):
        """
        Test case for a valid game round with the input 'jahan'.
        """
        score, message = game_round(15, 5)
        self.assertEqual(score, 15)
        self.assertEqual(message, "Valid word.")

    @patch('builtins.input', side_effect=['software'])
    def test_game_round_valid_software(self, _):
        """
        Test case for a valid game round with the input 'software'.
        """
        score, message = game_round(15, 8)
        self.assertEqual(score, 14)
        self.assertEqual(message, "Valid word.")

    @patch('builtins.input', side_effect=['tools'])
    def test_game_round_valid_tools(self, _):
        """
        Test case for a valid game round with the input 'tools'.
        """
        score, message = game_round(15, 5)
        self.assertEqual(score, 5)
        self.assertEqual(message, "Valid word.")

    @patch('builtins.input', side_effect=['quit'])
    def test_quit_game(self, _):
        """
        Test case for quitting the game
        immediately and showing the total score.
        """
        score, message = game_round(15, 5)
        self.assertEqual(score, -1)
        self.assertEqual(message, "Game ended. Exiting...")

    @patch('builtins.input', side_effect=['Musrat'])
    def test_invalid_word_length(self, _):
        """
        Test case for an invalid word length where the input length is not 5.
        """
        score, message = game_round(15, 5)
        self.assertEqual(score, 0)
        self.assertEqual(
            message, "Invalid length! The word should be 5 letters."
            )

    @patch('builtins.input', side_effect=['pytho'])
    def test_invalid_word(self, _):
        """
        Test case for an invalid word that is not recognized.
        """
        score, message = game_round(15, 5)
        self.assertEqual(score, 0)
        self.assertEqual(message, "Invalid word. Please enter a valid word.")


if __name__ == '__main__':
    unittest.main()
