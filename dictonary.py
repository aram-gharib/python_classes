# dict_1 = {1: 10, 2: 20}
# dict_2 = {3: 30, 4: 40}
# dict_3 = {5: 50, 6: 60}
# dict_4 = {6: 50, 7: 70}
# list_dict =[dict_1, dict_2, dict_3, dict_4]
# new_dict = {}
# for i in list_dict:
#     new_dict.update(i)
# print(new_dict)
# for j in [dict_1, dict_2, dict_3]:
#     new_dict.update(j)
# print(new_dict)

# def dict_multiply(n):
#     dict_ = {}
#     for x in range(1, n+1):
#         dict_[x] = x * x
    # return dict_
# n = 5
# print(dict_multiply(n))


def remove_none_from_dict(dict_1: dict):
     updated_dict = {}

     for key, value in dict_1.items():
         if value != None:
            updated_dict.update({key: value})
     return updated_dict
dict_1 = {'c1': "Red", 'c2': "Green", 'c3': None}

print(remove_none_from_dict(dict_1))
print(dict_1)

def remove_none_from_dict(dict_1: dict):
     updated_dict =(None, "", [], (), {}, 0)

     for key in dict_1.items():
         if value != None:
            updated_dict.update({key: value})
     return updated_dict
dict_1 = {'c1': "Red", 'c2': "Green", 'c3': None}


















