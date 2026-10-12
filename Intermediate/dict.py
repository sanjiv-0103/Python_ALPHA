# create dictionary
student={"name":"Arun","age":20,"city":"Chennai"}
print(student)

# create using dict()
employee=dict(name="Meera",age=24,city="Madurai")
print(employee)

# access value using key
print(student["name"])

# add new key
student["email"]="arun@gmail.com"
print(student)

# change existing value
student["city"]="Coimbatore"
print(student)

# delete key
del student["email"]
print(student)

# pop() removes key and returns value
age=student.pop("age")
print(age)
print(student)

# popitem() removes last inserted item
student={"name":"Arun","age":20,"city":"Chennai"}
item=student.popitem()
print(item)
print(student)

# check key exists
student={"name":"Arun","age":20,"city":"Chennai"}
if "name" in student:
    print(student["name"])

# try except for missing key
try:
    print(student["phone"])
except KeyError:
    print("key not found")

# loop through dictionary
for key in student:
    print(key,student[key])

# loop through keys
for key in student.keys():
    print(key)

# loop through values
for value in student.values():
    print(value)

# loop through key and value
for key,value in student.items():
    print(key,value)

# copy by reference
original={"name":"Kavin","age":22}
copy_ref=original
copy_ref["name"]="Ravi"
print(copy_ref)
print(original)

# real copy
original={"name":"Kavin","age":22}
copy_dict=original.copy()
copy_dict["name"]="Ravi"
print(copy_dict)
print(original)

# merge dict
person1={"name":"Nila","age":21}
person2={"city":"Salem","course":"CSE"}
person1.update(person2)
print(person1)

# number as key
marks={1:75,2:82,3:90}
print(marks[1])
print(marks[2])

# tuple as key
point=(10,20)
location={point:"classroom"}
print(location[point])

# nested dict
student1={"name":"Ajay","age":20}
student2={"name":"Divya","age":21}

students={
    "student1":student1,
    "student2":student2
}

print(students)
print(students["student1"]["name"])