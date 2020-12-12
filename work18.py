#! python3
# Simple program, define binary search function, store outputed values for it in a text file and read from it previous computed values

from os import chdir

chdir(r"Path to file")

class Binary(object):

    def __init__(self, iterator):
        self.iterator = iterator

    def create_log(self, element):
        with open("Memo_P.txt", "a") as file:
            file.write(str(element) + ";")

    def read_log(self, element):
        with open("Memo_P.txt", "r") as file:
            string = file.read()
            output_string = ""
            
            for char in string:
                if (char != ";"):
                    output_string += char
                else:
                    if (int(output_string) == element):
                        return element
                    else:
                        output_string = ""


    def binary_search(self, element):
        size = len(self.iterator)
        compare = self.read_log(element)

        if (compare == element):
            print("Found element")
            return True

        if size % 2 == 0:
            middle = int(size / 2)
        else:
            middle = int((size / 2) + 1)

        if size == 0:
            print("Element can't be found")
            return False
        elif (size == 1 or size == 2):
            if (self.iterator[0] == element or self.iterator[1] == element):
                print("Found element")
                self.create_log(element)
                return True
            else:
                print("Element can't be found")
                return False
        else:
            if (self.iterator[middle] == element):
                print("Found element")
                self.create_log(element)
                return True
            elif (element > self.iterator[middle]):
                new_iterator = Binary(self.iterator[middle:])
                new_iterator.binary_search(element)
            else:
                new_iterator = Binary(self.iterator[:middle])
                new_iterator.binary_search(element)





