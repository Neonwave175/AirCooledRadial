# © Bhuvan Jeyaganesan
# All Rights Reserved
# Creator Bhuvan Jeyaganesan
# Schwarzschild Radius finder

# Print Title
print(f"\nSchwarzschild Radius Finder\n")

# Set Constants
G = 6.6743e-11
print('Gravity Constant=', G)
C = 3.00e8
print('Speed of light=', C, "\n")

# Get Operation To Perform
print('Operation To perform:')
OppType = input('Mass->Rad(mass) Or Rad->Mass(rad): ')

# Perform Operation
if OppType == 'mass':
    # Get Input
    Mass = float(input("Mass(kg): "))
    # Formula: (2GM)/(C^2)
    Rad = (2*G*Mass)/(C*C)
elif OppType == 'rad':
    # Get Input
    Rad = float(input("Radius(m): ")) 
    # Formula: (RC^2)/(2G)
    Mass = (Rad*C*C)/(2*G)

# Print Answers
print(f'\n Results')
print(f"Mass full (kg) = {Mass:.0f}") #Full Value
print(f"Mass scientific (kg) = {Mass}") #Scientific Notation
print(f"Radius (m) = {Rad}") #Radius
