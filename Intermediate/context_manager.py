# basic file handling with with
with open("sample.txt","w") as file:
    file.write("Hello Python")
# file closes automatically after with block
# read file
with open("sample.txt","r") as file:
    data=file.read()
print(data)
# write multiple lines
with open("notes.txt","w") as file:
    file.write("line 1\n")
    file.write("line 2")
# append to file
with open("notes.txt","a") as file:
    file.write("\nline 3")
# read appended file
with open("notes.txt","r") as file:
    print(file.read())
# custom context manager using class
class MyContext:
    def __enter__(self):
        print("start")
        return self
    def __exit__(self,type,value,traceback):
        print("end")
with MyContext():
    print("inside context")