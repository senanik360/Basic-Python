'''Queue follow FIFO'''
from collections import  deque
course =deque(["Language", "Data Structure","Algorithm"])

course.popleft()
print(course)

course.popleft()
print(course)


course.popleft()
print(course)

if not course :
    print("No value exists")
