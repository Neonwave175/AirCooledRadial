# © Bhuvan Jeyaganesan 2026
# MIT License
# Creator Bhuvan Jeyaganesan
# Energy Mass Equation

# Print Title
print(f"\nEnergy Mass Equation\n")

# Set Constants
C = 3.00e8
print('Speed of light=', C, "\n")

# Get Operation To Perform
print('Operation To perform:')
OppType = input('Mass->Energy(mass) Or Energy->Mass(energy): ')

# Perform Operation
if OppType == 'mass':
    # Get Input
    Mass = float(input("Mass(kg): "))
    # Formula: MC*C
    Energy = (float(Mass*C*C))
elif OppType == 'energy':
    # Get Input
    Energy = float(input("Energy(j): ")) 
    # Formula: 
    Mass = (float(C*C)/(Energy))
# Print Answers
print(f'\n Results')
print(f"Mass full (kg) = {Mass:.0f}") #Full Value
print(f"Mass scientific (kg) = {Mass}") #Scientific Notation
print(f"Energy Full(m) = {Energy:.0f}") #Full Value
print(f"Energy scientific (kg) = {Energy}") #Scientific Notation
