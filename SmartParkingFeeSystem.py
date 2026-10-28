import math
import sys


Vehicle_Number = (input("Enter the Vehicle Number: "))
while True :
    Entry_Hour = int(input("Entry Timings in Hour: "))
    Entry_Minute = int(input("Entry Timings in Minute: "))
    Exit_Hour = int(input("Exit Timings in hour: "))
    Exit_Minute = int(input("Exit Timings in Minute: "))

    entry = Entry_Hour * 60 + Entry_Minute
    exit = Exit_Hour * 60 + Exit_Minute


    if not (0 <= Entry_Hour <= 23 and 0 <= Exit_Hour <= 23 and 0 <= Entry_Minute <= 59 and 0 <= Exit_Minute <= 59) or exit < entry:
        print("Invalid Timings")
        sys.exit()
    else:
        break

    additional_charge = 0
    charge = 0

Vehicle_type = input("Enter the type of vehicle: ")
if Vehicle_type.upper() == "BIKE" :
    if exit-entry <= 60:
        charge = 20
    elif 60 <exit-entry< 180:
        charge = 15
    elif 180 <= exit-entry < 360:
        charge = 10
    else:
        charge = 10
        additional_charge = 100
elif Vehicle_type.upper() == "CAR" :
        if exit-entry < 60:
            charge = 50
        elif 60 <=exit-entry< 180:
            charge = 30
        elif 180 <=exit-entry < 360:
            charge = 20
        else:
            charge = 20
            additional_charge = 100

parking_time = exit - entry 
parking_charge = (math.ceil(parking_time/60) * charge) + additional_charge

print("Vehicle_Number:", Vehicle_Number)
print("Total Parking tmings is :", exit - entry)
print(f"The total Amount to be paid is ${parking_charge}")