import numpy as np

def immune_system(y, t, alpha, beta, delta):
    A, N, T = y
    
    dA_dt = -delta * A
    dN_dt = -alpha * A * N
    dT_dt = alpha * A * N - beta * T
    
    return [dA_dt, dN_dt, dT_dt]

from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Let Initial conditions be:
A0 = 10   # initial antigen concentration of Antigen
N0 = 100  # initial concentration of naive T-cells
T0 = 0    # initial activated T cells

y0 = [A0, N0, T0]

# Time range
t = np.linspace(0, 20, 300)

# Parameters
alpha = 0.01
beta = 0.3
delta = 0.4

# Solve ODE
solution = odeint(immune_system, y0, t, args=(alpha, beta, delta))

A = solution[:, 0]
N = solution[:, 1]
T = solution[:, 2]

# Plot
plt.plot(t, A, label="Antigen")
plt.plot(t, N, label="Naive T cells")
plt.plot(t, T, label="Activated T-cells")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.show()
plt.savefig("immune_dynamics.png", dpi=300, bbox_inches="tight")
