from customer import Card
from customer import Account

card_example = Card("1234567890123456", "Ahmet Yılmaz", "12/25", 1234)
user_account = Account("1234567890")
_cardPassword = card_example.get_pin()
login = False
sifre_sayac = 3
user_account.set_available_balance(1234)

while True:
    if login == False:
        print(card_example.get_pin())
        password = int(input("Welcome! Please enter your password"))
        print(password)
    if password == _cardPassword:
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
                withdraw_value = 20
            elif(select_withdraw == 2):
                withdraw_value = 40
            elif(select_withdraw == 3):
                withdraw_value = 100
            elif(select_withdraw == 4):
                withdraw_value = int(input("How much money do you want to deposit"))
            elif choose == 5:
                break
            else:
                print("Please select between 1-5")

            if user_account.get_available_balance() < withdraw_value:
                print("Insufficient funds are not available")
                continue
            new_available_balance = int(user_account.get_available_balance()) - withdraw_value
            user_account.set_available_balance(new_available_balance)
        elif choose == 2:
            deposit_value = int(input("How much money do you want to deposit"))
            new_available_balance = int(user_account.get_available_balance()) - deposit_value
            user_account.set_available_balance(new_available_balance)
        elif choose == 3:
            print("Your balance {} $".format(user_account.get_available_balance()))
        elif choose == 5:
            print("Good Bye")
            break
        else:
            print("Please select between 1-5")
    else:
        sifre_sayac -=1
        if sifre_sayac <= 0:
            print("Your card blocked")
            break