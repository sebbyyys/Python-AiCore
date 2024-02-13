#altitude in ft, airspeed in knots
altitude = 90
airspeed = 125

if altitude < 100 or altitude > 50000:
    print("unsafe flying")  
elif airspeed < 60 or airspeed > 500 :
    print("unsafe flying")
else:
    print("safe flying")