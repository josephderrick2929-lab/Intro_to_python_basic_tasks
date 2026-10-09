import numpy as np
lapse_rate = 6.5
array = np.arange(0, 20001, 1000)
print(array)
temp = np.where( array < 11000, 288.15 - (((array)/1000) * lapse_rate) , 216.8)
print(temp)

T0 = 288
T = 216.8
L = 6.5/1000
R = 287
g = 9.81
P0 = 1.01325 * 100000
m = 28.97


p_low = np.where( array < 11000, ((T0/temp)**(-g/(L*R)))* P0 , 22.75 )
print(p_low)
p = ((T0/T)**(-g/(L*R)))* P0
print(p)
rho_array = np.where( array < 21000, 1.225 - (p_low * m ) / (R*temp), 0.05266) 
print(rho_array)


array = np.linspace(0, 20000, num=1000)
print(array)

results = [
    (0.5, 0.4, 0.03),   # (mach, CL, CD)
    (1.0, 0.6, 0.08),
    (1.5, 0.5, 0.06),
    (2.0, 0.4, 0.05),
]

with open("aerodynamic_results.txt", "w") as file:
    file.write(f"{'Mach':<10} {'CL':<10} {'CD':<10} {'L/D':<10}\n")
    file.write("-" * 40 + "\n")

    for mach, cl, cd in results:
        ld = cl / cd
        file.write(f"{mach:<10.1f} {cl:<10.3f} {cd:<10.3f} {ld:<10.2f}\n")