dict_1 = {'London': [51.509865,-0.118092]} 
dict_2 = {'Paris': [48.864716, 2.349014]}
MyList = [dict_1, dict_2]

for dict in MyList:
    for key in dict.keys():
        latitude = dict[key][0]
        print(key, ":", latitude)
        