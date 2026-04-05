import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Constants (choose normalized units)
R = 1
a = 1
b = 1

# Critical constants
Tc = 8*a/(27*R*b)
Vc = 3*b
Pc = a/(27*b**2)

# Volume range
V = np.linspace(0.4, 8, 500)

# Temperatures
T_values = [0.9*Tc, Tc, 1.1*Tc]

plt.figure(figsize=(8,6))

def pressure(V, T):
    return R*T/(V - b) - a/(V**2)

# Plot isotherms
for T in T_values:
    P = pressure(V, T)
    if np.isclose(T, Tc):
        plt.plot(V, P, 'k', linewidth=2.5, label="Critical isotherm")
    else:
        plt.plot(V, P, label=f"T = {T:.2f}")

# 🔷 Spinodal points (dP/dV = 0)
def dPdV(V, T):
    return -R*T/(V - b)**2 + 2*a/(V**3)

spinodal_points = []

T = 0.9*Tc
guesses = [0.6, 2, 5]

for g in guesses:
    try:
        root = fsolve(dPdV, g, args=(T))[0]
        if 0.4 < root < 8:
            spinodal_points.append(root)
    except:
        pass

spinodal_points = list(set(np.round(spinodal_points, 3)))

for V_s in spinodal_points:
    P_s = pressure(V_s, T)
    plt.scatter(V_s, P_s, color='red', zorder=5)
    plt.text(V_s, P_s, 'Spinodal', fontsize=8)

# 🔷 Coexistence region (Maxwell construction approximation)
V1, V2 = min(spinodal_points), max(spinodal_points)
P_coexist = pressure((V1+V2)/2, T)

plt.hlines(P_coexist, V1, V2, colors='purple', linestyles='dashed',
           label='Coexistence line')

# Labels
plt.xlabel("Volume (V)")
plt.ylabel("Pressure (P)")
plt.title("Van der Waals Isotherms")
plt.legend()
plt.grid()

plt.show()