# simple decorator
def my_decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper

@my_decorator
def greet():
    print("hello")
greet()

# decorator with function argument
def upper_decorator(func):
    def wrapper():
        text=func()
        return text.upper()
    return wrapper

@upper_decorator
def message():
    return "welcome"
print(message())

# decorator with parameters
def check_age(func):
    def wrapper(age):
        if age>=18:
            func(age)
        else:
            print("not allowed")
    return wrapper

@check_age
def show_age(age):
    print("age:",age)
show_age(20)
show_age(15)

# multiple decorators
def first(func):
    def wrapper():
        print("first")
        func()
    return wrapper
def second(func):
    def wrapper():
        print("second")
        func()
    return wrapper

@first
@second
def test():
    print("main function")
test()