class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("gagan", 20)


print("\n name of person is", p1.name)
print("\n age of person is", p1.age)

print("\n printing after deleting age attribute for p1")
del p1.age

print("\n name of perd=son 1 is",p1.age)
print("\nprinting after deleting p1")

print("\n name of perdson 1 is", p1.name)




