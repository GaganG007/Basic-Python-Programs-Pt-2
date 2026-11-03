class Payroll():
    def __init__( self, name, role, basic_pay, Gross):
        self.name = name
        self.role = role
        self.basic_pay = basic_pay
        self.Gross = Gross

class Employee(Payroll):
    def __init__(self, name, role, basic_pay, Gross):
        super().__init__(name, role, basic_pay,Gross)
        HRA = self.basic_pay * 0.2
        DA = self.basic_pay * 0.1
        Gross = HRA + DA + basic_pay
        if Gross <= 30000:
            TAX = 0
        elif 30000 < Gross <= 60000:
            TAX = Gross * 0.05
        else :
            TAX = Gross * 0.1
        Net_Salary = Gross - TAX
        print(f"Name:{name}({role})")
        print(f"HDA : ${HRA}    DA: ${DA}")
        print(f"Total Final Salary: ${Gross}")
        print(f"Tax : ${TAX}")
        print(f"Net Salary: ${Net_Salary}")

class Manager(Payroll):
    def __init__(self, name, role, basic_pay, Gross):
        super().__init__(name, role, basic_pay,Gross)
        HRA = self.basic_pay * 0.2
        DA = self.basic_pay * 0.1
        final_pay = self.basic_pay + 5000 + HRA + DA
        if final_pay <= 30000:
            MTAX = 0
        elif 30000 < final_pay <= 60000:
            MTAX = final_pay * 0.05
        else :
            MTAX = final_pay * 0.1
        Net_salary = final_pay - MTAX
        print(f"Name:{name}({role})")
        print(f"HDA : ${HRA}    DA: ${DA}")
        print(f"Total Final Salary: ${final_pay}")
        print(f"Tax : ${MTAX}")
        print(f"Net Salary: ${Net_salary}")

name = input("Enter the Name:")
role = input("Employee / Manager:")
basic_pay = int(input("Enter the Basic Pay:"))
Gross = 0

if role.strip().upper() == "MANAGER":
    Manager(name, role, basic_pay,Gross)
elif role.strip().upper() == "EMPLOYEE":
    Employee(name, role, basic_pay, Gross)
else:
    print("Unidentified Role")