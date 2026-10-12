class Item: #class declaration
    def total_price(self):
        return self.price*self.quantity
item1=Item() #1st object
item1.name="Phone"
item1.price=100
item1.quantity=5
print(item1.name)
print(item1.total_price())
item2=Item() #2nd object
item2.name="Laptop"
item2.price=1000
item2.quantity=2
print(item2.name)
print(item2.total_price())