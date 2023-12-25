import unittest
from transaction import Withdraw
from transaction import Deposit
from transaction import Transfer



class TestDeposit(unittest.TestCase):
    def setUp(self):
        self.deposit = Deposit(100)  # Başlangıçta 100 birimlik bir depozit oluşturuyoruz

    def test_get_amount(self):
        self.assertEqual(self.deposit.get_amount(), 100)  # Başlangıçtaki miktarın doğru olup olmadığını kontrol ediyoruz

    def test_set_amount(self):
        self.deposit.set_amount(200)  # Miktarı değiştiriyoruz
        self.assertEqual(self.deposit.get_amount(), 200)  # Yeni miktarın doğru şekilde ayarlanıp ayarlanmadığını kontrol ediyoruz


class TestWithdraw(unittest.TestCase):
    def setUp(self):
        self.withdraw = Withdraw(200)  # Başlangıçta 200 birimlik bir çekme işlemi oluşturuyoruz

    def test_get_amount(self):
        self.assertEqual(self.withdraw.get_amount(), 200)  # Başlangıçtaki miktarın doğru olup olmadığını kontrol ediyoruz

    def test_set_amount(self):
        self.withdraw.set_amount(300)  # Miktarı değiştiriyoruz
        self.assertEqual(self.withdraw.get_amount(), 300)  # Yeni miktarın doğru şekilde ayarlanıp ayarlanmadığını kontrol ediyoruz

class TestTransfer(unittest.TestCase):
    def setUp(self):
        self.transfer = Transfer("789101112")  # Başlangıçta 789101112 numaralı bir transfer işlemi oluşturuyoruz

    def test_get_destination_account(self):
        self.assertEqual(self.transfer.get_destination_account(), "789101112")  # Başlangıçtaki hedef hesap numarasının doğru olup olmadığını kontrol ediyoruz

    def test_set_destination_account(self):
        self.transfer.set_destination_account("987654321")  # Hedef hesap numarasını değiştiriyoruz
        self.assertEqual(self.transfer.get_destination_account(), "987654321")  # Yeni hedef hesap numarasının doğru şekilde ayarlanıp ayarlanmadığını kontrol ediyoruz


if __name__ == '__main__':
    unittest.main()
