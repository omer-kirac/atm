import unittest
from io import StringIO
from unittest.mock import patch

from atm import Bank, Screen
from atm import Keypad

class TestBankMethods(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Example Bank", "123")

    def test_get_name(self):
        self.assertEqual(self.bank.get_name(), "Example Bank")

    def test_set_name(self):
        self.bank.set_name("New Bank Name")
        self.assertEqual(self.bank.get_name(), "New Bank Name")
        #Kalacak test göstermek istersen çalıştığına dair.
        #self.assertEqual(self.bank.get_name(), "DENEME")

    def test_get_bank_code(self):
        self.assertEqual(self.bank.get_bank_code(), "123")

    def test_set_bank_code(self):
        self.bank.set_bank_code("456")
        self.assertEqual(self.bank.get_bank_code(), "456")

class TestKeypadInput(unittest.TestCase):
    @patch('builtins.input', return_value='12345')  # Mock input'i sağlamak için
    def test_get_input_valid(self, mock_input):
        keypad = Keypad()
        user_input = keypad.get_input()
        self.assertEqual(user_input, 12345)

    @patch('builtins.input', return_value='abcde')  # Mock input'i sağlamak için
    @patch('builtins.print')  # Mock print'i sağlamak için
    def test_get_input_invalid(self, mock_print, mock_input):
        keypad = Keypad()
        user_input = keypad.get_input()
        self.assertIsNone(user_input)
        mock_print.assert_called_with("Invalid input. Please enter a valid number.")

class TestScreenMethods(unittest.TestCase):
    def test_show_message(self):
        screen = Screen()
        message = "Hello, welcome to the ATM."
        expected_output = message + "\n"


        with StringIO() as fake_output, unittest.mock.patch('sys.stdout', new=fake_output):
            screen.show_message(message)
            printed_output = fake_output.getvalue()

        self.assertEqual(printed_output, expected_output)



if __name__ == '__main__':
    unittest.main()
