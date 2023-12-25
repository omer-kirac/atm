import unittest
from customer import Customer
from customer import Card
from customer import Account
from customer import add_customer,customer_list
from customer import check_account_number
from customer import check_card_pin

class TestCustomerMethods(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Ahmet Yılmaz", "İstiklal Cad. No: 123", "ahmet@example.com", "0555 555 55 55", "Aktif", "1234 5678 9101 1121", "Ahmet Yılmaz", "12/25", "1234", "789101112")

    def test_get_name(self):
        self.assertEqual(self.customer.get_name(), "Ahmet Yılmaz")

    def test_set_name(self):
        self.customer.set_name("Mehmet Demir")
        self.assertEqual(self.customer.get_name(), "Mehmet Demir")

    def test_get_address(self):
        self.assertEqual(self.customer.get_address(), "İstiklal Cad. No: 123")

    def test_set_address(self):
        self.customer.set_address("Atatürk Cad. No: 456")
        self.assertEqual(self.customer.get_address(), "Atatürk Cad. No: 456")

    def test_get_email(self):
        self.assertEqual(self.customer.get_email(), "ahmet@example.com")

    def test_set_email(self):
        self.customer.set_email("mehmet@example.com")
        self.assertEqual(self.customer.get_email(), "mehmet@example.com")

    def test_get_phone(self):
        self.assertEqual(self.customer.get_phone(), "0555 555 55 55")

    def test_set_phone(self):
        self.customer.set_phone("0555 123 45 67")
        self.assertEqual(self.customer.get_phone(), "0555 123 45 67")

    def test_get_status(self):
        self.assertEqual(self.customer.get_status(), "Aktif")

    def test_set_status(self):
        self.customer.set_status("Pasif")
        self.assertEqual(self.customer.get_status(), "Pasif")


class TestCardMethods(unittest.TestCase):
    def setUp(self):
        self.card = Card("1234 5678 9101 1121", "Ahmet Yılmaz", "12/25", "1234")

    def test_get_card_number(self):
        self.assertEqual(self.card.get_card_number(), "1234 5678 9101 1121")

    def test_set_card_number(self):
        self.card.set_card_number("2222 3333 4444 5555")
        self.assertEqual(self.card.get_card_number(), "2222 3333 4444 5555")

    def test_get_customer_name(self):
        self.assertEqual(self.card.get_customer_name(), "Ahmet Yılmaz")

    def test_set_customer_name(self):
        self.card.set_customer_name("Mehmet Demir")
        self.assertEqual(self.card.get_customer_name(), "Mehmet Demir")

    def test_get_card_expiry(self):
        self.assertEqual(self.card.get_card_expiry(), "12/25")

    def test_set_card_expiry(self):
        self.card.set_card_expiry("01/30")
        self.assertEqual(self.card.get_card_expiry(), "01/30")

    def test_get_pin(self):
        self.assertEqual(self.card.get_pin(), "1234")

    def test_set_pin(self):
        self.card.set_pin("5678")
        self.assertEqual(self.card.get_pin(), "5678")



class TestAccountMethods(unittest.TestCase):
    def setUp(self):
        self.account = Account("123456789")

    def test_get_account_number(self):
        self.assertEqual(self.account.get_account_number(), "123456789")

    def test_set_account_number(self):
        self.account.set_account_number("987654321")
        self.assertEqual(self.account.get_account_number(), "987654321")

    def test_get_total_balance(self):
        self.assertEqual(self.account.get_total_balance(), 0.0)

    def test_set_total_balance(self):
        self.account.set_total_balance(1000.0)
        self.assertEqual(self.account.get_total_balance(), 1000.0)

    def test_get_available_balance(self):
        self.assertEqual(self.account.get_available_balance(), 0.0)

    def test_set_available_balance(self):
        self.account.set_available_balance(500.0)
        self.assertEqual(self.account.get_available_balance(), 500.0)



class TestAddCustomer(unittest.TestCase):
    def setUp(self):
        self.initial_customer_count = len(customer_list)  # Başlangıçtaki müşteri sayısını saklarız

    def test_add_customer(self):
        add_customer("Ahmet Yılmaz", "İstiklal Cad. No: 123", "ahmet@example.com", "0555 555 55 55", "Aktif", "1234 5678 9101 1121", "Ahmet Yılmaz", "12/25", "1234", "789101112")
        new_customer_count = len(customer_list)  # Fonksiyon çağrıldıktan sonraki müşteri sayısını alırız

        # Yeni müşteri eklenip eklenmediğini kontrol ederiz
        self.assertEqual(new_customer_count, self.initial_customer_count + 1)

        # Eklenen müşterinin bilgilerini kontrol ederiz
        last_customer = customer_list[-1]
        self.assertEqual(last_customer.get_name(), "Ahmet Yılmaz")
        self.assertEqual(last_customer.get_address(), "İstiklal Cad. No: 123")
        self.assertEqual(last_customer.get_email(), "ahmet@example.com")
        self.assertEqual(last_customer.get_phone(), "0555 555 55 55")
        self.assertEqual(last_customer.get_status(), "Aktif")
        # Diğer müşteri bilgileri de kontrol edilebilir


class TestCheckAccountNumber(unittest.TestCase):
    def setUp(self):
        self.initial_customer_count = len(customer_list)  # Başlangıçtaki müşteri sayısını saklarız

    def test_check_account_number_existing(self):
        # Öncelikle bir müşteri ekleyelim
        add_customer("Ahmet Yılmaz", "İstiklal Cad. No: 123", "ahmet@example.com", "0555 555 55 55", "Aktif", "1234 5678 9101 1121", "Ahmet Yılmaz", "12/25", "1234", "789101112")
        account_number_to_check = "789101112"

        result = check_account_number(account_number_to_check)

        # Hesap numarası varsa True dönmeli
        self.assertTrue(result)

    def test_check_account_number_not_existing(self):
        account_number_to_check = "999999999"  # Var olmayan bir hesap numarası

        result = check_account_number(account_number_to_check)

        # Hesap numarası yoksa False dönmeli
        self.assertFalse(result)

    def tearDown(self):
        # Test sonunda eklenen müşteriyi silelim (istenirse)
        del customer_list[-1]


class TestCheckCardPin(unittest.TestCase):
    def setUp(self):
        self.initial_customer_count = len(customer_list)  # Başlangıçtaki müşteri sayısını saklarız

    def test_check_card_pin_existing(self):
        # Öncelikle bir müşteri ekleyelim
        add_customer("Ahmet Yılmaz", "İstiklal Cad. No: 123", "ahmet@example.com", "0555 555 55 55", "Aktif", "1234 5678 9101 1121", "Ahmet Yılmaz", "12/25", "1234", "789101112")
        pin_to_check = "1234"
        account_number = "789101112"

        result = check_card_pin(pin_to_check, account_number)

        # Pin ve account_number eşleşiyorsa True dönmeli
        self.assertTrue(result)

    def test_check_card_pin_not_existing(self):
        pin_to_check = "9999"  # Var olmayan bir pin
        account_number = "123456789"  # Var olmayan bir account_number

        result = check_card_pin(pin_to_check, account_number)

        # Pin veya account_number eşleşmiyorsa False dönmeli
        self.assertFalse(result)

    




if __name__ == '__main__':
    unittest.main()
