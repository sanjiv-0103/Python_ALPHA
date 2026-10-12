from itertools import count,cycle,repeat,product,permutations,combinations,accumulate
# count() keeps counting from a start value
for i in count(1):
    print(i)
    if i==5:
        break

# cycle()=repeats values again and again
colors=["red","blue"]
c=cycle(colors)

for i in range(4):
    print(next(c))

# repeat()=repeats the same value
for x in repeat("hello",3):
    print(x)

# product()=all possible pairs
a=[1,2]
b=["A","B"]
print(list(product(a,b)))

# permutations()=all possible orders
nums=[1,2,3]
print(list(permutations(nums,2)))

# combinations()=unique grps without changing order
nums=[1,2,3]
print(list(combinations(nums,2)))

# accumulate()=running total
nums=[1,2,3,4]
print(list(accumulate(nums)))