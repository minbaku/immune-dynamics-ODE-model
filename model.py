# SRC
import numpy as np
def immune_system(y, t, alpha, beta, delta):
  A, N, T = y
   
  dA_dt = -delta * A
  dN_dt = -alpha * A * N
  dT_dt = alpha * A - beta * T
  
  return[dA_dt, dN_dt, dT_dt]

