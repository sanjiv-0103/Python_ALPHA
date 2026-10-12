# 1. CREATE A LIST
fruits=["banana","cherry","apple"]
print(fruits)

# 2. DIFFERENT DATA TYPES IN A LIST
mixed= [5,True,"apple",3.5]
print(mixed)

# 3. DUPLICATE VALUES
numbers = [1, 1, 2, 2, 3]
print(numbers)

# 4. ACCESS ELEMENTS
fruits = ["banana","cherry","apple"]
print(fruits[0])    # first 
print(fruits[-1])  # last

# 5. CHANGE AN ITEM
fruits[2] = "lemon"
print(fruits)

# 6. LENGTH OF LIST
print(len(fruits))

# 7. APPEND
fruits.append("orange")
print(fruits)

# 8. INSERT
fruits.insert(1, "blueberry")
print(fruits)

# 9. POP
removed_item = fruits.pop()
print("Removed:", removed_item)
print(fruits)

# 10. REMOVE
fruits.remove("cherry")
print(fruits)

# 11. CLEAR
temp = [1, 2, 3]
temp.clear()
print(temp)

# 12. REVERSE
fruits = ["banana", "cherry", "apple"]
fruits.reverse()
print(fruits)

# 13. SORT
fruits.sort()
print(fruits)

# 14. SORTED
fruits = ["banana", "cherry", "apple"]
new_fruits=sorted(fruits)
print("Original:",fruits)
print("Sorted:",new_fruits)

# 15. REPEATED ELEMENTS
zeros = [0] * 5
print(zeros)

# 16. CONCATENATION
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)

# 17. CONVERT STRING TO LIST
text = "Hello"
letters = list(text)
print(letters)

# 18. COPY BY REFERENCE
original = ["banana", "apple"]
copy_ref = original
copy_ref.append("orange")
print("Copy:", copy_ref)
print("Original:", original)

# 19. REAL COPY
original = ["banana", "apple"]
copy_list = original.copy()
copy_list.append("orange")
print("Copy:", copy_list)
print("Original:", original)

# 20. FOR LOOP
fruits = ["banana", "cherry", "lemon"]
for fruit in fruits:
    print(fruit)

# 21. CHECK ITEM EXISTS
if "banana" in fruits:
    print("Yes")
else:
    print("No")

# 22. SLICING
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[1:3])
print(numbers[2:])
print(numbers[:3])
print(numbers[::2])
print(numbers[::-1])

# 23. COPY USING SLICING
numbers_copy = numbers[:]
print(numbers_copy)

# 24. LIST COMPREHENSION
numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]
print(squares)

# 25. NESTED LISTS
matrix = [[1, 2],[3, 4]]
print(matrix)
print(matrix[0])
print(matrix[0][1])