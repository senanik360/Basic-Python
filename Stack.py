''' Stack follow LIFO'''

course =["Language", "Data Structure","Algorithm"]

print(course)

course.append("TOC")
print(course)

course.pop()
print(course)

print(course[-1]) #print the last value

course.pop()
print(course[-1]) #print the last value

if not course:
    print("No value exits")
course.pop()
course.pop()

if not course:
    print("No value exits")
