class Item:
    disc=0.9
    def __init__(self,name,price):
        self.name=name
        self.price=price
    @classmethod
    def change_disc(cls,new_disc):
        cls.disc=new_disc
    @staticmethod
    def is_costly(price):
        return price>500
    
item1=Item("Phone",400)
item2=Item("Laptop",1000)
print(Item.disc)
Item.change_disc(0.8)
print(Item.disc)
print(Item.is_costly(item1.price))
print(Item.is_costly(item2.price))