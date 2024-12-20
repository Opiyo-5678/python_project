from variables import number

number = 67 # interger
second = 34.43# float
greetings="hello"#string
ispythoninteresting= True #boolean

print(number)
print(second)
print(greetings)
print(ispythoninteresting)

#data structures multiple values stored in a single variable

cars =["TX", "V8","BMW"] #list-  ordered and changeable
fruits = ("mango","apple","banana")#tuple-ordered but unchangeable
countries = {"kenya","algeria","uganda"}#set-unordered and unchangeable
student = {
    "firstname" :"chess",
    "age" : 25,
    "course" : "web development",
    "gender" : "female"
}#dictionary-key-value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["gender"])

#determing datatypes
print(type(countries))
#typecasting-converting form one datatypes to another
print(float(number))
print(int(second))