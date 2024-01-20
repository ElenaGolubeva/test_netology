from unittest import TestCase
from YApi import create_a_folder

TOKEN_YANDEX_DISK = ""


class TestTask1(TestCase):
    def test_ok(self):
        name = "folder1"
        expected = 201
        result = create_a_folder(TOKEN_YANDEX_DISK, name)
        self.assertEqual(result, expected)

    def test_one_name_folder(self):
        name = "hello"
        expected = 409
        result = create_a_folder(TOKEN_YANDEX_DISK, name)
        self.assertEqual(result, expected)

    def test_not_authorized(self):
        token_yandex_disk_failled = TOKEN_YANDEX_DISK[1:] #Неверный токен
        name = "hello"
        expected = 401
        result = create_a_folder(token_yandex_disk_failled, name)
        self.assertEqual(result, expected)
