# create set
colors={"red","blue","green"}
print(colors)

# create set from list
nums=set([2,4,6,8])
print(nums)

# create set from string
letters=set("programming")
print(letters)

# empty set
empty=set()
print(type(empty))

# add elements
items=set()
items.add(10)
items.add("hello")
items.add(True)
print(items)

# duplicate values are ignored
items.add(10)
print(items)

# remove()
fruits={"mango","grape","orange"}
fruits.remove("grape")
print(fruits)

# discard()
fruits.discard("orange")
fruits.discard("apple")
print(fruits)

# clear()
temp={1,2,3}
temp.clear()
print(temp)

# pop() removes one random item
values={5,10,15,20}
removed=values.pop()
print(removed)
print(values)

# check item exists
animals={"cat","dog","rabbit"}
if "dog" in animals:
    print("yes")

# loop through set
for animal in animals:
    print(animal)

# union
set1={1,3,5}
set2={2,4,6}
result=set1.union(set2)
print(result)

# intersection
set1={1,2,3,4}
set2={3,4,5,6}
result=set1.intersection(set2)
print(result)

# difference
a={1,2,3,4,5}
b={4,5,6,7}
print(a.difference(b))
print(b.difference(a))

# symmetric difference
print(a.symmetric_difference(b))

# update()
a={1,2,3}
b={3,4,5}
a.update(b)
print(a)

# intersection_update()
a={1,2,3,4}
b={3,4,5}
a.intersection_update(b)
print(a)

# difference_update()
a={1,2,3,4}
b={3,4,5}
a.difference_update(b)
print(a)

# symmetric_difference_update()
a={1,2,3,4}
b={3,4,5}
a.symmetric_difference_update(b)
print(a)

# copy by reference
original={10,20,30}
copy_ref=original
copy_ref.add(40)
print(copy_ref)
print(original)

# real copy
original={10,20,30}
copy_set=original.copy()
copy_set.add(40)
print(copy_set)
print(original)

# subset
small={1,2}
large={1,2,3,4}
print(small.issubset(large))

# superset
print(large.issuperset(small))

# disjoint
x={1,2,3}
y={7,8,9}
print(x.isdisjoint(y))

# frozenset = immutable set
fixed=frozenset([2,4,6,8])
print(fixed)

# set operations also work with frozenset
odd=frozenset({1,3,5})
even=frozenset({2,4,6})

print(odd.union(even))
print(odd.intersection(even))
print(odd.difference(even))