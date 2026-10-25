class normal_customer():
    discount = 0

    def __init__( self, customer_name, product_price, quantity):
        self.customer_name = customer_name
        self.product_price = product_price
        self.quantity = quantity
        
        payable_amount = self.product_price * self.quantity
        total = payable_amount - (payable_amount * self.discount)
        print(f"{customer_name} has bought {quantity} products of price {product_price} \n Total amount to be paid is {total}")

class premium_customer(normal_customer):
    discount = 0.1

customer_name=input("Enter the name of the Customer: ")
product_price=int(input("Enter the price of the Product:$ "))
quantity=int(input("Enter the quantity of product bought: "))
option=int(input("Enter 1 for Normal Customer, 2 for Premium Customer: "))
if option==1:
    normal_customer(customer_name, product_price, quantity)
else:
    premium_customer(customer_name, product_price, quantity)