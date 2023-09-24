from Problems.Funciones import F_Kepler
from scipy.optimize import fsolve 

#EULER
def Euler(dt,U,N):
      
    for i in range(N):
        U[:, i+1] = U[:,i] + dt * F_Kepler(U[:,i])
        
    return U

# RUNGE KUTTA 4

def RK4(dt,U,N):
    
    for i in range(N):
        k1 = F_Kepler( U[:,i] )
        k2 = F_Kepler( U[:,i] + dt * k1 / 2 )
        k3 = F_Kepler( U[:,i] + dt * k2 /2 )
        k4 = F_Kepler( U[:,i] + dt * k3 )

        U[:, i+1] = U[:,i] + dt / 6 * (k1 +2*k2 +2*k3 +k4)  

    return U

# CRANCK NICOLSON
def CN( dt, U, N ):
    
    for i in range(N):

        def CN_res(x):
            
            return x - U_temp -dt/2 * F_Kepler(x)

        U_temp = U[:,i] + dt/2 * F_Kepler(U[:,i])


        U[:,i+1] = fsolve(CN_res,U[:,i])

    return U 
