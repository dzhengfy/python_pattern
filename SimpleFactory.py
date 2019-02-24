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
    @staticmethod
    def create_animal(name):
    """
    Please input necessary codes
    """

if __name__ == '__main__':
    """
    Please use simple factory pattern to complete the codes.
    Output expected is:
    Dog eats bones
    Cat eats fishes
    """

