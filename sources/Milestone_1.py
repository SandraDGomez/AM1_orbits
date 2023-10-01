# Archivo que permite ejecutar todo.
# Lo que vamos a hacer es importar las funciones del codigo Funciones.py
from numpy import array, zeros 
from Methods.Esquemas_Temporales_MS_1 import *
import matplotlib.pyplot as plt

## Datos iniciales
N = 10000 
U_O = array([1, 0, 0, 1])
dt = [0.1, 0.01, 0.001] # Es una lista de cosas, no un vector


## Inicializacion de variables
U_euler = zeros((len(dt),4,N+1)) # tensor de 3 matrices donde cada matriz será calculada con cada dt
U_RK4 = zeros((len(dt),4,N+1)) # tensor
U_CN = zeros((len(dt),4,N+1)) # tensor
#len(dt) lo que hace es dar el nº de elementos hay en la lista

U_euler[:,:,0] = U_O # De cada matriz coge todas las filas de la columna 0.
U_RK4[:,:,0] = U_O 
U_CN[:,:,0] = U_O 


for i in range (len(dt)):
    
    U_euler[i,:,:] = Euler( dt[i], U_euler[i,:,:], N ) 
    U_RK4[i,:,:] = RK4( dt[i], U_RK4[i,:,:], N ) 
    U_CN[i,:,:] = CN( dt[i], U_CN[i,:,:], N ) 
     
     
# Plot


##Figura 1:  EULER
fig, Euler_plt = plt.subplots(figsize = (4,4))
for i in range (len(dt)):
    
    Euler_plt.plot(U_euler[ i, 0, : ], U_euler[ i, 1, : ], label = "Euler Explícto dt =  " + str(dt[i]))
    
Euler_plt.set_xlabel('x')
Euler_plt.set_ylabel('y')
Euler_plt.set_title('Euler')
Euler_plt.legend()
# plt.show()
     
##Figura 2:  RUNGE KUTTA 4
fig, RK4_plt_plot = plt.subplots(figsize = (4,4))
for i in range (len(dt)):
    
    RK4_plt_plot.plot(U_RK4[ i, 0, : ], U_RK4[ i, 1, : ], label = "Runge Kutta 4 dt =  " + str(dt[i]))
    
RK4_plt_plot.set_xlabel('x')
RK4_plt_plot.set_ylabel('y')
RK4_plt_plot.set_title('Runge Kutta 4')
RK4_plt_plot.legend()
# plt.show()

##Figura 1:  EULER
fig, CN_plot = plt.subplots(figsize = (4,4))
for i in range (len(dt)):
    
    CN_plot.plot(U_CN[ i, 0, : ], U_CN[ i, 1, : ], label = "Crank Nicolson dt =  " + str(dt[i]))
    
CN_plot.set_xlabel('x')
CN_plot.set_ylabel('y')
CN_plot.set_title('Crank Nicolson')
CN_plot.legend()
plt.show()
