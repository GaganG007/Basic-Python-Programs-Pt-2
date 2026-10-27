class bank_account():
    def __init__ ( self, Account_number, name, balance):
        self.Account_number = Account_number
        self.name = name
        self.balance = balance

class transaction(bank_account):
    def __init__( self, Account_number, name, balance, mode, Amount):
        super().__init__( Account_number, name, balance)
        self.mode = mode
        self.Amount = Amount
        self.status = ""

        if self.mode.upper() == "WITHDRAW" :
            if self.Amount <= self.balance :
                self.balance -= self.Amount
                self.status = "SUCCESS"
                print(f"Withdraw {self.Amount} SUCCESS, New Balance is {self.balance}")
                if self.Amount >= 20000 :
                    print("LARGE WITHDRAWAL")
            else :
                self.status = "REJECTED"
                print(f"Withdraw {self.Amount} REJECTED, Insufficient Balance")
        elif self.mode.upper() == "DEPOSIT" :
            self.balance += self.Amount
            self.status = "SUCCESS"
            print(f"Deposit {self.Amount} SUCCESS, New balance is {self.balance}")
        else :
            self.status = "INVALID"
            print("Unrecognized Characters")

        print(f"The Final Balance : {self.balance}")

Accounts = {1001: bank_account(1001,"Aman",25000),
            1002: bank_account(1002,"Riya",42000),
            1003: bank_account(1003,"Rahul",18000)}

transactions = [(1001,"WITHDRAW",5000),
                (1002,"DEPOSIT",10000),
                (1001,"WITHDRAW",23000), 
                (1003,"WITHDRAW",3000),
                (1002,"WITHDRAW",52000), 
                (1003,"DEPOSIT",7000)]

success_withdrawals = 0
rejected_withdrawals = 0
total_deposited = 0
total_withdrawn = 0

with open("audit.txt", "w") as audit:
    audit.write("----ATM TRANSACTION AUDIT----\n")

    for Account_number, mode, amount in transactions:
        acc = Accounts[Account_number]
        print(f"----Transaction for {acc.name}")
        t = transaction(acc.Account_number, acc.name, acc.balance, mode, amount)
        acc.balance = t.balance

        line = f"{acc.Account_number} {acc.name} {mode.upper()} {amount} {t.status} | Balance: {t.balance}"
        if mode.upper() == "WITHDRAW" and t.status == "SUCCESS" and amount >= 20000 :
            line += " | LARGE WITHDRAWAL"
        audit.write(line + "\n")

        if mode.upper() == "WITHDRAW" :
            if t.status == "SUCCESS" :
                success_withdrawals += 1
                total_withdrawn += amount
            else :
                rejected_withdrawals += 1
        elif mode.upper() == "DEPOSIT" :
            total_deposited += amount

print("\n----Final Balances----")
for acc in Accounts.values():
    print(acc.Account_number, acc.name, acc.balance)

print("Successful withdrawals:", success_withdrawals)
print("Rejected withdrawals:", rejected_withdrawals)
print("Total deposited:", total_deposited)
print("Total withdrawn:", total_withdrawn)

top = max(Accounts.values(), key=lambda a: a.balance)
print("Highest balance:", top.Account_number, top.name, top.balance)