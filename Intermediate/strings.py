# create string
text="Welcome"
print(text)

# single and double quotes
msg1='Hello'
msg2="Python"
print(msg1)
print(msg2)

# quotes inside string
quote="Hello"
print(quote)

# escape characters
line="He said \"Good job\""
print(line)

# multiline string
multi="""Python
is
easy"""
print(multi)

# access character
word="Programming"
print(word[0])
print(word[-1])

# slicing
print(word[0:4])
print(word[:6])
print(word[6:])
print(word[::2])
print(word[::-1])

# concatenate strings
first="Good"
second="Morning"
result=first+" "+second
print(result)

# loop through string
name="Arun"
for ch in name:
    print(ch)

# check character exists
if "r" in name:
    print("yes")

# check substring exists
if "run" in name:
    print("yes")

# strip() removes extra spaces
text="   Hello Python   "
print(text.strip())

# len()
print(len("Python"))

# upper() and lower()
text="Python Basics"
print(text.upper())
print(text.lower())

# startswith() and endswith()
print("programming".startswith("pro"))
print("programming".endswith("ing"))

# find()
print("welcome".find("c"))

# count()
print("banana".count("a"))

# replace()
sentence="I like Java"
new_sentence=sentence.replace("Java","Python")
print(new_sentence)

# split()
sentence="learn python step by step"
words=sentence.split()
print(words)

# split using comma
data="red,blue,green"
colors=data.split(",")
print(colors)

# join()
words=["Python","is","simple"]
sentence=" ".join(words)
print(sentence)

# format()
name="Kavin"
age=22
message="My name is {} and I am {} years old".format(name,age)
print(message)

# format with positions
message="Hello {0},welcome to {1}".format("Sanjiv","Python")
print(message)

# number formatting
price=45.6789
print("Price is {:.2f}".format(price))

# old style formatting
name="Divya"
score=88
print("Name: %s Score: %d"%(name,score))

# f-string
name="Ajay"
age=20
print(f"My name is {name} and I am {age}")

# f-string with calculation
a=5
b=4
print(f"Total is {a+b}")
