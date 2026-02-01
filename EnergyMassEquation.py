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
OppType = input('Mass->Energy(mass) Or Energy->Mass(rad): ')

# Perform Operation
if OppType == 'mass':
    # Get Input
    Mass = float(input("Mass(kg): "))
    # Formula: MC*C
    Energy = Mass*C*C
elif OppType == 'rad':
    # Get Input
    Rad = float(input("Energy(j): ")) 
    # Formula: (RC^2)/(2G)
    Mass = (C*C)/E
