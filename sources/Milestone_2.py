# Archivo que permite ejecutar todo.
# Lo que vamos a hacer es importar las funciones del codigo Funciones.py
from numpy import array, linspace 
from Methods.Esquemas_Temporales import *
from Methods.Problema_Cauchy import P_C
from Problems.Funciones import F_Kepler
import matplotlib.pyplot as plt

## Datos iniciales
N = [1000, 10000, 100000] 
U_0 = array([1, 0, 0, 1])
#Establecer un tiempo fijo, T, que queremos operar.
T = 20

#Inicializar el diccionario. Permite almacenar matrices de distintas
# dimensiones. Hay que darle como imputs una key que es del tipo string.
t = {}   
U_Euler = {}
U_RK4 = {}
U_CN = {}
U_In_Euler = {}

for i in N:
    t[str(i)] = linspace(0,T,i+1)
    # Este vector va desde 0 hasta T en N pasos. Por ej:
    # (0,10,9) va desde 0 hasta la posicion 10 y esa posicion la divide entre 9 "trozos"
    # Aquí por tanto, es dividir t_n que vamos a ir obteniendo,t0=0, t1= 0.02, t2=..., t3=..., t999=T

# Esquemas_T = [Euler, RK4, CN].

for key in t: 
    # Las key son las cosas que he definido en el diccionaro (la lista de N). 
    # Lo que hago es que meto esa key, para cada caso que yo quiero (en este todas las  key)
    # y se va a P_C con el vector t de esa K y me resuelve el metodo que le pido en concreto.)
    U_Euler[str(key)] = P_C( U_0, t[key], F_Kepler, Euler)
    
print('Euler done')
    
for key in t: 
    U_RK4[str(key)] = P_C( U_0, t[key], F_Kepler, RK4)
    
print('RK4 done')

    
for key in t: 
    U_CN[str(key)] = P_C( U_0, t[key], F_Kepler, CN)
    
print('CN done')
    
  
for key in t: 
    U_In_Euler[str(key)] = P_C( U_0, t[key], F_Kepler, In_Euler)
    
print('Inverse Euler done')

ET_plots = ['Euler_plt', 'RK4_plt', 'CN_plt', 'Inv_Euler_plt'] #  Lista de los nombre de los futuros objetos de plotear que voy a crear
U_plots = [U_Euler, U_RK4, U_CN, U_In_Euler] # lista con los resultados
Titles = ['Euler Explícito', 'Runge Kutta 4', 'Crank Nicolson', 'Euler Implícito'] # lista de los títulos

i = 0
for pintar in ET_plots:
    fig, pintar = plt.subplots(figsize = (4,4)) # Creo el objeto desde la lista
    # U = U_plots[]
    for key in t:
        dt = t[key][2] - t[key][1] # Se hace concatenacion. Es de la key en la que estés la posicon 2 - la 1.
        pintar.plot(U_plots[i][key][0, : ], U_plots[i][key][1, : ], label = "dt = " + str(dt))
    
    pintar.set_xlabel('x')
    pintar.set_ylabel('y')
    pintar.set_title(Titles[i])
    pintar.legend()
    i += 1 

plt.show()
     
