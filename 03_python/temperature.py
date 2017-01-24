# temperature conversion
temp_Kelvin = []
temperatures = [60.1, 78.3, 98.8, 97.1, 101.3, 110.0]
for x in  temperatures:
    T = (x - 32) * (5/9) + 273.15
    print(T)
    temp_Kelvin.append (T)
print ("Conversion complete")
print (temp_Kelvin)
