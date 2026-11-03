import sys
salary = int(input("Enter the Monthly Salary: "))
age = int(input("Enter the Age: "))
EMI = int(input("Enter the existing Monthly EMI: "))
Loan_Amt = int(input("Enter the Loan Amount: "))
Tenure = int(input("Enter the Tenure in Months: "))
conditions = True
reason = open("Reason.txt", "w")
reason.write("---------- Loan Eligibility Check Reasons --------\n")

if 21 <= age <= 58 and salary >= 25000 and EMI <= (salary * 0.4) and Loan_Amt < (salary * 20) and 12 <= Tenure <= 60:
    print("Congrats You are Eligible for the Loan.")
else:
    print("You're Not Eligible for the Loan.")


if  21 <= age <= 58:
    pass
else :
    with open("Reason.txt", "a") as reason:
        reason.write("Age must be between 21 and 58.\n")


if salary >= 25000:
    pass
else:
    with open("Reason.txt", "a") as reason:
        reason.write("Salary is not sufficient.\n")


if EMI <= (salary * 0.4):
    pass
else:
    with open("Reason.txt", "a") as reason:
        reason.write("EMI is more than 40% of your Monthly Salary.\n")


if Loan_Amt < (salary * 20) : 
    pass
else:
    with open("Reason.txt", "a") as reason:
        reason.write("Loan Amount should be less than 20 times of your Monthly Salary.\n")

if 12 <= Tenure <= 60:
    pass
else :
    with open("Reason.txt", "a") as reason:
        reason.write("Tenure must be between 12 and 60.\n")

Interest = (Loan_Amt * 0.1 * Tenure) / 100
New_EMI = (Loan_Amt + Interest) / Tenure

if New_EMI + EMI < (salary * 0.5):
    pass
else:
    with open("Reason.txt","a") as reason:
        reason.write("Total EMI (Existing + New) is more than 50% of your Monthly Salary.\n")

reason.close()

