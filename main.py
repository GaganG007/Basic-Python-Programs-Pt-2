class ride():
    def __init__(self, Customer_name, Distance_Traveled):
        self.Customer_name = Customer_name
        self.Distance_Traveled = Distance_Traveled

    def calculate_fare(self):
        total_fare = self.Distance_Traveled * 12
        print(f"Total fare for {self.Customer_name} for {self.Distance_Traveled} km is ₹{total_fare}")
        return total_fare
    
class Premiumride(ride):
    def __init__(self, Customer_name, Distance_Traveled):
        super().__init__(Customer_name, Distance_Traveled)

    def calculate_fare(self):
        premium_fare = (self.Distance_Traveled * 12) + 50
        print(f"Premium Total fare for {self.Customer_name} for {self.Distance_Traveled} km is ₹{premium_fare}")
        return premium_fare

name=input("Enter Customer name: ")
distance=int(input("Enter Distance traveled in km: "))
print("Choose ride type: 1. Normal Ride 2. Premium Ride")
ride_type=int(input("Enter your choice (1 or 2): "))
if ride_type == 1:
    ride1 = ride(name, distance)
    ride1.calculate_fare()
else:
    ride2 = Premiumride(name, distance)
    ride2.calculate_fare()