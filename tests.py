import unittest

from unittest.mock import patch
from app import run_manually, run_from_file


class TestMethods(unittest.TestCase):
    @patch('builtins.input', side_effect=['input.txt'])
    def test_instructions_from_file(self, mock):
        self.plateau = run_from_file()
        self.assertEqual(2, len(self.plateau.rovers))

    @patch('builtins.input', side_effect=['5 5', '1 2 N', 'LMLMLMLMM', 'S'])
    def test_instructions_manually(self, mock):
        self.plateau = run_manually()
        self.assertEqual(3, len(self.plateau.rovers))


if __name__ == '__main__':
    unittest.main()
