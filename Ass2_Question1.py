#R246282H
#Assignment 2

class Vehicle:
    def description(self):
        print("The vehicles have been revealed")

class Car(Vehicle):
    def description(self):
        print("The first vehicle is a Car!!")

class Bike(Vehicle):
    def description(self):
        print("The second vehicle is a Bike!!")

v = Vehicle()
c = Car()
b = Bike()

v.description()
c.description()
b.description()