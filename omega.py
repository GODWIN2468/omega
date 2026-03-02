def variableName():
    print("hello world")
    print("hello godwin")
    print( 1 + 3)


variableName()

def substract():
    x = 6
    y = 5
    z = x - y
    print(z)

substract()



def age():
    person_age = 18
    if(person_age == 18):
        print("You are qualified")
    else:
        print("you are not qualified")
    print
age()     



def hello():
    print("Hello world")

hello()

def guessnumber():
    print(10)

guessnumber()


def sum():
    print(3 + 7)

sum()


def current_year():
    print(2026)

current_year()

def check_weather():
    weather ="rainy"

    if weather == "rainy":
     print("Take an umbrella")
    else:
        print("The is Good")

check_weather()


# functions with parameter

def add(x,y):
    z = x + y
    return z

print(add(3,98))
print(add(5,8))
print(add(2,9))


def sayMyName(name):
    print(f"Hello {name}")

sayMyName("George")