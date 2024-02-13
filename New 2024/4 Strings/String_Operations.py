# TODO -  Create a variable called `string_1` - assign it a value of "Hello "
# TODO -  Create a variable called `string_2` - assign it a value of "World!"
# TODO - Add `string_1` and `string_2`
# TODO - Print `string_3`

string_1 = "Hello "
string_2 = "World!"
string_3 = string_1 + string_2
print(string_3)

#Slicing a string
my_string = "one two three"
print('the first three characters of my string are:', '\n' + my_string[:3])
# TODO - print the 4th to 7th characters of the string
print('the last two characters are:' '\n' + my_string[-2:])

#Updating a String
string_1 = "Hello World!"
string_2 = "Crab!"
string_1 = string_1[:6] + string_2
print(string_1)

sentence_1 = 'Wow, what a large horse!'
substring_1 = "small"
# TODO - Replace "large" with "small" in the sentence
sentence_1 = sentence_1[:-12] + substring_1 + sentence_1[-7:]
print(sentence_1)

#Splitting Strings
my_filepath = "C:/Images/cow.jpg"
# TODO  Call `my_filepath`'s  `.split` method and assign the output to a variable called `my_file_structure`.
my_file_structure = my_filepath.split("/")
# TODO - print `my_file_structure`
print(my_file_structure)
# TODO - print just the filename
print(my_file_structure[2])
