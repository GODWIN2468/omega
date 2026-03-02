# class Car:
#     def __init__(self , colour, type_of_car, mode):
#         self.colour = colour
#         self.type_of_car = type_of_car
#         self.mode = mode

#     def display(self):
#         print("colour:", self.colour)
#         print("type of car:", self.type_of_car)
#         print("mode:", self.mode)
        
# Car1 = Car("red", "rollsroyce", "automatic")
# Car2 = Car("blue", "toyota", "manual")
# Car1.display()

  


# class Fruit:
#     def __init__(self, fruit, colour, size):
#         self.fruit = fruit
#         self.colour = colour
#         self.size = size

#     def display(self):
#         print("fruit:", self.fruit)
#         print("Colour:", self.colour)
#         print("Size:", self.size)
        
# Fruit1 = Fruit("apple", "red", "small")
# Fruit2 = Fruit("banana", "yellow", "medium")
# Fruit1.display()
# Fruit2.display()
           



class Car():
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color

    def sound(self):
        if(self.brand == "Volvo"):
            print("piiiiiiii")
        if(self.brand == "Corolla"):
            print("pooooo")

    def speed(self):
        print("Speeeediiiiiiiiiiiiiiig")



first_car = Car("Volvo", "Mod 1", "red")
second_car = Car("Corolla", "mod 2", "yellow")
first_car.sound()
second_car.sound()

class Bus(Car):
    def __init__(self,seats):
/