#built in fi=unctions
from audioop import minmax

y = max(34,56, 18,100)
print(y)
y = min(34,56, 18,100)
print(y)

z = pow(2, 3)
print("the result is ",z)

#user-defined functions

def greeting():
    print("hello there!")
greeting() #calling a function

def multiply():
    a = 12
    b = 10
    print (a * b)
multiply()


#parameters/variable and argument/value stored in variable

def add(x,y):

    print(x + y)
add(5,67)
add(400, 67)

def employee (fullname,age,position,status):
    print(fullname,age,position,status)
employee("opiyo",24,"manager","married")
employee("odono",34,"secretary","married")
employee("opii",35,"clerk","married")
employee("chess",56,"hr","single")

yu = min(67,8,3,78)
print(yu)