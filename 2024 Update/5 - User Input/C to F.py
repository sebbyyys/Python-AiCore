# TODO - Ask the user for the temperature in Fahrenheit and store it in the variable 'fahrenheit'
# TODO - Cast the variable 'fahrenheit' to a float and store it in the variable 'fahrenheit'

f = input("What is the temperature in Fahrenheit")
f = float(f)

# TODO - Convert the temperature in Fahrenheit to Celsius and store it in the variable 'celsius'
celsius = round((f - 32) * (5/9), 2)
print(f"The temperature in Celsius is {celsius}")