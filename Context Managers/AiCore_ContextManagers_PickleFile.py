# rb() = read binary
# wb() = write binary
# open() = open function


# TODO: Import pickle module
import pickle

# TODO: Create a dictionary
my_dict = {
    "a":1,
    "b":2,
    "c":3
}

# TODO: Open a file in write binary mode and dump the dictionary into it
with open('mydict.pk1','wb') as opened_file:
    pickle.dump(my_dict, opened_file)
    
# TODO: Open the pickle file in read binary mode and load the dictionary from it
with open('mydict.pk1','rb') as opened_file:
    my_dict_2 = pickle.load(opened_file)

# TODO: Print the dictionary
    print(my_dict_2)
