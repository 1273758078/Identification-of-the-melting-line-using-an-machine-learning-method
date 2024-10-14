import numpy as np

# Function to calculate gamma based on charge and Debye temperature
def calcu_gamma(Q=8000*1.60e-19, Td=1000):
    # Calculate the average particle spacing 'b' based on the given formula
    b = pow(np.pi * 6400 / pow(0.0335, 2), -0.5)
    Qs = pow(Q, 2)  # Square of the charge
    # Denominator consists of constants and temperature-dependent terms
    fpibktd = 4 * np.pi * b * 1.380649e-23 * Td * 8.854e-12
    return Qs / fpibktd  # Return gamma value

# Test the function with different Debye temperatures
# print(calcu_gamma(Td=19299.58296))
# print(calcu_gamma(Td=26458.96))
# print(calcu_gamma(Td=34278.01))
# print(calcu_gamma(Td=35378.05))
# print(calcu_gamma(Td=33426.12))

# Example calculation for a specific temperature
print(calcu_gamma(Td=33553.63))

# Additional calculations (commented out)
# b = 0.000236  # Particle spacing
# debey = 800e-6  # Debye length
# kappa = b / debey  # Calculate kappa
# print(kappa)
