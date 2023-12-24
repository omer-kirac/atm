from customer import Card
from customer import Account
from customer import add_customer
from customer import check_account_number
from customer import check_card_pin
from customer import CheckingAccount
from atm import Screen
from atm import Printer
from atm import Keypad
from transaction import Withdraw
from transaction import Deposit
from transaction import Transfer


"""card_example = Card("1234567890123456", "Ahmet Yılmaz", "12/25", 1234)
user_account = Account(1234567890)
card_example2 = Card("1234567890123333", "Mehmet Yılmaz", "12/25", 1234)
user_account2 = Account(1234567222)

account_list = []
account_list.append(1234567890)
account_list.append(1234567222)"""

# Örnek müşterileri ekleme
add_customer("Mehmet", "Ankara", "mehmet@email.com", "5556667778", "Silver", "9876543210987654", "Mehmet Yıldırım", "11/24", 4321, 123123)
add_customer("Ayşe", "İzmir", "ayse@email.com", "5334448899", "Bronze", "1111222233334444", "Ayşe Demir", "09/23", 6789, 567567)
add_customer("Fatma", "Bursa", "fatma@email.com", "5325551122", "Gold", "5555444433332222", "Fatma Çelik", "08/25", 9876, 789789)



login = False
sifre_sayac = 2
"""user_account.set_available_balance(1234)"""
Account(123123).set_available_balance(1234)
screen = Screen()
printer = Printer()
keypad = Keypad()
withdraw = Withdraw(0)
deposit = Deposit(0)
transfer = Transfer(0)
card = Card(0,0,0,0)

id = None
while True:
    if login == False:
        if id == None:
            screen.show_message("Welcome! Please enter your account number: ")
            id = keypad.get_input()
        if check_account_number(id):
            user_account = Account(id)
            screen.show_message("Please enter your password:")
            password = keypad.get_input()
            if check_card_pin(password,id) == False:
                if sifre_sayac != 0:
                    screen.show_message("You have {}$ attemps left for your card code".format(sifre_sayac))
        else:
            screen.show_message("Account does not exist ")
            continue

    if check_card_pin(password,id):
        login = True
        print("""
        1.Withdraw
        2.Deposit
        3.Balance Inquiry
        4.Transfer
        5.Exit
        """)
        choose = int(input("Select a process"))
        if choose == 1:
            #ismi değiştirilecek withdraw_value'nun
            select_withdraw = int(input(""" 
            1.20$
            2.40$
            3.100$
            4.Custom amount
            5.Cancel
            """))
            if(select_withdraw == 1):
                withdraw.set_amount(20)
            elif(select_withdraw == 2):
                withdraw.set_amount(40)
            elif(select_withdraw == 3):
                withdraw.set_amount(100)
            elif(select_withdraw == 4):
                withdraw.set_amount(int(input("How many dollars would you like to withdraw")))
            elif choose == 5:
                break
            else:
                screen.show_message("Please select between 1-5")

            if user_account.get_available_balance() < withdraw.get_amount():
                print("Insufficient funds are not available")
                continue
            new_available_balance = int(user_account.get_available_balance()) - withdraw.get_amount()
            user_account.set_available_balance(new_available_balance)
        elif choose == 2:
            deposit.set_amount(int(input("How many dollars would you like to deposit")))
            user_account.set_available_balance(int(user_account.get_available_balance()) + deposit.get_amount())
        elif choose == 3:
            print("Your balance {}$".format(user_account.get_available_balance()))
        elif choose == 4:
            transfer_amount = int(input("How many dollars would you like to transfer"))
            if user_account.get_available_balance() < transfer_amount:
                print("Insufficient funds are not available")
                continue
            transfer.set_destination_account(int(input("Enter number of receiver's account")))
            if check_account_number(transfer.get_destination_account()):
                new_available_balance = int(user_account.get_available_balance()) - transfer_amount
                user_account.set_available_balance(new_available_balance)
                print("{}$ sent successfully".format(transfer_amount))
                receipt = input("Print receipt(Yes/No)").lower()
                if receipt == 'yes':
                    printer.print_receipt(transfer_amount)
            else:
                user_input = input("This account was not found. Would you like to try again?(Yes/No)").lower()
                if user_input == 'yes':
                    continue
                elif user_input == 'no':
                    break
                else:
                    print("You have written an invalid text, just write yes or no")



        elif choose == 5:
            print("Good Bye")
            break
        else:
            print("Please select between 1-5")
    else:
        sifre_sayac -=1
        if sifre_sayac < 0:
            print("Your card blocked")
            break