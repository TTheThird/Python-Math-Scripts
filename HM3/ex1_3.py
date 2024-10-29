from sympy import symbols, Matrix, pprint, sin, cos, cosh, sinh, tan, simplify, init_printing, diff, ln, latex

init_printing(use_unicode=True, wrap_line=False)


# T 3 -----------------------------------------------------
print("T3 -----------------------------------------")

# f
x1, x2, phi = symbols('x1 x2 phi')
f = x1 **2 + 2*x1*x2 - 3*x2
d = Matrix([cos(phi), sin(phi)])

gradient = [diff(f, var) for var in (x1, x2)]

pprint(gradient)

directional_derivative = sum(grad * d[i] for i, grad in enumerate(gradient))

pprint(directional_derivative)




# g
x1, x2, x3 = symbols('x1 x2 x3')
g1 = (3 * x3) / (sin(-x1 + 2*x2 + x3))
g = Matrix([g1])

jacobian_matrix_2 = g.jacobian([x1, x2, x3])

print("Jacobi Matrix g:")
#pretty_print(jacobian_matrix)
pprint(simplify(jacobian_matrix_2))

