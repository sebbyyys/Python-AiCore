# TODO: Create a context manager that opens a file called `test.txt` in write mode and writes the message "Hello, I am a context manager!" to the file.
with open('test.txt', 'w') as opened_file:
    opened_file.write('Hello, I am a context manager!')
    
# TODO: Create a context manager that opens a file called `test.txt` in read mode and reads the contents of the file into a variable called `my_string`.
# TODO: Print `my_string `

file = open('test.txt', 'r')
my_string = file.read()

print(my_string)