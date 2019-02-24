#! /usr/bin/python

class Animal(object):
    def eat(self, food):
        raise NotImplementedError()

class Dog(Animal):
    def eat(self, food):
        print('Dog eats {}'.format(food))

class Cat(Animal):
    def eat(self, food):
        print('Cat eats {}'.format(food))

class AnimalFactory(object):
    def create_animal(self):
        raise NotImplementedError()

class DogFactory(AnimalFactory):
    """
    Please input necessary codes
    """

class CatFactory(AnimalFactory):
    """
    Please input necessary codes
    """

if __name__ == '__main__':
    """
    Please use factory method pattern to complete the codes.
    Output expected is:
    Dog eats bones
    Cat eats fishes
    """
