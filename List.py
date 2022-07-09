course = ["Language","Data Structure","Algorithm","CN","OS","Data Com"]

print(course)
print(course[0]) #index wise print
print(course[2:]) #all the value after 2nd index
print(course[-1]) #last index

print("Data Com" in course) # return ture if exist
print("Data Com" not in course) # return ture if not exist


print(course + ["TOC"]) #print list adding new value

print(course)

print("Length : ",len(course)) #return the length of list
course.append("Micro") #it uses for adding new value in list
print(course)

course.insert(3,"Database") #for inserting new value index should be mentioned
print(course)

course.remove("OS") # removing value
print(course)

course.sort()
print(course) #sorting as like dictionary

course.reverse()
print(course) #sort in reverse order

course.pop() #popig value form the last index
print(course)

courseN = course.copy() #copy to the another list
course.clear() #all the value will be cleared
print(course)
print(courseN)

print(courseN.index("Database")) #return the position of value
print(courseN.count("Database")) #how much time it exists
