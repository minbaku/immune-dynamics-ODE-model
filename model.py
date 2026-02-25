# SRC
import numpy as np
def immune_system(y, t, alpha, beta, delta):
  A, T = y
   
  dA_dt = -delta A
  dT_dt = alpha * A - beta * T
  
  return[dA_dt, dT_dt]

