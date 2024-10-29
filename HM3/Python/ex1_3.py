from sympy import symbols, Matrix, pprint, sin, cos, cosh, sinh, tan, simplify, init_printing, diff, ln, latex

init_printing(use_unicode=True, wrap_line=False)


# T 3 -----------------------------------------------------
print("T3 -----------------------------------------")

# f
x1, x2, phi = symbols('x1 x2 phi')
f = x1 **2 + 2*x1*x2 - 3*x2
d = Matrix([cos(phi), sin(phi)])

gradient = [diff(f, var) for var in (x1, x2)]

print("Gradient: ")
pprint(gradient)

directional_derivative = sum(grad * d[i] for i, grad in enumerate(gradient))

print("Richtungsableitung: ")
pprint(directional_derivative)

print("")

print(latex(gradient))
print(latex(directional_derivative))
