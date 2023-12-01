from numpy import array, save, zeros, linspace, shape, reshape, around
from Methods.Problema_Cauchy import P_C
from Methods.RKEmbe_Esquema import RKE
from Problems.NBody import P_Lagrange, stb_Lp, RBP
from Utilities.Plots import Pintar_ProblemaLagrange
import matplotlib.pyplot as plt

# Esquema temporal escogido
ET = [RKE]

#Datos del sistema

mu_T_M = 1.2151e-2

#Inicializacion de variables
N = 10000
t = linspace(0,100,N)

#Condiciones inciales de intermpolacion
 
# 5 puntos de Lagrange y 4 es el numero de coordenadas 
U0 = zeros([5,4])
U0[0,:] = [0.8, 0.6, 0, 0]
U0[1,:] = [0.8, -0.6, 0, 0]
U0[2,:] = [-0.1, 0, 0, 0]
U0[3,:] = [0.1, 0, 0, 0]
U0[4,:] = [1.01, 0, 0, 0]

#Declarar el problema de Lagrange

L_p = P_Lagrange(U0, shape(U0)[0], mu_T_M)
print( "\n" + str(L_p) + "\n" )

#Estabilidad de los puntos de Lagrange

L_p_stb = zeros(4)  #Inicializcion de variables

for i in range(shape(U0)[0]):
    L_p_stb[:2] = L_p[i,:] 
    stb = around(stb_Lp(L_p_stb, mu_T_M),5 )
    print(str(stb) + "\n")
    

#Puntos de Lagrange en orbitas

U_0LPO = zeros( [shape(U0)[0], 4] )

eps = 1e-5   # Considerar las perturbaciones para obtener el movimiento

for i in range( shape(U0)[0]):
    U_0LPO[i, :2] = L_p[i,:] + eps
    U_0LPO[i, 2:] = eps
    
def F(U,t):
    return RBP(U,t, mu_T_M)

for i in range(shape(U0)[0]):
    U_LP = P_C(F,t, U_0LPO[i,:], ET[i])
    Pintar_ProblemaLagrange(U_LP, L_p, mu_T_M, ET[i])

plt.show()