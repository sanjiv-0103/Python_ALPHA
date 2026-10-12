def numbers():
    yield 1
    yield 2
    yield 3
g=numbers()
print(next(g))
print(next(g))
print(next(g))

# loop
def count_up():
    for i in range(1,4):
        yield i

for num in count_up():
    print(num)

# generator keeps its state
def steps():
    print("start")
    yield 10
    print("middle")
    yield 20
    print("end")
g=steps()
print(next(g))
print(next(g))

# expression
nums=(x*x for x in range(1,5))
for num in nums:
    print(num)

# list vs generator
list_nums=[x*x for x in range(1,5)]
gen_nums=(x*x for x in range(1,5))
print(list_nums)
print(gen_nums)

# example
def one_value():
    yield 5
g=one_value()
print(next(g))
try:
    print(next(g))
except StopIteration:
    print("generator finished")

# even numbers
def even_nums(limit):
    for i in range(limit):
        if i%2==0:
            yield i
for num in even_nums(10):
    print(num)