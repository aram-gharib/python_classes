# def set_shallow_copy(set_1: set):
#     new_set = set_1.copy()
#     return new_set
#
#
# set_1 = {1, 5, "abc", (1, "hi")}
# print("old set is: ", set_1, "\n",id(set_1), "\n new set: ", set_shallow_copy(set_1), "\n", id(set_shallow_copy(set_1)))

# def max_and_min_set(set_2: set):
#       new_list = list(set_2)
#
#       return  dict([("min", sorted(new_list)[0]), ("max", sorted(new_list)[-1])])
#
# set_2 = {1, 4, 3, 9, 7}
# print(max_and_min_set(set_2))
# set_of_numbers = {5, 3, 1, 7, 0}
# new_set = list(set_of_numbers)
# print("Minimum value is: ", sorted(new_set)[0], "\n maximum value is: ", sorted(new_set)[-1])
# def differance_between_sets(set_1: set, set_2: set):
#       set_1.difference(set_2)
#       set_2.difference(set_1)
#       return dict([("differance between set_2 and set_1: ", set_2.difference(set_1)), \
#                   ("differance between set_1 and set_2: ", set_1.difference(set_2))])


# set_1 ={1, 5, "abc", (4, 15)}
# set_2 = {3, "abc", 15, 24}
# print(differance_between_sets(set_1, set_2))
# import copy
# set_1 = {1, 3, 5, "abc"}
# new_set = set_1.copy()
# new_set = copy.copy(set_1)
# new_set.add(2)
# print(set_1, id(set_1))
# print(new_set, id(new_set))







