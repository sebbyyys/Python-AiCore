dict_1 = {'London': [51.509865,-0.118092]} 
dict_2 = {'Paris': [48.864716, 2.349014]}

# TODO: Create a list of the two dictionaries
my_list = [dict_1, dict_2]

for dict in my_list:
    for keys in dict.keys():
        latitude = dict[keys][1]
        print(keys, ':', latitude)
