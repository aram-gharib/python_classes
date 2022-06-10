class Rectangular:
    created_rectangular = 0

    def __init__(self, *args):
        Rectangular.created_rectangular += 1
        (self.length_1, self.length_2, self.width_1, self.width_2) = args
        if self.length_1 == self.length_2 and self.width_2 != self.width_2:
            print("Valid Rectangular")
        else:
            raise ValueError

    def area(self):
        return self.length_1 * self.width_1

    def perimeter(self):
        return (self.length_1 + self.width_1) * 2

    def sorted_to_tuple(self):
        return sorted((self.length_1, self.width_2))

    def __gt__(self, other):
        if not isinstance(other, Rectangular):
            raise TypeError
        if self.length_1 > other.length_1 and \
                self.width_1 > other.width_2:
            return True
        return False

    def __eq__(self, other):
        if not isinstance(other, Rectangular):
            return TypeError
        return self.sorted_to_tuple == other.sorted_to_tuple

    def __ne__(self, other):
        return not self.__eq__(other)


rectangular_1 = Rectangular(1, 3, 5, 5)
rectangular_2 = Rectangular(2, 2, 3, 3)
# print(rectangular_1.__gt__(rectangular_2))
print(Rectangular.__init__())
