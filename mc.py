import numpy as np
import sympy as sp

# Defina os símbolos para theta
t1, t2, t3, t4, t5, t6 = sp.symbols('theta1 theta2 theta3 theta4 theta5 theta6')

l1 = 180.7
l2 = 174.15
l3 = 612.7
l4 = 174.15
l5 = 571.55
l6 = 174.15
l7 = 119.85
l8 = 116.55

d1 = 0.1807
d2 = 0
d3 = 0
d4 = 0.17415
d5 = 0.11985
d6 = 0.11655

alp1 = np.pi/2
alp2 = 0
alp3 = 0
alp4 = np.pi/2
alp5 = -np.pi/2
alp6 = 0

a1 = 0
a2 = -0.6127
a3 = -0.57155
a4 = 0
a5 = 0
a6 = 0

def mat(t,d,a,alp):
        return sp.Matrix([[sp.cos(t), -sp.sin(t)*sp.cos(alp), sp.sin(t)*sp.sin(alp), a*sp.cos(t)],
                    [sp.sin(t), sp.cos(t)*sp.cos(alp), -sp.cos(t)*sp.sin(alp), a*sp.sin(t)],
                    [0, sp.sin(alp), sp.cos(alp), d],
                    [0, 0, 0, 1]])

# Matrices multiplication
mat1 = mat(t1,d1,a1,alp1)
mat2 = mat(t2,d2,a2,alp2)
mat3 = mat(t3,d3,a3,alp3)
mat4 = mat(t4,d4,a4,alp4)
mat5 = mat(t5,d5,a5,alp5)
mat6 = mat(t6,d6,a6,alp6)

HTM = mat1@mat2@mat3@mat4@mat5@mat6

theta1_value = np.radians(30)
theta2_value = np.radians(20)
theta3_value = np.radians(85)
theta4_value = np.radians(60)
theta5_value = np.radians(90)
theta6_value = np.radians(84)

matrix = HTM.subs({t1: theta1_value, t2: theta2_value, t3: theta3_value, t4: theta4_value, t5: theta5_value, t6: theta6_value})*1000

print("Matriz 4x4:")
sp.pprint(matrix, use_unicode=True)
