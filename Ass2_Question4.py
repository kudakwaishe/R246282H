#R246282H
#Assignment 2
#Question 4


class Dog:
    def make_sound(self):
        return "Woof! Woof!"

class Cat:
    def make_sound(self):
        return "Meow! Meow!"

def process_sound(sound_object):
    print(sound_object.make_sound())

dog = Dog()
cat = Cat()

process_sound(dog)
process_sound(cat)
