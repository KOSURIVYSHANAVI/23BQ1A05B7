class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price = self.price - (self.price * percent / 100)

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Price:", int(self.price))


p = Product(1, "Laptop", 50000)

p.apply_discount(10)
p.display()