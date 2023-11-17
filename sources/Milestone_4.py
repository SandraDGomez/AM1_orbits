from numpy import array, linspace 
from Methods.Esquemas_Temporales import *
from Methods.Problema_Cauchy import P_C
from Problems.Funciones import F_Kepler, Oscilador_Lineal
import matplotlib.pyplot as plt
from Error.Richarson import Richarson, Convergencia
from Utilities.Plots import Pintar_Oscilador, Pintar_SR
from Stability_Region.S_R import *
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
U_LeapFrog_OL ={}
for i in N:
    t[str(i)] = linspace(0,T,i+1)

# Aqui lo que se simula es ver como varian las oscilaciones para cada delta t
# # 
for key in t: 
    
    U_Euler_OL[str(key)] = P_C( U_0, t[key], Oscilador_Lineal, Euler)
    print('Euler done')
    
    U_RK4_OL[str(key)] = P_C( U_0, t[key], Oscilador_Lineal, RK4)
    print('RK4 done')
    
    U_CN_OL[str(key)] = P_C( U_0, t[key], Oscilador_Lineal, CN)
    print('CN done')
    
    U_In_Euler_OL[str(key)] = P_C( U_0, t[key], Oscilador_Lineal, In_Euler)
    print('In_Euler done')
    
    U_LeapFrog_OL[str(key)] = P_C( U_0, t[key], Oscilador_Lineal, LeapFrog)
    print('LeapFrog')
    
Pintar_Oscilador(U_Euler_OL, t,'Euler')
Pintar_Oscilador(U_RK4_OL, t,'Runge Kutta 4')
Pintar_Oscilador(U_CN_OL, t,'Crank Nicolson')
Pintar_Oscilador(U_In_Euler_OL, t,'Euler Inversa')
Pintar_Oscilador(U_LeapFrog_OL, t,'Leap Frog')



# Regiones de estabilidad: para poder ejecutar esta parte, en los esquemas implicitos es necesario resolverlos
# con Newton, el fsolve no funciona en dicho caso
Estab_reg = {}

Esquemas = [Euler, RK4, CN, In_Euler, LeapFrog]

for esquema in Esquemas:
    Estab_reg[esquema.__name__] = Stability_Region(esquema)
    Pintar_SR(Estab_reg[esquema.__name__], t, esquema)

plt.show()