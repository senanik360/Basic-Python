course = {
     "101": "Language",
     "102": "Data Structure",
     "103": "Algorithm"
           }

print(course.get("101"))
print(course.get("108"))
print(course.get("108","Not a valid key")) #print not a valid key instead of none
