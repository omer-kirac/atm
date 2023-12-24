from abc import ABC


class Transaction(ABC):
    def __init__(self, id, creation_date, status):
        self.__transaction_id = id
        self.__creation_time = creation_date
        self.__status = status

    def make_transaction(self):
        None

    # Getter ve setter metodları
    def get_transaction_id(self):
        return self.__transaction_id

    def set_transaction_id(self, new_id):
        self.__transaction_id = new_id

    def get_creation_time(self):
        return self.__creation_time

    def set_creation_time(self, new_creation_date):
        self.__creation_time = new_creation_date

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        self.__status = new_status


class BalanceInquiry(Transaction):
    def __init__(self, account_id):
        self.__account_id = account_id

    def get_account_id(self):
        return self.__account_id

    def set_account_id(self, new_account_id):
        self.__account_id = new_account_id


class Deposit(Transaction):
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, new_amount):
        self.__amount = new_amount


class CheckDeposit(Deposit):
    def __init__(self, check_number, bank_code):
        self.__check_number = check_number
        self.__bank_code = bank_code

    def get_check_number(self):
        return self.__check_number

    def set_check_number(self, new_check_number):
        self.__check_number = new_check_number

    def get_bank_code(self):
        return self.__bank_code

    def set_bank_code(self, new_bank_code):
        self.__bank_code = new_bank_code


class CashDeposit(Deposit):
    def __init__(self, cash_deposit_limit):
        self.__cash_deposit_limit = cash_deposit_limit

    def get_cash_deposit_limit(self):
        return self.__cash_deposit_limit

    def set_cash_deposit_limit(self, new_cash_deposit_limit):
        self.__cash_deposit_limit = new_cash_deposit_limit


class Withdraw(Transaction):
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, new_amount):
        self.__amount = new_amount


class Transfer(Transaction):
    def __init__(self, destination_account_number):
        self.__destination_account_number = destination_account_number

    def get_destination_account(self):
        return self.__destination_account_number

    def set_destination_account(self, new_destination_account_number):
        self.__destination_account_number = new_destination_account_number
