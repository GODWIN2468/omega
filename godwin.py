import random
import time
import random
print("Avaitor predictor app")
print("Welcome to the crash game")
print("CASH OUT BEFORE THE GAME CRASHES 🤑🤑🤑🤑")

#user interface
multiplier = 1.00
Crash_point = random.uniform(1.00, 100.00)
Crash_point_3sf = float(f"{Crash_point :.3g}")
print("Crash_point (3sf):", Crash_point_3sf)

#User input to cash out
bet = float(input("enter your bet amount:(¢)"))
