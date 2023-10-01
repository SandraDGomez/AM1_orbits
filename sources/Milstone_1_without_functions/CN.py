from numpy import * 
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


## VARIABLES
N = 10000  # Nº de particiones
dt =0.01 #cada cuanto queremos analizar a Kepler
U_0 = array([1, 0, 0, 1]) # Vector de estado elegido, las dos primeras componentes son  la posicion y las dos segundas de la velocidad 

## FUNCION DE KEPLER
def F_Kepler(U):
    
    x, y, vx, vy = U[0], U[1], U[2], U[3]
    mr = (x**2 + y**2 )**1.5 # mr es el modulo del vector posicion fijandote en la ecuacion de Euler
    #El array que devuelve es parte de la solucion de la Ecuacion de Euler (vector columnas)
    return array( [vx, vy, -x/mr, -y/mr])

## METODO RUNGE KUTTA

U = zeros( (4,N+1) )

U[:,0] = U_0

for i in range(N):

    def CN_res(x):
        
        return x - U_temp -dt/2 * F_Kepler(x)
    
    U_temp = U[:,i] + dt/2 * F_Kepler(U[:,i])
    
    
    U[:,i+1] = fsolve(CN_res,U[:,i])
    
# Plot

fig, CranckN = plt.subplots(figsize = (4,4))
CranckN.plot(U[0,:], U[1,:], label = "Cranck Nicolson")
CranckN.set_xlabel('x')
CranckN.set_ylabel('y')
CranckN.set_title('Cranck Nicolson')
CranckN.legend()
plt.show()
