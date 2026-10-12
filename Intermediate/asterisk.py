# multiplication
print(5*3)

# repeat string
print("Hi"*3)

# repeat list
nums=[1,2]
print(nums*3)

# unpack list
values=[10,20,30]
print(*values)

# multiple positional arguments
def add(*nums):
    total=0
    for n in nums:
        total+=n
    print(total)
add(1,2,3,4)

# unpack list into func
def show(a,b,c):
    print(a,b,c)
values=[5,10,15]
show(*values)

# collect remaining values
nums=[1,2,3,4,5]
first,*middle,last=nums
print(first)
print(middle)
print(last)
print(2**3)

# multiple keyword arguments
def details(**data):
    print(data)
details(name="Arun",age=21)