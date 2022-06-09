# import random
import math


# # final_computer_num = []
# print("Lets play Cows and Bulls, \n For every correct digit in right place you will get cows \n For every correct digit in \
# wrong place you will get bulls")
#
#
# # computer_num = str(random.randint(1000, 9999))
#
# def cows_and_bulls():
#     computer_num = str(random.randint(1000, 9999))
#     cows = 0
#     while cows != 4:
#         cows = 0
#         bulls = 0
#         user_num = input("enter 4-digit number: ")
#         if len(user_num) > 4:
#             raise ValueError("enter 4 digit number")
#
#         else:
#             for i in range(4):
#                 if user_num[i] == computer_num[i]:
#                     cows += 1
#                 if user_num[i] != computer_num[i] and user_num[i] in computer_num:
#                     bulls += 1
#         print(cows, bulls)
#         print(computer_num)
#
#
# cows_and_bulls()



class Triangle:
    def __init__(self, side_1, side_2, side_3, height):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.height = height

    def validation_of_triangle(self):
        if self.side_1 + self.side_2 <= self.side_3 or self.side_2 + self.side_3 <= self.side_1 or \
                self.side_1 + self.side_3 <= self.side_2:
            return ValueError("triangle is not Valid")
        else:
            return "Valid"

    def calculate_area_of_triangle(self):
        semi_perimeter = (self.side_2 + self.side_3 + self.side_1) / 2
        return (semi_perimeter * (semi_perimeter - self.side_1) * (semi_perimeter - self.side_2) *
                (semi_perimeter - self.side_3)) ** 0.5

    def perimeter_of_triangle(self):
        return self.side_2 + self.side_3 + self.side_1


    def get_angle(self):
        return int(180 / math.pi * math.acos((self.side_2 ** 2 + self.side_3 ** 2 - self.side_1 ** 2) / \
                                             (2 * self.side_2 * self.side_3)))

    def similar_triangle(self, s_1, s_2, s_3):
        if s_1 * s_2 == self.side_1 * self.side_2 and s_2 * s_3 == self.side_2 * self.side_3 and \
        Triangle.get_angle(self) == int(180 / math.pi * math.acos((s_2 **2 + s_3 ** 2 -s_1 ** 2) / (2 * s_2 * s_3))):
            return True
        else:
            return False








triangle_1 = Triangle(2, 3, 3, 8)
# triangle_2 = Triangle(4, 6, 6)
print(triangle_1.similar_triangle(4, 6, 6))
# print(triangle_1.perimeter_of_triangle(), triangle_1.validation_of_triangle(), triangle_1.calculate_area_of_triangle())
