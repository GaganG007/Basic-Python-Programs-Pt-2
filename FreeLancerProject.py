class freelancer():
    def __init__( self, Client_name, Project_Amount, Days_Taken):
        self.Client_name = Client_name
        self.Project_Amount = Project_Amount
        self.Days_Taken = Days_Taken 

Client_Name = input("Enter the client name : ")
Project_Amount = int(input("Enter the project amount: "))
Days_Taken = int(input("Enter the Duration you worked on the Project: "))

def normal_project():
    deduction_amt = 0
    print(f"Congrats on finishing the project in {Days_Taken} days, Your total payment is {Project_Amount}.")


def Urgent_project():
    total = Project_Amount + (Project_Amount * 0.20)
    if Days_Taken > 10 :
        total = total - 1000
        print("$1000 deducted because the deadline is over.")
    print(f"Congrats on finishing the project in {Days_Taken} days, Your total payment is {total}.")
    
def International_Project():
    total = Project_Amount - (Project_Amount * 0.15)
    print("15% Deducted as it is an International Project.")
    if total >= 100000 :
        total += 5000
        print("Bonus of $5000")
    print(f"Congrats on finishing the project in {Days_Taken} days, Your total payment is {total}.")


while True:
    project_type = input("Enter the Project Type: ").strip().upper()

    if project_type == "NORMAL" :
        normal_project()
        break
    elif project_type == "URGENT" :
        Urgent_project()
        break
    elif project_type == "INTERNATIONAL" :
        International_Project()
        break
    else:
        print("Enter Invalid Project Type")