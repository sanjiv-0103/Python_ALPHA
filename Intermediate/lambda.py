# simple lambda
add=lambda a,b:a+b
print(add(2,3))

# square number
square=lambda x:x*x
print(square(5))

# check even number
is_even=lambda x:x%2==0
print(is_even(4))

# map()
nums=[1,2,3,4]
double=list(map(lambda x:x*2,nums))
print(double)

# filter()
even=list(filter(lambda x:x%2==0,nums))
print(even)

# sorted()
students=[("Arun",80),("Meera",95),("Kavin",75)]
students.sort(key=lambda x:x[1])
print(students)