import numpy as np
from scipy.optimize import fsolve

def equations(vars):
    x, y = vars
    eq1 = np.sqrt((x - 2)**2 + (y + 1)**2) + np.sqrt((x - 5)**2 + (y - 2)**2) - 3*np.sqrt(2)
    eq2 = (x - 2)**2 + y**2 - 3
    return [eq1, eq2]

# Guess values for x and y
initial_guess = [2, 0]

# Solve the system of equations
solution = fsolve(equations, initial_guess)

x, y = solution
print(f"x = {x}, y = {y}")
