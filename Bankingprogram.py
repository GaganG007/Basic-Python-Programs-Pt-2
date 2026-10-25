import sys
import random
account_number = random.randint(1,1000000)
balance = 0
is_running = True

def show_balance():
    print(f"Your balance is {balance}")

def deposit():
    global balance
    deposit_amount = float(input("Enter the amount you want to deposit: "))
    if deposit_amount <= 0:
        print("Amount can't be negative or 0")
        return
    balance += deposit_amount
    print(f"Your balance is {balance}")

def withdraw():
    global balance
    withdraw_amount = float(input("Enter the amount you want to withdraw: "))
    if withdraw_amount <= 0:
        print("Amount can't be negative or 0")
        return
    if withdraw_amount > balance:
        print("Insufficient Balance")
        return
    balance -= withdraw_amount
    print(f"Your balance is {balance}")

def exit():
    print("Thankyou for visiting Supreme Banks :)")
    sys.exit()

is_error = True
while is_error:
    user=input("Print 'n' for new user and 'e' for existing user: ").lower().strip()
    if user == 'n':
        name = input("Enter your name: ")
        print(f"Welcome {name} to the Banking Program")
        print("Your account has been created successfully")
        print(f"Your Account Number is {account_number}")
        print("Your current balance is $0")
        break
        is_error = False
    elif user == 'e':
        print("Welcome to Supreme Banks")
        print("Have a Wonderful Day!!")
        break
        is_error = False
    else:
        print("Unidentified format enter e or n, try again")

def main():
    print("Welcome to Supreme Banks")
    print("Choose one service from the services listed below")
    print("1.Account Balance")
    print("2.Deposit Amount")
    print("3.Withdraw Cash")
    print("4.Exit")

    while is_running :
        choice = input("Enter the choice(1-4): ")
        if choice == '1':
            show_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            exit()
        else :
            print("Unidentified Format")

if __name__ == '__main__':
    main()