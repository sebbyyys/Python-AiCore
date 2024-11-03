dict_1 = {'London': [51.509865,-0.118092]} 
dict_2 = {'Paris': [48.864716, 2.349014]}

# TODO: Create a list of the two dictionaries
my_list = [dict_1, dict_2]

# TODO: Loop through the list
    # TODO: Get the name of the city by using the keys() method
    # TODO: Get the latitude of the city by using the index
    # TODO: Print the city name and latitude
for dict in my_list:
    x = dict.keys()
    for keys in x:
        print(f"{keys} : {dict[keys][0]}")