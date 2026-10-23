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
