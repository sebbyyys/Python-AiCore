# # TODO - Create a dictionaries named dict_1, according to the schema above
# dict_1 = {
#     'name': 'vahin',
#     'skills': ['smoking like its breathing', 'not having money', 'being unemployed']
# }

# # TODO - Create a dictionaries named dict_2, according to the schema above
# dict_2 = {
#     'name': 'jack',
#     'skills': ['geting rimmed', 'cheating', 'not being able to save money']
# }

# # # TODO - Put both of them in a list called `list_of_dictionaries`
# list_of_dictionaries = [dict_1, dict_2]

# for dict in list_of_dictionaries:
#     for keys in dict.keys():
#         if keys == "name":
#             continue
#         else:
#             r = dict[keys][0][-1]
#             print(r)

dict_1 = {
        'name': 'John',
        'skills': ['Python', 'JavaScript', 'HTML']
    }

# TODO - Create a dictionaries named dict_2, according to the schema above
dict_2 = {
        'name': 'Mayer',
        'skills': ['Python', 'JavaScript', 'CSS']
    }


list_of_dictionaries = [dict_1, dict_2]


# TODO - Now index that list of dictionaries to find the last letter of the first skill of the last dictionary.
# dict = list_of_dictionaries[-1]
# firstSkills = dict['skills'][0]
# lastLetter = firstSkills[-1]
# print(lastLetter)

# TODO - Create a list comprehension which maps that list to a list of the length of names. Assign it to a variable called `name_lengths`.

name_lengths = [len(x['name']) for x in list_of_dictionaries]

# TODO - add the lengths together

sum_lenghts = sum(name_lengths)
print(sum_lenghts)



        