class myClass:
    x = 5
    b = 6

    def new_unction():
        print("calling function")

class AnotherClass:
    pass

p1 = myClass
p2 = myClass

del AnotherClass

print(p1.x)
print(p1.b)
p1.new_unction()

class StudentRecord:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greetings(self):
        print("Hello" + self.name)

    def checkAge(self):
        if(self.age > 7):
            print("You are old")
        else:
            print("congratulation")



per1 = StudentRecord("Nana",7)
per1.greetings()
per1.checkAge()