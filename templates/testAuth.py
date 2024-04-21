from TrueGame import Statistic
import tkinter
import unittest
from unittest.mock import patch
from TrueGame import Menu


class TestRegistration(unittest.TestCase):

    def test_registration_empty_fields(self):
        result = Statistic.registration("", "")
        self.assertEqual(result, "Пусто")

    def test_registration_non_numeric_password(self):
        result = Statistic.registration("test_user", "password")
        self.assertEqual(result, "Цифр")

    def test_registration_user_exist(self):
        result = Statistic.registration("test_user1", "12345")
        self.assertEqual(result, "Никнейм занят")

    @patch('TrueGame.json.loads')
    @patch('builtins.open')
    @patch('TrueGame.json.dumps')
    def test_registration_successful(self, mock_json_dumps, mock_open, mock_json_loads):
        mock_json_loads.return_value = []
        result = Statistic.registration("new_user", "123456")
        self.assertEqual(result, "1")

    def test_try_auto_invalid_credentials(self):
        result = Statistic.login("non_existing_user", "invalid_password")
        self.assertEqual(result, "0")

class TestAuth(unittest.TestCase):

    @patch('TrueGame.Statistic.registration', return_value="1")
    def test_successful_registration(self, mock_registration):
        parent = tkinter.Tk()
        menu = Menu(parent)
        menu.nickname_pole = tkinter.Entry(parent)
        menu.nickname_pole.insert(0, "test_user")
        menu.password_pole = tkinter.Entry(parent)
        menu.password_pole.insert(0, "123456")
        menu.successful_label = tkinter.Label(parent)
        menu.try_reg()
        self.assertEqual(menu.successful_label.cget("text"), "Регистрация успешна!")

    @patch('TrueGame.Statistic.login', return_value="some_id")
    def test_successful_authorization(self, mock_login):
        parent = tkinter.Tk()
        menu = Menu(parent)
        menu.nickname_pole = tkinter.Entry(parent)
        menu.nickname_pole.insert(0, "test_user")
        menu.password_pole = tkinter.Entry(parent)
        menu.password_pole.insert(0, "123456")
        menu.auth_errors = tkinter.Label(parent)
        menu.try_auto()
        self.assertEqual(menu.auth_errors.cget("text"), "Вход выполнен")

    @patch('TrueGame.Statistic.login', return_value="0")
    def test_authorization_error(self, mock_login):
        parent = tkinter.Tk()
        menu = Menu(parent)
        menu.nickname_pole = tkinter.Entry(parent)
        menu.nickname_pole.insert(0, "non_existent_user")
        menu.password_pole = tkinter.Entry(parent)
        menu.password_pole.insert(0, "wrong_password")
        menu.auth_errors = tkinter.Label(parent)
        menu.try_auto()
        self.assertEqual(menu.auth_errors.cget("text"), "Неверные данные")


if __name__ == '__main__':
    unittest.main()
