# © Bhuvan Jeyaganesan 2026
# MIT License
# Creator Bhuvan Jeyaganesan
# Terminal Velocity finder

# Print Title
print(f"\nTerminal Velocity Finder\n")

# Set Constants
g = 9.81
print("Gravity (m/s^2) =", g)

rho = 1.225
print("Air density (kg/m^3) =", rho, "\n")

# Get Operation To Perform
print("Operation To perform:")
OppType = input("Find Velocity (vel) Or Find Mass (mass): ")

# Perform Operation
if OppType == "vel":
    # Get Inputs
    m = float(input("Mass (kg): "))
    Cd = float(input("Drag Coefficient (Cd): "))
    A = float(input("Cross-sectional Area (m^2): "))

    # Formula: sqrt((2mg)/(rho * Cd * A))
    v = ((2 * m * g) / (rho * Cd * A)) ** 0.5

elif OppType == "mass":
    # Get Inputs
    v = float(input("Terminal Velocity (m/s): "))
    Cd = float(input("Drag Coefficient (Cd): "))
    A = float(input("Cross-sectional Area (m^2): "))

    # Formula: (v^2 * rho * Cd * A) / (2g)
    m = (v * v * rho * Cd * A) / (2 * g)

# Print Answers
print("\nResults")
print(f"Mass full (kg) = {m:.3f}")
print(f"Mass scientific (kg) = {m}")
print(f"Terminal Velocity (m/s) = {v:.3f}")
