import unittest
from unittest.mock import patch, mock_open
from main import (
    read_integer_between_numbers,
    read_nonempty_string,
    read_integer,
    winner_of_race,
    display_races
)

class TestMainFunctions(unittest.TestCase):

    def test_read_integer_between_numbers_valid(self):
        with patch('builtins.input', side_effect=['5']):
            self.assertEqual(read_integer_between_numbers("Enter a number: ", 1, 10), 5)

    def test_read_integer_between_numbers_out_of_range(self):
        with patch('builtins.input', side_effect=['15', '5']):
            self.assertEqual(read_integer_between_numbers("Enter a number: ", 1, 10), 5)

    def test_read_nonempty_string_valid(self):
        with patch('builtins.input', side_effect=['Runner']):
            self.assertEqual(read_nonempty_string("Enter your name: "), "Runner")

    def test_read_integer_valid(self):
        with patch('builtins.input', side_effect=['7']):
            self.assertEqual(read_integer("Enter a number: "), 7)

    def test_read_integer_negative(self):
        with patch('builtins.input', side_effect=['-3', '7']):
            self.assertEqual(read_integer("Enter a number: "), 7)

    def test_winner_of_race(self):
        ids = ['R1', 'R2', 'R3']
        times = [320, 300, 310]
        self.assertEqual(winner_of_race(ids, times), ['R2', 'R3', 'R1'])

    def test_display_races(self):
        ids = ['R1', 'R2', 'R3']
        times = [125, 240, 360]
        venue = "Test Venue"
        podium = ['R1', 'R2', 'R3']
        with patch('builtins.print') as mock_print:
            display_races(ids, times, venue, podium)
            mock_print.assert_called()


if __name__ == '__main__':
    unittest.main()
