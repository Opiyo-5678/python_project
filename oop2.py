class person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def movement(self):
        print("person is walking")

person1 = person("evans","male",35)
print(person1.name,person1.gender,person1.age)
person2 = person("faith","female",15)
person3 = person("cladys","female",25)