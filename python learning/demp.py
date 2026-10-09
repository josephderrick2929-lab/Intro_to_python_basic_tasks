rho = float(1.225)  # Example value for air at sea level
U = float(80)  # Example value for velocity
L = float(1)  # Example value for characteristic length
mu = float(1.81e-5)  # Example value for dynamic viscosity

Re = (rho * U * L) / mu

print(f"Density (rho): {rho} kg/m^3")
print(f"Velocity (U): {U} m/s")
print(f"Characteristic length (L): {L} m")
print(f"Dynamic viscosity (mu): {mu} Pa·s")
print(f"The Reynolds number (Re) is: {Re:.2f}")

if Re < 500000:
    print("The flow is laminar.")
elif Re >= 500001 and Re <= 1000000:
    print("The flow is transitional.")
elif Re > 1000000:
    print("The flow is turbulent.")


    