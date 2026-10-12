def add(a,b):
    print(a+b)
add(2,3)

# positional arguments
def show(name,age):
    print(name,age)
show("Arun",21)

# keyword arguments
show(age=22,name="Meera")

# default argument
def greet(name="Guest"):
    print("Hello",name)
greet()
greet("Kavin")

# *args = multiple positional arguments
def total(*nums):
    sum=0
    for n in nums:
        sum+=n
    print(sum)
total(1,2,3,4)

# multiple keyword arguments
def details(**data):
    for key in data:
        print(key,data[key])
details(name="Divya",age=20,city="Chennai")

# return value
def multiply(a,b):
    return a*b
result=multiply(4,5)
print(result)