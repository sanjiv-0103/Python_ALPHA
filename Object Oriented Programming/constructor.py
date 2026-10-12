class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total(self):
        return self.price*self.quantity
item1=Item("Phone",100,5)
print(item1.name)
print(item1.price())
item2=Item("Laptop",1000,2)
print(item2.name) #constructor is used to init the obj with values
print(item2.total())