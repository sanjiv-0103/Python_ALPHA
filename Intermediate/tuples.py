# create tuple
person=("Max",28,"New York")
print(person)

# tuple without brackets
person2="Linda",25,"Miami"
print(person2)

# single value tuple needs comma
single=(25,)
print(single)

# convert list to tuple
nums=tuple([1,2,3])
print(nums)

# access elements
print(person[0])
print(person[-1])

# delete tuple
temp=(1,2,3)
del temp

# loop through tuple
for item in person:
    print(item)

# check item exists
if "New York" in person:
    print("yes")
else:
    print("no")

# len()
letters=("a","p","p","l","e")
print(len(letters))

# count()
print(letters.count("p"))

# index()
print(letters.index("l"))

# repeat tuple
repeat=("a","b")*3
print(repeat)

# join tuples
joined=(1,2,3)+(4,5,6)
print(joined)

# list to tuple
my_list=["a","b","c"]
to_tuple=tuple(my_list)
print(to_tuple)

# tuple to list
to_list=list(to_tuple)
print(to_list)

# string to tuple
text_tuple=tuple("Hello")
print(text_tuple)

# slicing
nums=(1,2,3,4,5,6,7,8,9,10)
print(nums[1:3])
print(nums[2:])
print(nums[:3])
print(nums[::2])
print(nums[::-1])

# unpack tuple
person=("Max",28,"New York")
name,age,city=person
print(name)
print(age)
print(city)

# unpack middle values
nums=(0,1,2,3,4,5)
first,*middle,last=nums
print(first)
print(middle)
print(last)

# nested tuple
nested=((0,1),("age","height"))
print(nested)
print(nested[0])

# tuple can be used as dictionary key
location={(10,20):"point a"}
print(location[(10,20)])