class Dictionary:
    data_type = "Dictionary"

    def __init__(self, dict_):
        self.dict_ = dict_
        # self.sample_str = sample_str

    def duplicate_from_dictionary(self):
        dict_1 = {}
        for key, value in self.dict_.items():
            if value not in dict_1.values():
                dict_1[key] = value
        return dict_1

    def string_to_dictionary(self):
        dict_2 = {}
        for i in self:
            dict_2[i] = 1
        return dict_2
    def three_highest_values(self):
        value_ = self.dict_.values()
        return sorted(value_)[-3:]

dict_3 = Dictionary({"a": 20, "b": 20, "c": 303})
str_1 = "python"

print(Dictionary.duplicate_from_dictionary(dict_3))
print(Dictionary.three_highest_values(dict_3))
print(Dictionary.string_to_dictionary(str_1))

# class Circle:
#     method_for_circle = "Circle"
#     def __init__(self, radius):
#         self.radius = self .validate_number(radius)
#
#     def validate_number(self, number):
#         if number <= 0:
#             raise ValueError("Radius can not be negative or zero ")
#         return number
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#     def perimetr(self):
#         return 2 * self.radius * 3.14
# Circle_1 = Circle(int(input("Tell me the radius: ")))
# print(Circle.area(Circle_1), Circle.perimetr(Circle_1))


# def number(dict_):
#     value_ = dict_.values()
#     return sorted(value_)[-3:]
# print(number({"a": 20, "b": 18, "d": 30, "c": 50 }))

