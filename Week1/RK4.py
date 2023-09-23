from numpy import * 
import matplotlib.pyplot as plt

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
  
    k1 = F_Kepler( U[:,i] )
    k2 = F_Kepler( U[:,i] + dt * k1 / 2 )
    k3 = F_Kepler( U[:,i] + dt * k2 /2 )
    k4 = F_Kepler( U[:,i] + dt * k3 )

    U[:, i+1] = U[:,i] + dt / 6 * (k1 +2*k2 +2*k3 +k4)

# Plot

fig, Runge4 = plt.subplots(figsize = (4,4))
Runge4.plot(U[0,:], U[1,:], label = "RK4")
Runge4.set_xlabel('x')
Runge4.set_ylabel('y')
Runge4.set_title('Rk4')
Runge4.legend()
plt.show()
