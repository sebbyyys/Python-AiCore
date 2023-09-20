dict1 = {"name" : "jack", "age": 22, "favourite_colour" : "green"}
dict2 = {"name" : "matt", "age": 22, "favourite_colour" : "red"}
dict3 = {"name" : "seb", "age": 22, "favourite_colour" : "blue"}

my_list = [dict1, dict2, dict3]

# TODO: Create an empty dictionary called names_dict
dict = {}
# TODO: Loop through the list of dictionaries
for names in my_list:
    for key in names.keys():
    # TODO: Get the name of the person and store it in a variable called name        
        if key == 'name': 
            name = names.get('name')
    # TODO: Get the age of the person and store it in a variable called age
        elif key == 'age':
            age = names.get('age')
    # TODO: Get the favourite colour of the person and store it in a variable called favourite_colour
        elif key == 'favourite_colour':
            favourite_colour = names.get('favourite_colour')      
        else:
            print("error")
        
    # TODO: Create a new key in the names_dict dictionary with the name of the person as the key and a dictionary with the age and favourite colour as the value
    dict[name] = {"age":age,"favourite_colour":favourite_colour}     
    print(dict) 
                 


            
        
