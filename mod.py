import platform
import datetime
import os

x = datetime.datetime.now()
print(x)
print(x . year)
print(x . strftime("%A"))
print(platform.system())

y = datetime.datetime(2020 , 5 , 17)
print(y)

z = datetime . datetime(2018, 6, 1)

print(z.strftime("%B"))




# with open("godwin.txt", 'w') as f:
#     f.write("I was just added")

# with open("godwin.txt", 'r') as f:
#     print(f.read())

# os.remove("godwin.txt")



try:
    print(student)
except:
    print("An error occured")
else:
    print("No error occured")
finally:
    print("This will always execute")