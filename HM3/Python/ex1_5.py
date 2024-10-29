from sympy import symbols, Matrix, pprint, sin, cos, cosh, sinh, tan, simplify, init_printing, exp, ln, latex

init_printing(use_unicode=True, wrap_line=False)


# T 5 a -----------------------------------------------------
print("T5 a -----------------------------------------")

# f
x1, x2, x3 = symbols('x1 x2 x3')
f1 = sin(x1) * x2 * cos(x3)
f = Matrix([f1])

jacobian_matrix_1 = f.jacobian([x1, x2, x3])

print("Jacobi Matrix f:")
pprint(jacobian_matrix_1)
print(latex(jacobian_matrix_1))
print("")


# g
x1, x2, x3 = symbols('x1 x2 x3')
g1 = (3 * x3) / (sin(-x1 + 2*x2 + x3))
g = Matrix([g1])

jacobian_matrix_2 = g.jacobian([x1, x2, x3])

print("Jacobi Matrix g:")
#pretty_print(jacobian_matrix)
pprint(simplify(jacobian_matrix_2))
print(latex(simplify(jacobian_matrix_2)))


# T 5 b ----------------------------------------------------------
print("")
print("T5 b ---------------------------------------------")

# f
x1, x2, x3 = symbols('x1 x2 x3')
f1 = sin(x1) + ln(1- (x2 ** 2))
f2 = exp(-(x2 ** 2))
f3 = cosh(x1 * x3)
f = Matrix([f1, f2, f3])

jacobian_matrix_3 = f.jacobian([x1, x2, x3])

print("Jacobi Matrix f:")
pprint(jacobian_matrix_3)
print(latex(jacobian_matrix_3))
print("")

# g
x1, x2, x3 = symbols('x1 x2 x3')
g1 = x1 ** 3 + 2* x2 ** 2 + sin(x3)
g2 = x1 * x2 **2 * x3 ** 3
g3 = cos(x1) * sin(x2)
g = Matrix([g1, g2, g3])

jacobian_matrix_4 = g.jacobian([x1, x2, x3])

print("Jacobi Matrix g:")
#pretty_print(jacobian_matrix)
pprint(simplify(jacobian_matrix_4))
print(latex(jacobian_matrix_4))
print("")

# h
x1, x2, x3 = symbols('x1 x2 x3')
h1 = exp(3*x1**3 + 2*x2**2)
h2 = tan(exp(- (x2**2)))
h3 = sinh(x1*x2**2)
h = Matrix([h1, h2, h3])

jacobian_matrix_5 = h.jacobian([x1, x2])

print("Jacobi Matrix h:")
#pretty_print(jacobian_matrix)
pprint(simplify(jacobian_matrix_5))
print(latex(jacobian_matrix_5))
