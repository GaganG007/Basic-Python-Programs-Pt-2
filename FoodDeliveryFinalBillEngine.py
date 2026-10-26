import random
class bill():
    def __init__( self, OrderID, Customername, FoodAmount, Distance, Membership, Coupon):
        self.OrderID = OrderID
        self.Customername = Customername
        self.FoodAmount = FoodAmount
        self.Distance = Distance
        self.Membership = Membership
        self.Coupon = Coupon

class final_amount(bill):
    def __init__( self, FoodAmount, Distance, Delivery):
        super().__init__(None ,None, FoodAmount, Distance, None, None)
        if Distance < 5 :
            self.Delivery = 40
        elif Distance < 10:
            self.Delivery = 70
        else :
            self.Delivery = 120

class member(bill):
    def __init__(self, FoodAmount, Distance, Membership, Delivery):
        super().__init__(None , None, FoodAmount, Distance, Membership, None)
        self.Delivery = Delivery
        if FoodAmount >= 500:
            self.Delivery = 0
            print("You get free delivery!!")
        else :
            print("Free delivery needs a bill of 500 or more.")

class coupon(bill):
    def __init__( self, FoodAmount, Coupon):
        super().__init__(None , None, FoodAmount, None, None, Coupon)
        coupon_code = input("Enter the Coupon: ")
        if coupon_code.strip().upper() == "SAVE50":
            self.FoodAmount -= 50
            print("You got $50 off.")
        else :
            print("Invalid Coupon")

class Bill_amount(bill):
    def __init__(self, OrderID, Customername, FoodAmount, Distance, Membership, Coupon, Delivery):
        super().__init__(OrderID, Customername, FoodAmount, Distance, Membership, Coupon)
        if self.FoodAmount > 1200:
            self.FoodAmount = self.FoodAmount - (self.FoodAmount*0.1)
            print("Congrats you got additional 10% off!!")
        total = self.FoodAmount + Delivery
        print(f"Food amount after offers: {self.FoodAmount}")
        print(f"Delivery charge: {Delivery}")
        print(f"{Customername}'s total bill is {total}")
        print(f"Order id:{OrderID}") 

Delivery = 0
OrderID = random.randint(1000,9999)
Customername = input("Enter the customer Name: ")
FoodAmount = float(input("Enter the Bill Amount: "))
Distance = int(input("Enter the distance to the Customer Place: "))
f = final_amount( FoodAmount, Distance, Delivery)
Delivery = f.Delivery

Membership = input("Does the customer have a Membership?: ")
if Membership.upper() == 'YES' :
    m = member(FoodAmount, Distance, Membership, Delivery)
    Delivery = m.Delivery
else:
    print("Delivery charges apply since you are not a Member.")

Coupon = input("Does the customer have a Coupon?: ")
if Coupon.upper() == 'YES' :
    c = coupon( FoodAmount, Coupon)
    FoodAmount = c.FoodAmount
else :
    print("No coupon applied.")

Bill_amount( OrderID, Customername, FoodAmount, Distance, Membership, Coupon, Delivery)