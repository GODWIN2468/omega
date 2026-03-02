import math


def greet(name):
    name = "GODWIN"
    print(f'hello Goodmorning {name}')


greet("name")


def Area_rectangle(length, width):
    area = length * width
    return area


print(Area_rectangle(5, 3))
print(Area_rectangle(8, 43))
print(Area_rectangle(342, 9))


def is_even():
    num = int(input("enter a number"))
    result = num/2
    if result == (int(result)):
        print("True")
    else:
        print("False")


is_even()


def sum(X, Y):
    Z = X + Y
    return Z


print(sum(22, 44))
print(sum(63, 95))


A = "Godwin"
reversed_A = A[:: -1]
print(reversed_A)

# max value


def max_three(a, b, c):
    return max(a, b, c)


print(max_three(4, 9, 2))



def celcius_to_fahrenheit():
    c = 35
    F = (c * 9/5) + 32
    print(F)

celcius_to_fahrenheit()

#factorial of a number
def factorial():
    print(math.factorial(5))
    print(math.factorial(7))
    print(math. factorial(38)) 

factorial()   
                     





# sum numbers
def sum_list(num):
        return sum(num)
        print(sum_list([1, 2, 3, 4]))

def is_vowel():
            lett = input("enter a letter: ")
            if   lett in "aeiou":
                print("It is a vowel")
            else:
                print("It is NOT a vowel")











