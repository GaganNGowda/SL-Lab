class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("gagan", 20)
p2 = person("ashish", 12)

print("\n name of person is", p1.name)
print("\n age of person is", p1.age)

print("\n name of person is", p2.name)
print("\n age of person is", p2.age)

p2.age = 10

print("\n p2 age is", p2.age)
