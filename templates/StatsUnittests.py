import unittest
from TrueGame import Statistic

class TestStatistic(unittest.TestCase):

    def test_registration(self):
        self.assertEqual(Statistic.registration("test_user1", "12345"), "Никнейм занят") # Пользователь успешно зарегистрирован
        self.assertEqual(Statistic.registration("test_user", "67890"), "Никнейм занят")  # Никнейм уже занят
        self.assertEqual(Statistic.registration("", "12345"), "Пусто")  # Пустой никнейм
        self.assertEqual(Statistic.registration("test_user23", "abcde"), "Цифр")  # Пароль содержит не только цифры

    def test_login(self):
        self.assertEqual(Statistic.login("test_user", "12345"), "e3f67f96-72fd-4be6-94b8-c610c4e57d2e")  # Вход выполнен успешно
        self.assertEqual(Statistic.login("non_existing_user", "12345"), "0")  # Несуществующий пользователь

    def test_update_stats(self):
        Statistic.update_stats("e3f67f96-72fd-4be6-94b8-c610c4e57d2e", 5)  # Обновление статистики пользователя

    def test_get_statics(self):
        stats = Statistic.get_statics()  # Получение статистики всех пользователей
        self.assertTrue(isinstance(stats, list))

if __name__ == '__main__':
    unittest.main()
