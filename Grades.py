Total = 0
Lowest = 100
Count = 1

while Count <= 5 :
    Mark = input(f"Enter the marks of subject {Count}: ").strip()
    if Mark.isdigit() and int(Mark) <= 100 :
        Mark = int(Mark)
        Total += Mark
        if Mark < Lowest :
            Lowest = Mark
        Count += 1
    else :
        print("Marks must be a number from 0 to 100.")

Average = Total / 5

print(f"Total: {Total}")
print(f"Average: {Average}")

if Lowest < 35 :
    print("Result: FAIL")
else :
    if Average >= 90 :
        Grade = "A+"
    elif Average >= 75 :
        Grade = "A"
    elif Average >= 60 :
        Grade = "B"
    elif Average >= 50 :
        Grade = "C"
    else :
        Grade = "D"

    print(f"Grade: {Grade}")

    if Average > 75 and Lowest >= 60 :
        print("Result: PASS with DISTINCTION")
    else :
        print("Result: PASS")