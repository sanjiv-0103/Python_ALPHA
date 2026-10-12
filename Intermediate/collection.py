from collections import namedtuple,OrderedDict,Counter,defaultdict,deque
# namedtuple
Person=namedtuple("Person",["name","age"])
p=Person("Arun",21)
print(p.name)
print(p.age)

# OrderedDict
student=OrderedDict()
student["name"]="Meera"
student["age"]=22
student["city"]="Chennai"
print(student)

# Counter
items=["apple","banana","apple","orange","apple"]
count=Counter(items)
print(count)
print(count["apple"])

# defaultdict
marks=defaultdict(int)
marks["math"]=80
marks["science"]=90
print(marks["math"])
print(marks["english"])

# deque 
q=deque([1,2,3])
q.append(4)
q.appendleft(0)
print(q)

q.pop()
q.popleft()
print(q)