rods = float(input ("Enter the number of rods."))
def rods_to_meters(rods):
    return rods*5.0292

def rods_to_feet(rods):
    return rods*5.0292/0.3048

def rods_to_miles(rods):
    return rods*5.0292/1609.34

def rods_to_furlongs(rods):
    return rods/40

def rods_to_mtw(rods):
    return rods*3.1/60

print (f"You entered {rods} rods")
print ("Here are the conversions:")
print (f"Meters: {rods_to_meters(rods)}")
print (f"Feet: {rods_to_feet(rods)}")
print (f"Miles: {rods_to_miles(rods)}")
print (f"Furlongs: {rods_to_furlongs(rods)}")
print (f"Minutes to walk {rods} rods:{rods_to_mtw(rods)}")
