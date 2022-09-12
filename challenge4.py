temp = float(input("enter wind temperature:"))
wspeed = float(input("enter wind speed:"))

def conversion (temp, wspeed):
    return (35.74+0.6215*temp-35.75*wspeed**0.16+0.4275*temp*wspeed**0.16)

def conversion (x, y):
    return (35.74+0.6215*x-35.75*y**0.16+0.4275*x*y**0.16)

a = conversion (10, 15)
b = conversion (0, 25)
c = conversion (-10, 35)

print (f"Temperature of 10 and speed of 15 gives windchill of: {a})")
print (f"Temperature of 0 and speed of 25 gives windchill of: {b})")
print (f"Temperature of -10 and speed of 35 gives windchill of: {c})")

print (f"Temperature: {temp}")
print (f"Speed: {wspeed}")
print (f"Windchill: {conversion (temp, wspeed)}")






