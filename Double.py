import math

# Constants
G = 6.67430e-11
c = 299792458

# Precompute constant for Schwarzschild in log10
LOG10_RS_FACTOR = math.log10(2 * G / (c ** 2))  # ~ -26.83

def format_log_value(log10_val):
    """Convert log10 value to scientific notation string"""
    exponent = int(math.floor(log10_val))
    mantissa = 10 ** (log10_val - exponent)
    return f"{mantissa:.3f}e{exponent}"

def compute():

    print("=== Log-Safe Exponential Mass Calculator ===\n")

    years = float(input("Enter time (years): "))
    doubling_days = float(input("Enter doubling time (days): "))
    mode = input("Input (s)tart mass or (e)nd mass? ").lower()

    days = years * 365
    doublings = days / doubling_days

    if mode == 's':
        start_mass = float(input("Enter starting mass (kg): "))
        log_start = math.log10(start_mass)
        log_end = log_start + doublings * math.log10(2)

    elif mode == 'e':
        end_mass = float(input("Enter final mass (kg): "))
        log_end = math.log10(end_mass)
        log_start = log_end - doublings * math.log10(2)

    else:
        print("Invalid option.")
        return

    # Schwarzschild radius in log space
    log_rs = LOG10_RS_FACTOR + log_end

    print("\n=== Results ===")
    print(f"Total doublings: {doublings:.2f}")
    print(f"Start mass: {format_log_value(log_start)} kg")
    print(f"End mass:   {format_log_value(log_end)} kg")
    print(f"Schwarzschild radius: {format_log_value(log_rs)} m")

    # Year-by-year breakdown
    print("\nYear-by-year:")
    for y in range(int(years) + 1):
        d = y * 365
        log_m = log_start + (d / doubling_days) * math.log10(2)
        log_r = LOG10_RS_FACTOR + log_m

        print(f"Year {y:2d}: Mass = {format_log_value(log_m)} kg | Rs = {format_log_value(log_r)} m")


if __name__ == "__main__":
    compute()
