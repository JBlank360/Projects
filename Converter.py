print ("How many kilometers did you travel today?")
kms = input ()
miles = float(kms)/1.60934
# can instead add: miles = round(miles,2) on a seperate line for same rounding results.
print (f"Your travel distances of {kms}km is {round(miles, 2)} miles.")
