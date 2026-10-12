import json
# python dictionary
student={"name":"Arun","age":21,"city":"Chennai","active":True}
print(student)

# dumps() = python object to json string
student_json=json.dumps(student)
print(student_json)

# pretty json using indent
pretty_json=json.dumps(student,indent=4)
print(pretty_json)

# dump() = save py object into json file
with open("student.json","w") as file:
    json.dump(student,file,indent=4)

# loads() = json string to python dictionary
data='{"name":"Meera","age":22,"city":"Madurai"}'
person=json.loads(data)
print(person)
print(person["name"])

# load() = read json file into python object
with open("student.json","r") as file:
    saved_data=json.load(file)

print(saved_data)

# json with list
course={
    "name":"Python",
    "topics":["list","tuple","dict"]
}
print(json.dumps(course,indent=4))

# json with nested dictionary
employee={
    "name":"Kavin",
    "details":{
        "age":24,
        "city":"Salem"
    }
}
print(json.dumps(employee,indent=4))

# python to json value conversion
values={
        "text":"hello",
        "number":10,
        "decimal":5.5,
        "active":True,
        "empty":None
}
print(json.dumps(values,indent=4))

# custom object
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=Person("Divya",23)

# convert object to dictionary then json
person_json=json.dumps(p.__dict__,indent=4)
print(person_json)