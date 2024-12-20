from strings import course

courses = ["MIT","DATASCIENCE","CYBERSECURITY"]
print(courses)
print(courses[1])
for y in courses:
    print("course is", y)


#adding a new element
courses.append("web development")
print(courses )
#deleting an element

courses.remove("MIT")
print(courses)