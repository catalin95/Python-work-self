#!/usr/bin/python3

class Math(object):

    def __init__(self):
        return

    def logarithm(self, base, number):
        if (number < 0):
            print("Please provide only positive numbers!")
            return

        initial = 1
        counter = 0
        while initial != number:
            initial *= base
            if (initial > number):
                print("Not implemented behaviour, please give a valid base and number!")
                return
            else:
                counter += 1

        return counter

    def exponent(self, number, power):
        base = number
        if power == 0:
            return 1
        else:
            for i in range(power - 1):
                number *= base

        return number


        
