import unittest
from main import regular

class TestRegular(unittest.TestCase):

    def test_regular_function(self):
        """ Тестирует функцию `regular` из модуля `main` на корректность извлечения данных из CSV файлов."""

        test_data = [
            ("FILE.csv", 3, "+7(903)123-45-67", "+7(925)000-00-00доб.123", "+7(916)123-45-67", "ivan.ivanov2@example.com"),

        ]

        for filename, expected_len, expected_phone1, expected_phone2, expected_phone3, expected_email in test_data:
            with self.subTest(filename=filename):
                result = regular(filename)
                self.assertEqual(len(result), expected_len)
                self.assertEqual(result[0][5], expected_phone1)
                self.assertEqual(result[1][5], expected_phone2)
                self.assertEqual(result[2][5], expected_phone3)
                ivan_contacts = [contact for contact in result if contact[0] == "Ivanov" and contact[1] == "Ivan"]
                self.assertEqual(len(ivan_contacts), 1)
                self.assertEqual(ivan_contacts[0][6], expected_email)


if __name__ == '__main__':
    unittest.main()