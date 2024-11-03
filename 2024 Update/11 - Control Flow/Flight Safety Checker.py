# TODO - Create a variable called altitude and set it to a value in ft
# TODO - Create a variable called airspeed and set it to a value in knots

# TODO - Create the if/else statement to check if the altitude is within the safe range

def flightSafety(altitude, airspeed):
    if not(50000 > altitude > 100) or not(500 > airspeed > 60):
        print("Flying is not safe")
    else:
        print("Flying is safe") 
    
flightSafety(900, 65)