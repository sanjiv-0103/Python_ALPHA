class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def show_item(self):
        print(self.name,self.price)
class Phone(Item):
    def call(self):
        print("calling")
phone1=Phone("iPhone",800)
phone1.show_item()
phone1.call()
#child gets properties and methods from parent.