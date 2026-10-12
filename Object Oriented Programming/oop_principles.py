#encapsulation
class Account:
    def __init__(self,balance):
        self._balance=balance
    def show_balance(self):
        print(self._balance)
#inheritance
class Savings(Account):
    def add_interest(self):
        self._balance=self._balance+100
#abstraction
class Vehicle:
    def start(self):
        print("vehicle started")
#polymorphism
class Car(Vehicle):
    def start(self):
        print("car started")
class Bike(Vehicle):
    def start(self):
        print("bike started")

account=Savings(1000)
account.show_balance()
account.add_interest()
account.show_balance()
car=Car()
bike=Bike()
car.start()
bike.start()