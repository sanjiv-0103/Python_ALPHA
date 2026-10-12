# zero division error
try:
    print(10/0)
except ZeroDivisionError:
    print("cannot divide by zero")
# value error
try:
    num=int("abc")
except ValueError:
    print("invalid number")
# index error
nums=[1,2,3]
try:
    print(nums[5])
except IndexError:
    print("index not found")
# key error
student={"name":"Arun"}
try:
    print(student["age"])
except KeyError:
    print("key not found")
# type error
try:
    print("age"+20)
except TypeError:
    print("different data types cannot be added")
# try except else
try:
    num=int("10")
except ValueError:
    print("error")
else:
    print("valid number:",num)
# finally = always runs
try:
    print(10/2)
except ZeroDivisionError:
    print("error")
finally:
    print("program finished")
# raise exception manually
age=15
try:
    if age<18:
        raise ValueError("age must be 18 or above")
except ValueError as e:
    print(e)
# custom exception
class AgeError(Exception):
    pass
age=16
try:
    if age<18:
        raise AgeError("not eligible")
except AgeError as e:
    print(e)