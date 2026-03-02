import os
a = float(input("Enter first number"))
b = float(input("Enter a second number"))

op = input("choose + , _, *, / : ")


if op == "+":
   print (a + b)
elif op == "-":
   print(a - b)
elif op == "*":
   print(a * b)
elif op == "/":
   print(a / b)
else:
   print("Invalid operator")
