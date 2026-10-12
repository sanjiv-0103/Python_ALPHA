class Person:
    def __init__(self,name,age):
        self.name=name
        self._age=age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
        if new_age>=0:
            self._age=new_age
        else:
            print("invalid age")
p1=Person("Arun",21)
# getter
print(p1.age)
# setter
p1.age=25
print(p1.age)