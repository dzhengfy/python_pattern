#! /usr/bin/python

class SubSystemA_Light(object):
    def turn_on(self):
        print("Turn light on")
    def turn_off(self):
        print ("Turn light off")

class SubSystemB_Television(object):
    def turn_on(self):
        print("Turn TV on")
    def turn_off(self):
        print ("Turn TV off")

class SubSystemC_Aircondition(object):
    def turn_on(self):
        print("Turn aircondition on")
    def turn_off(self):
        print ("Turn aircondition off")

class Facade(object):
    def __init__(self, light, tv, aircondition):
        self._light = light
        self._tv = tv
        self._aircondition = aircondition
    def turn_on_all(self):
        print("I get up ...")
        self._light.turn_on()
        self._tv.turn_on()
        self._aircondition.turn_on()
    def turn_off_all(self):
        """
        Please input necessary codes
        """
        print("I go to bed ...")


if __name__ == '__main__':
    """
    Please use Facade pattern to complete the codes.
    Below outputs are expected:
    I get up ...
    Turn light on
    Turn TV on
    Turn aircondition on
    I go to bed ...
    Turn light off
    Turn TV off
    Turn aircondition off
    """
