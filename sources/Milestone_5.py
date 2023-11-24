from numpy import zeros, linspace, transpose
from Methods.Problema_Cauchy import P_C
from Problems.Funciones import N_B, join, split
from Methods.Esquemas_Temporales import RK4
import matplotlib.pyplot as plt
from Utilities.Plots import Pintar_problemaNCuerpos

# Condiciones iniciales 

(Nb, Nc) = (4,3)   # Nº de cuerpos y coordenadas

r0 = zeros((Nb, Nc))  #Matriz posicon
v0 = zeros((Nb, Nc))  # Matriz velocidad

# Se establecen las condiciones inciales para cada cuerpo (Nb)

# body 1
r0[0,:] = [1,0,1]
v0[0,:] = [0, 0.4, 0]
# body 2
r0[1,:] = [-1,0,-1]
v0[1,:] = [0, -0.4, 0]
# body 3
r0[2,:] = [0,1,2]
v0[2,:] = [-0.4,0,0]
# body 4
r0[3,:] = [-2,-1,0]
v0[3,:] = [0.4,0,0]

# Lo siguiente es juntar todas las condiciones iniciales en un vector U0
# Esto se realiza mediante la función "join" que irá con reshapes
U0 = join(r0, v0, Nc, Nb)

# Para guardar imágenes
#  Save = True # True si deseas guardarlas, False, si solo quieres mostrarlas

# Seleccionar el nº de iteraciones que se desea hacer
N = 10000        # Pasos deseados a dar
T = 10         # Tiempo de duracion
t =linspace(0,T,N+1)  # Adaptarlo para el caso de querer tener una lista de N
dt = T/N
# Simulaciones  P_C( U_0, t, F, ET) 
# U = transpose( P_C(N_B, t, U0, RK4))
U = transpose( P_C(U0, t, N_B, RK4))

# Separar soluciones en tensores

r = split(U)

Pintar_problemaNCuerpos(r,T, dt, 'RK4')
plt.show()