
# open and write to a file with context manager
with open('test.txt', 'w') as opened_file:
    opened_file.write("Hello, I am a context manager!")

# open and read from the file with context manager and save it to variable
with open('test.txt','r') as opened_file:
    my_string = opened_file.read()
    print(my_string)