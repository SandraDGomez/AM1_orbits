from numpy import zeros, array

# P_C= Problema de Cauchy
# Problema de condiciones inciales (valido para cualquier esquema temporal)

def P_C( U_0, t, F, ET ):
    
    # U_0 vector inicializador, t= tiempo a estudiar (Milstone_2.py),
    # F= es la funcion, ET= esquema temporal
    
    ## Inicializacion de variables
    
    N = len(t) - 1 #Longitud de N saltos de pasos.
    # Se define aquí con la t (tiempo), con t-1.
    
    # Para hacer los pasos N, hay que tener en cuenta que se contabiliza
    # desde el 0 hasta el T y se cuentan los "saltos".Ejm
    # linspace (0,10,11) => [ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.] => Son 11 elementos y 10 "saltos (dts)".
    
    U = zeros( (len(U_0), N+1)) # Matriz inicial de ceros. La longitud de U_0 para que sea generalista.
    U[:, 0] = U_0               # Definir el valor inicial.

    if ET.__name__ == "LeapFrog":
        for i in range(N):
            dt = t[i+1]-t[i]
            if t[i]==0:
                U[:,1] = U[:,0] + dt*F(U[:,0])
            else:
                U[:,i+1] = ET(dt, U[:,i-1], U[:,i], F)  
                
    elif ET.__name__ == "RKE":   
        
        for n in range (N):
            dt = t[n+1] - t[n]
            U[:, n + 1] = ET(dt, U[:,n], t, F)  
    else:   
        dt = t[2] - t[1]
        for n in range (N):
            
            U[:, n + 1] = ET(dt, U[:,n], F)
         
    return U  


