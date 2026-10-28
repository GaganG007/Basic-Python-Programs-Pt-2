import sys
class ATM():
    def __init__( self, Balance, PIN):
        self.Balance = Balance
        self.PIN = int(PIN)
        i = 0
        Access = False
        while i < 3:
            usr_PIN = int(input("Enter the PIN: "))
            if usr_PIN == self.PIN:
                print("Correct PIN!")
                Access = True
                break
            elif usr_PIN != self.PIN:
                i += 1
                if i < 3 :
                    print(f"Wrong PIN {3-i} tries remain.")
            
        if Access == False:
            print("Maximum attempts reached.")
            sys.exit()

acc1 = ATM( 35000, 2468)
Balance = acc1.Balance

while True :
    withdrawal_amount = int(input("Enter the Amount to Withdraw: "))
    if withdrawal_amount < 500 :
        print("Minimum Withdrawal should be greater than 500.")
        continue
    elif withdrawal_amount > Balance :
        print("Insufficient Balance")
        continue
    elif withdrawal_amount % 500 != 0 :
        print("Withdrawal Amount should be a multiple of 500.")
        continue
    elif Balance < 1000 :
        print("Minimum Balance must be 1000.")
        continue
    else :
        Balance -= withdrawal_amount


    print("Withdrawal Successfull")
    print(f"Amount Withdrawn: ${withdrawal_amount}, Balance : ${Balance}")

    while True :
        repeat = input("Do you want another transaction Yes/No :").strip().upper()
        if repeat == "YES" or repeat == "NO":
            break
        print("Type Yes or No.")

    if repeat == "NO":
        print("Thankyou!!")
        break