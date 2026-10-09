# user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = [75, 82, 68, 90, 55]
is_student = True
print("Name:",name)
print("Age:",age)
print("Student:", is_student)
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
print("Marks:")
for mark in marks:
    # continue skips this value
    if mark==68:
        continue
    # break stops the loop
    if mark<60:
        print("Low mark found")
        break
    print(mark)
total = 0
for mark in marks:
    total = total + mark
average = total/len(marks)
print("Total:",total)
print("Average:",average)

# dictionary
student = {
    "name": name,
    "age": age,
    "average": average
}
print("Student details:",student)
numbers = {1,2,2,3,4}
print("Set:",numbers)
def check_result(avg):
    if avg >= 60:
        return "Pass"
    else:
        return "Fail"
print("Result:",check_result(average))