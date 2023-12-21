class Bank:
  def __init__(self, name, bank_code):
    self.__name = name
    self.__bank_code = bank_code

  # Getter ve Setter metotları
  def get_name(self):
    return self.__name

  def set_name(self, new_name):
    self.__name = new_name

  def get_bank_code(self):
    return self.__bank_code

  def set_bank_code(self, new_bank_code):
    self.__bank_code = new_bank_code

  def add_atm(self, atm):
    None  # ATM ekleme metodu


class ATM:
  def __init__(self, id, location):
    self.__atm_id = id
    self.__location = location

    # Diğer özellikler...

  # Getter ve Setter metotları
  def get_atm_id(self):
    return self.__atm_id

  def set_atm_id(self, new_id):
    self.__atm_id = new_id

  def get_location(self):
    return self.__location

  def set_location(self, new_location):
    self.__location = new_location

  def authenticate_user(self):
    None  # Kullanıcı doğrulama metodu

  def make_transaction(self, customer, transaction):
    None  # İşlem yapma metodu


class CashDispenser:
  def __init__(self):
    self.__total_five_dollar_bills = 0
    self.__total_twenty_dollar_bills = 0

  def dispense_cash(self, amount):
    None

  def can_dispense_cash(self):
    None


class Keypad:
  def get_input(self):
    None


class Screen:
  def show_message(self, message):
    print(message)

  def get_input(self):
    try:
      return int(input("Welcome! Please enter your account number: "))
    except ValueError:
      print("Invalid input. Please enter a valid account number.")
      return None


class Printer:
  def print_receipt(self):
    return print("RECEIPT")


class CheckDeposit:
    def __init__(self):
        None


class CashDeposit:
    def __init__(self):
        None


class DepositSlot(ATM):
  def __init__(self):
    self.__total_amount = 0.0

  def get_total_amount(self):
    return self.__total_amount


class CheckDepositSlot(DepositSlot):
  def get_check_amount(self):
    None


class CashDepositSlot(DepositSlot):
  def receive_dollar_bill(self):
    None

