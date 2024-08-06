class Bread:
    def __init__(self, name, price):
        # way to create an attribute
        self.name = name
        self.price = price
        self.amount = 0

    def set_amount(self, num):
        self.amount = num

bread_1 = Bread("Ciabatta", "$56")
bread_2 = Bread("Gluten-free", "$21")
bread_1.set_amount(233)
print(bread_1.amount)