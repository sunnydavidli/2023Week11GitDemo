# let's define a user Class

class User:
    # initializer 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # display info
    # class method
    def displayInfo(self):
        print(self.name, self.age)

u1 = User("David", 45)
u1.displayInfo()

class Test:
    pass 


