from numpy import zeros, linspace, shape 
from Methods import Problema_Cauchy
from Problems import Funciones
from Methods import Esquemas_Temporales

# Condiciones iniciales
r0 =[1,0]
v0 = [0,1]
U0 = r0 + v0
T =100
dt = [0.01]
