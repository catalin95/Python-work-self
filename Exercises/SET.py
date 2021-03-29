#!/usr/bin/python3

class SET(object):

    def __init__(self, new_set):
        self.new_set = new_set

    def cardinal(self):
        count = 0
        for i in self.new_set:
            count += 1

        return count

    def show(self):
        if self.cardinal() == 0:
            print("Empty set")
            return False
        for i in self.new_set:
            print(i)

    def __eq__(self, other):
        if self.cardinal() == other.cardinal():
            return True
        else:
            return False

    def check_if_subset(self, other):
        if self.cardinal() < other.cardinal():
            count = 0
            for i in self.new_set:
                if i in other.new_set:
                    count += 1
                else:
                    continue

            if count == self.cardinal():
                return True
            else:
                return False
        else:
            return False

    def check_if_superset(self, other):
        output = other.check_if_subset(self)

        return output

    def union(self, other):
        for i in other.new_set:
            self.new_set.append(i)

        output = SET(set(self.new_set))

        return output

    def intersection(self, other):
        output = SET([])
        for i in self.new_set:
            for j in other.new_set:
                if i == j:
                    output.new_set.append(i)
        
        return output

    def complement(self, other):
        output = SET([])
        for i in self.new_set:
            if i not in other.new_set:
                output.append(i)

        return output
    
    
    def cartesian_product(self, other):
        output = SET([])

        for i in self.new_set:
            for j in other.new_set:
                new_tuple = []
                new_tuple.append(i)
                new_tuple.append(j)
                output.new_set.append(tuple(new_tuple))

        return output




    


