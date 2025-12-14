from scipy.integrate import quad
import numpy as np
import math as m

def E(t):
    return 50*(m.e)**(-0.3*t)

result, error = quad(E, 0, 10)
print(f"Result: {result}, Estimated Error: {error}")