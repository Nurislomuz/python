#Task: Electricity Bill Calculator
#Write a Python program using Object-Oriented Programming (OOP) to calculate a customer's 
#electricity bill based on the number of units consumed.

#Your program should:
#Create a class named Customer.
#Include a method get_info() to accept the customer's name, ID, 
# and the number of consumed units via user input.
#Include a method calculate_bill() to compute the total bill based on specific pricing tiers 
# (e.g., rate for the first 100 units, rate for units above 100, and rate for units above 200).
#Include a method display_bill() to print the customer's name, ID, total consumed units, 
# and the final calculated bill amount formatted with a dollar sign.

class Customer:
    def get_info(self):
        self.customer_name = input('Enter customer name: ').strip()
        self.customer_id = int(input('Enter your customer id: ').strip())
        self.units = int(input('Enter Number of Units Consumed: ').strip())
    def calculate_bill(self):
        self.aunits = self.units
        self.bbalance= 0
        if 0 < self.units <= 100:
            self.bbalance = self.units * 2
        elif self.units > 100:
            self.bbalance = + ((self.units - 100) * 3)
        elif self.units > 200:
            self.bbalance = + ((self.units - 200) * 5)
    def display_bill(self):
        print('='*8)
        print(f'Customer name: {self.customer_name}')
        print(f'Customer ID: {self.customer_id}')
        print(f'Consumer Units: {self.aunits}')
        print(f'Total bill: {self.bbalance}$')

s = Customer()
s.get_info()
s.calculate_bill()
s.display_bill()
