height = 1.73
weight = 60

BMI = (weight/height ** 2)

print(BMI)

#print BMi for different ranges

#f statements = put f before printing to input variable in {} halfway thru
#round() = round(var, value to round to)

if BMI <= 18.5:
    print(f"Your BMI is {round(BMI,2)}. You're in the underweight range.")
elif 18.5 < BMI <= 24.9:
    print(f"Your BMI is {round(BMI,4)}. You're in the healthy weight range.")
elif 25 < BMI <= 29.9:
    print(f"Your BMI is {round(BMI,2)}. You're in the overweight range.")
elif 30< BMI <= 39.9:
    print(f"Your BMI is {round(BMI,2)}. You're in the obese range.")
    


