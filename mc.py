import numpy as np
import sympy as sp

# Defina os símbolos para theta
theta1, theta2, theta3, theta4, theta5, theta6 = sp.symbols('theta1 theta2 theta3 theta4 theta5 theta6')

# Substitua os símbolos theta nas expressões
a = sp.cos(theta2 + theta3 + theta4) * sp.cos(theta1) * sp.cos(theta5) * sp.cos(theta6) + sp.cos(theta6) * sp.sin(theta1) * sp.sin(theta5) - sp.cos(theta1) * sp.sin(theta2 + theta3 + theta4) * sp.sin(theta6)
b = -sp.cos(theta2 + theta3 + theta4) * sp.cos(theta1) * sp.cos(theta5) * sp.sin(theta6) - sp.sin(theta1) * sp.sin(theta5) * sp.sin(theta6) - sp.cos(theta1) * sp.sin(theta2 + theta3 + theta4) * sp.cos(theta6)
c = sp.sin(theta1) * sp.cos(theta5) - sp.cos(theta1) * sp.cos(theta2 + theta3 + theta4) * sp.sin(theta5)
d = -612.7 * sp.cos(theta1) * sp.cos(theta2) - 571.55 * sp.cos(theta1) * sp.cos(theta2 + theta3 + theta4) + 174.15 * sp.sin(theta1) + 119.85 * sp.cos(theta1) * sp.sin(theta2 + theta3 + theta4) + 116.55 * (sp.sin(theta1) * sp.cos(theta5) - sp.cos(theta1) * sp.cos(theta2 + theta3 + theta4) * sp.sin(theta5))
e = sp.sin(theta1) * sp.cos(theta2 + theta3 + theta4) * sp.cos(theta5) * sp.cos(theta6) - sp.cos(theta6) * sp.cos(theta1) * sp.sin(theta5) - sp.sin(theta1) * sp.sin(theta2 + theta3 + theta4) * sp.sin(theta6)
f = -sp.sin(theta1) * sp.cos(theta2 + theta3 + theta4) * sp.cos(theta5) * sp.sin(theta6) + sp.sin(theta6) * sp.cos(theta1) * sp.sin(theta5) - sp.sin(theta1) * sp.sin(theta2 + theta3 + theta4) * sp.cos(theta6)
g = -sp.cos(theta1) * sp.cos(theta5) - sp.sin(theta1) * sp.cos(theta2 + theta3 + theta4) * sp.sin(theta5)
h = -612.7 * sp.sin(theta1) * sp.cos(theta2) - 571.55 * sp.sin(theta1) * sp.cos(theta2 + theta3 + theta4) - 174.15 * sp.cos(theta1) + 119.85 * sp.sin(theta1) * sp.sin(theta2 + theta3 + theta4) - 116.55 * (sp.cos(theta1) * sp.cos(theta5) + sp.sin(theta1) * sp.cos(theta2 + theta3 + theta4) * sp.sin(theta5))
i = sp.sin(theta2 + theta3 + theta4) * sp.cos(theta5) * sp.cos(theta6) + sp.cos(theta2 + theta3 + theta4) * sp.sin(theta6)
j = -sp.sin(theta2 + theta3 + theta4) * sp.cos(theta5) * sp.sin(theta6) + sp.cos(theta2 + theta3 + theta4) * sp.cos(theta6)
k = -sp.sin(theta2 + theta3 + theta4) * sp.sin(theta5)
l = -612.7 * sp.sin(theta2) - 571.55 * sp.sin(theta2 + theta3) - 119.85 * sp.cos(theta2 + theta3 + theta4) - 116.55 * sp.sin(theta2 + theta3 + theta4) * sp.sin(theta5) + 180.7

# Crie a matriz 4x4
matrix = sp.Matrix([[a, b, c, d],
                    [e, f, g, h],
                    [i, j, k, l],
                    [0, 0, 0, 1]])


theta1_value = np.radians(90)
theta2_value = np.radians(0)
theta3_value = np.radians(90)
theta4_value = np.radians(0)
theta5_value = np.radians(90)
theta6_value = np.radians(0)

matrix = matrix.subs({theta1: theta1_value, theta2: theta2_value, theta3: theta3_value, theta4: theta4_value, theta5: theta5_value, theta6: theta6_value})

print("Matriz 4x4:")
sp.pprint(matrix, use_unicode=True)
