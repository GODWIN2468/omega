
#"""A simple CLI tool that prints the current date and time."""
import datetime
from datetime import datetime
x = datetime.now()
print(x)

x = datetime(2026, 3, 6)
print(x.strftime("%Y"))
print(x.strftime("%B"))
print(x.strftime("%d"))
print("current date is", x.strftime("%Y-%m-%d"))
#time
from datetime import datetime
now= datetime.now()
times = now.strftime("%H: %M: %S")
print("current time is", times)




