while True :
    Units = input("Enter the units consumed: ").strip()
    if Units.isdigit() :
        Units = int(Units)
        break
    print("Invalid input, enter a whole number.")

if Units <= 100 :
    Energy = Units * 5
elif Units <= 200 :
    Energy = 100 * 5 + (Units - 100) * 7
else :
    Energy = 100 * 5 + 100 * 7 + (Units - 200) * 10

Fixed = 50
Bill = Energy + Fixed

if Bill > 2000 :
    Surcharge = Bill * 0.10
else :
    Surcharge = 0

Total = Bill + Surcharge

print(f"Energy charge: Rs. {Energy}")
print(f"Fixed charge: Rs. {Fixed}")
print(f"Surcharge: Rs. {Surcharge}")
print(f"Total Bill = Rs. {Total}")