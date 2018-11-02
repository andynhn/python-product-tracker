# By Andy Nguyen
# Product Assignment

class Product:
    def __init__ (self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self
    
    def addTax(self, sales_tax):
        self.price = self.price + (self.price*sales_tax)
        return self

    def returnItem(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "like_new":
            self.status = "for sale"
        if reason_for_return == "opened":
            self.status = "used"
            self.price = self.price*0.80
        return self
    
    def displayInfo(self):
        print(f"Price = ${self.price}")
        print(f"Item Name = {self.item_name}")
        print(f"Weight = {self.weight}")
        print(f"Brand = {self.brand}")
        print(f"Status = {self.status}\n")
        return self

print("PRODUCT TRACKER\n")

product1 = Product(10, "coffee", "2 pounds", "Starbucks")
product1.sell().addTax(0.065).displayInfo()

product2 = Product(20, "phone charger", "0.5 pounds", "unknown")
product2.returnItem("defective").displayInfo()

product3 = Product(300, "television", "15 pounds", "Sony")
product3.sell().addTax(0.065).displayInfo()

product4 = Product(1000, "laptop computer", "3 pounds", "Lenovo")
product4.returnItem("opened").displayInfo()

product4 = Product(200, "boots", "3 pounds", "Timberland")
product4.returnItem("like_new").displayInfo()


# Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# Practice altering an instance's attributes
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product Class:
# Attributes:

# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"
# Methods:

# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# Return Item: takes reason_for_return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been opened, set the status to "used" and apply a 20% discount.  (use "defective", "like_new", or "opened" as three possible value for reason_for_return).
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.