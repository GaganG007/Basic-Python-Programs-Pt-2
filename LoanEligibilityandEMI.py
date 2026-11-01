salary = int(input("Enter the Monthly Salary: "))
age = int(input("Enter the Age: "))
EMI = int(input("Enter the existing Monthly EMI: "))
Loan_Amt = int(input("Enter the Loan Amount: "))
Tenure = int(input("Enter the Tenure in Months: "))
    
if  21 <= age <= 58:
    pass
else :
    print("Your not eligible because your not in the required age range.")


if salary < 25000:
    print("Minimum Salary required is 25000")
else:
    print("Your Salary is above the required Amount.")


if EMI > (salary * 0.4) :
    print("You're Not eligible as your EMI is more than 40% of your Monthly Salary.")
else:
    pass


if Loan_Amt < (salary * 20) : 
    pass
else:
    print("Loan Amount is too high.")


if 12 < Tenure < 60:
    pass
else :
    print("Tenure must be between 12 and 60.")
    

Interest = (Loan_Amt * '0.1' * Tenure) / 100
New_EMI = (Loan_Amt + Interest) / Tenure

if New_EMI + EMI > (salary * 0.5):
    print("Not Eligible.")
else:
    print("Congrats You are Eligible for the Loan.")

