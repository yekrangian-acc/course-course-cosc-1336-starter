import random

class Die:
    def __init__(self):
        self.__roll_value = 0

    def roll(self):
        self.__roll_value = random.randint(1, 6)
        return self.__roll_value

    def get_rolled_value(self):
        return self.__roll_value

    def __str__(self):
        return f"The rolled value is {self.__roll_value}"