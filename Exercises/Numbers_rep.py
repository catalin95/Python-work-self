#!/usr/bin/python3

class Positional(object):

    def __init__(self):
        return 

    def power_of_2(self, power):
        if power == 0:
            return 1
        
        new_number = 1
        base = 2
        for i in range(power):
            new_number *= base

        return new_number

    def power_of_16(self, power):
        if power == 0:
            return 1

        new_number = 1
        base = 16
        for i in range(power):
            new_number *= base

        return new_number

    def binary_rep(self, number):
        a = ""
        b = ""
        for i in range(number):
           a += str(number % 2)
           number = int(number / 2)
           if (number == 0):
               break

        c = len(a) - 1
        while c != -1:
            b += a[c]
            c -= 1

        return b

    def decimal_rep(self, number):
        last = len(number) - 1
        new_number = 0
        index = 0
        while last != -1:
            new_number += int(number[last]) * self.power_of_2(index)
            index += 1
            last -= 1

        return new_number

    def hexadecimal_rep(self, number):
        result = 0
        remainder = ""
        new_number = ""
        for i in range(number):
            result += number % 16
            if result == 10:
                remainder += "A"
                result = 0
            elif result == 11:
                remainder += "B"
                result = 0
            elif result == 12:
                remainder += "C"
                result = 0
            elif result == 13:
                remainder += "D"
                result = 0
            elif result == 14:
                remainder += "E"
                result = 0
            elif result == 15:
                remainder += "F"
                result = 0
            else:
                remainder += str(result)
                result = 0

            number = int(number / 16)
            if number == 0:
                break

        last = len(remainder) - 1
        while last != -1:
            new_number += remainder[last]
            last -= 1

        return new_number
