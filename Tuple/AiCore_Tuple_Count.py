vowels = ("a", "e", "i", "o", "u")
vow = vowels.count("i")
#print(vow)

my_tuple = (1, 'f', [1, 2, 3], [4, 5], ('f', 'd'), ('f', 'd', 'e'), [1, 2, 3], 'a')

count_1 = my_tuple.count([1, 2, 3])
count_2 = my_tuple.count(('f', 'd')) 
print(count_1)
print(count_2)