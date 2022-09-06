rods = float(input ("Enter the number of rods."))
meters = rods*5.0292
feet = rods*5.0292/0.3048
miles = rods*5.0292/1609.34
furlongs = rods/40
mtw = rods*3.1/60
print ("You entered", rods, "rods")
print ("Here are the conversions:")
print ("Meters:", meters)
print ("Feet:", feet)
print ("Miles:", miles)
print ("Furlongs:", furlongs)
print ("Minutes to walk", rods, "rods", mtw)
