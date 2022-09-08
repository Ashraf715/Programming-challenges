richter = float(input("Please enter a Richter scale value:"))

def richter_to_joules(richter):
    return 10**((1.5*richter)+4.8)

def joules_to_tnt(richter):
    return (richter_to_joules(richter))/(4.184*10**9)

print (f"Richter value:{richter}")
print (f"Equivalence in joules: {richter_to_joules(richter)}")
print (f"Equivalence in tons of TNT: {joules_to_tnt(richter)}")
