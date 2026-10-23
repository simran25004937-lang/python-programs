Aim
To write a Python program to demonstrate object-oriented programming concepts using a class and object.

Algorithm
1. Start the program.
2. Create a class named Game.
3. Define a method to display game details.
4. Create an object and call the method.
5. Stop the program.

Code:
class Game:
    def display(self):
        print("Game Name: Minecraft")
        print("Genre: Adventure")
        print("Platform: PC")

g = Game()
g.display()

Output:
Game Name: Minecraft
Genre: Adventure
Platform: PC

 Result:
 Thus, the Python program demonstrates object-oriented programming concepts using a class, object, and method.




Aim: To demonstrate overloading and overriding in python.
Algorithm:
Start.
Define a class Vehicle with a method start() that displays "Vehicle is starting".
Define a class Car that inherits from Vehicle.
Override the start() method in Car to display "Car starts with a key".
Define a class Bike that inherits from Vehicle.
Override the start() method in Bike.
Call super().start() to display "Vehicle is starting".
Display "Bike starts with a button".
Create objects of Vehicle, Car, and Bike.
Call the start() method using each object.
Display the corresponding messages.
Stop.

Code:
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = Calculator()

print(obj.add(30,40))
print(obj.add(30,40,50))
print(obj.add(30))



class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        super().start()
        print("Bike starts with a button")

v = Vehicle()
c = Car()
b = Bike()

v.start()
c.start()
b.start()

Output:
70
120
30
Vehicle is starting
Car starts with a key
Vehicle is starting
Bike starts with a button
