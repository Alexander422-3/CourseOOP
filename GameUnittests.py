import unittest
from unittest.mock import patch, Mock
from TrueGame import Game
from TrueGame import Menu
import tkinter as tk


class TestGame(unittest.TestCase):
    def setUp(self):
        game_window = tk.Tk()
        self.Menu = Menu
        self.game = Game(game_window, self.Menu)

    def test_get_answer_empty_input(self):
        self.game.user_squares = [-1, -1, -1, -1, -1, -1, -1]
        self.assertEqual(self.game.get_answer(), 1)

    def test_check_answer_level_success(self):
        self.game.numbers_sequence = [1, 2, 3, 4, 5, 6, 7]
        self.game.user_answers = [1, 2, 3, 4, 5, 6, 7]
        self.game.get_answer = Mock(return_value=None)
        self.assertEqual(self.game.check_answer(), "Уровень пройден успешно!")

    def test_check_answer_level_fail(self):
        self.game.numbers_sequence = [1, 2, 3, 4, 5, 6, 7]
        self.game.user_answers = [1, 2, 3, 4, 5, 6, 8]
        self.game.get_answer = Mock(return_value=None)
        self.assertEqual(self.game.check_answer(), "К сожалению, вы проиграли!")

    def test_check_answer_level_4_success(self):
        self.game.level = 4
        self.game.numbers_sequence = [1, 2, 3, 4, 5, 6, 7]
        self.game.user_answers = [1, 2, 3, 4, 5, 6, 7]
        self.game.get_answer = Mock(return_value=None)
        self.assertEqual(self.game.check_answer(), "Вы успешно прошли игру!")

if __name__ == '__main__':
    unittest.main()