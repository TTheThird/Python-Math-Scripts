import sympy as sp

# Define the symbols
x, y = sp.symbols('x y')

# Define the function
f = x**2 + y**2  # Example function

# Compute the gradient of the function
gradient = [sp.diff(f, var) for var in (x, y)]

# Define the direction vector (e.g., v = (1, 1))
v = sp.Matrix([1, 1])

# Normalize the direction vector
v_normalized = v / v.norm()

# Compute the directional derivative
directional_derivative = sum(grad * v_normalized[i] for i, grad in enumerate(gradient))

# Display the results
print("Gradient:", gradient)
print("Normalized direction vector:", v_normalized)
print("Directional Derivative:", directional_derivative)

print(sp.latex(directional_derivative))