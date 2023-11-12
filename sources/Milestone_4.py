from numpy import array, linspace 
from Methods.Esquemas_Temporales import *
from Methods.Problema_Cauchy import P_C
from Problems.Funciones import F_Kepler, Oscilador_Lineal
import matplotlib.pyplot as plt
from Error.Richarson import Richarson, Convergencia
from Utilities.Plots import Pintar_error, Pintar_Conver
## Datos iniciales
N = [1000, 10000, 100000] 

U_0 = array([1, 0]) # Oscilador lineal libre
#Establecer un tiempo fijo, T, que queremos operar.
T = 10

#Inicializar el diccionario. Permite almacenar matrices de distintas
# dimensiones. Hay que darle como imputs una key que es del tipo string.
t = {} 
U_dic={}         
U_Euler_OL = {}
U_RK4_OL = {}
U_CN_OL = {}
U_In_Euler_OL = {}
for i in N:
    t[str(i)] = linspace(0,T,i+1)


for key in t: 
    
    U_Euler_OL[str(key)] = P_C( U_0, t[key], Oscilador_Lineal, Euler)
    print('Euler done')
    
    U_RK4_OL[str(key)] = P_C( U_0, t[key], Oscilador_Lineal, RK4)
    print('RK4 done')
    
    U_CN_OL[str(key)] = P_C( U_0, t[key], Oscilador_Lineal, CN)
    print('CN done')
    
    U_In_Euler_OL[str(key)] = P_C( U_0, t[key], Oscilador_Lineal, In_Euler)
    print('In_Euler done')

