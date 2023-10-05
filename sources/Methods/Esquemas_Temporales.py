from scipy.optimize import fsolve 

#EULER
def Euler(dt,U,F):
        
    return U + dt * F(U)

# RUNGE KUTTA 4

def RK4(dt,U,F):
   
    k1 = F( U )
    k2 = F( U + dt * k1 / 2 )
    k3 = F( U + dt * k2 /2 )
    k4 = F( U + dt * k3 )

    
    return U + dt / 6 * (k1 +2*k2 +2*k3 +k4)

# CRANCK NICOLSON
def CN(dt, U,F):
    
    def CN_res(x):
        # x es el residuo que se crea para resolver el método. Para ello es necesario utilizar un 
        # solucionador de 0 para que lo permita resolver los sistemas no lineales. En este caso es 
        # fsolve, aunque se podria resolver con el metodo de Newton
        return x - U_temp -dt/2 * F(x)

    U_temp = U + dt/2 * F(U)

    return  fsolve(CN_res,U)

#EULER IMPLICITO
def In_Euler(dt, U, F):

    def Euler_res(x):

        return x - U - dt*F(x)

    return fsolve(Euler_res, U)
