while True :
    Room = input("Enter the room type (STANDARD / DELUXE / SUITE): ").strip().upper()
    if Room == "STANDARD" :
        Rate = 2000
        break
    elif Room == "DELUXE" :
        Rate = 3500
        break
    elif Room == "SUITE" :
        Rate = 6000
        break
    print("Invalid room type.")

while True :
    Nights = input("Enter the number of nights: ").strip()
    if Nights.isdigit() and 1 <= int(Nights) <= 30 :
        Nights = int(Nights)
        break
    print("Nights must be a number from 1 to 30.")

while True :
    Extra = input("Extra bed (YES / NO): ").strip().upper()
    if Extra == "YES" or Extra == "NO" :
        break
    print("Please enter YES or NO.")

RoomCharges = Rate * Nights

if Nights >= 10 :
    Discount = RoomCharges * 0.15
elif Nights >= 5 :
    Discount = RoomCharges * 0.10
else :
    Discount = 0

AfterDiscount = RoomCharges - Discount

if Extra == "YES" :
    ExtraBed = 500 * Nights
else :
    ExtraBed = 0

Subtotal = AfterDiscount + ExtraBed

if Subtotal <= 10000 :
    GST = Subtotal * 0.12
else :
    GST = Subtotal * 0.18

Total = Subtotal + GST

print(f"Room charges: Rs. {RoomCharges}")
print(f"Discount: Rs. {Discount}")
print(f"Extra bed: Rs. {ExtraBed}")
print(f"Subtotal: Rs. {Subtotal}")
print(f"GST: Rs. {GST}")
print(f"Total: Rs. {Total}")