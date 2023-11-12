from numpy import array, linspace 
from Methods.Esquemas_Temporales import *
from Methods.Problema_Cauchy import P_C
from Problems.Funciones import F_Kepler
import matplotlib.pyplot as plt
from Error.Richarson import Richarson, Convergencia
from Utilities.Plots import Pintar_error, Pintar_Conver
## Datos iniciales
N = [1000, 10000, 100000] 
U_0 = array([1, 0, 0, 1])
#Establecer un tiempo fijo, T, que queremos operar.
T = 10

#Inicializar el diccionario. Permite almacenar matrices de distintas
# dimensiones. Hay que darle como imputs una key que es del tipo string.
t = {}   
U_Euler = {}
U_RK4 = {}
U_CN = {}
U_In_Euler = {}
Er_Euler ={}
Er_RK4 = {}
Er_CN = {}
Er_In_Euler = {}

for i in N:
    t[str(i)] = linspace(0,T,i+1)


caso = input('Ric: = 1; Conv= 2: ')

if caso == "1":
    
    for key in t: 
        Er_Euler[key] = Richarson(U_0, t[key], F_Kepler, Euler, P_C, 1)
        print(f'Ric: Euler {key}')

        Er_RK4[key] = Richarson(U_0, t[key], F_Kepler, RK4, P_C,4)
        print(f'Ric: RK4 {key}')
        
        Er_CN[key] = Richarson(U_0, t[key], F_Kepler, CN, P_C,1)
        print(f'Ric: CN {key}')
        
        Er_In_Euler[key] = Richarson(U_0, t[key], F_Kepler, In_Euler, P_C,4)
        print(f'Ric: In_Euler {key}')

    Pintar_error(Er_Euler, t, 'Euler')
    Pintar_error(Er_RK4, t, 'RK4')
    Pintar_error(Er_CN, t, 'CN')
    Pintar_error(Er_In_Euler, t, 'In_Euler')   
    
elif caso == "2":
    
    for key in t:
        
        log_Er_euler, log_N_euler, regress_euler = Convergencia(U_0,t[key], F_Kepler, Euler, P_C) 
        Pintar_Conver(log_N_euler, log_Er_euler, regress_euler,t[key][2]-t[key][1], 'Euler')
        print(f'Conv: Euler {key}')
        
        log_Er_RK4, log_N_RK4, regress_RK4 = Convergencia(U_0,t[key], F_Kepler, RK4, P_C) 
        Pintar_Conver(log_N_RK4, log_Er_RK4, regress_RK4,t[key][2]-t[key][1], 'RK4')
        print(f'Conv2: RK4 {key}')
        
        log_Er_CN, log_N_CN, regress_CN = Convergencia(U_0,t[key], F_Kepler, CN, P_C)
        Pintar_Conver(log_N_CN, log_Er_CN, regress_CN,t[key][2]-t[key][1], 'CN') 
        print(f'Conv: CN {key}')
        
        log_Er_In_Euler, log_N_In_Euler, regress_In_Euler = Convergencia(U_0,t[key], F_Kepler, In_Euler, P_C) 
        Pintar_Conver(log_N_In_Euler, log_Er_In_Euler, regress_In_Euler,t[key][2]-t[key][1], 'In_Euler')
        print(f'Conv: In_Euler {key}')
    
    plt.show()
    
    
    

