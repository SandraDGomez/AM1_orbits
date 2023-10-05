from numpy import zeros, array

# P_C= Problema de Cauchy

def P_C( U_0, t, F, ET ):
    # U_0 vector inicializador, t= tiempo a estudiar,
    # F= es la funcion, ET= esquema temporal
    
    ## Inicializacion de variables
    N = len(t) - 1 # Se define aquí con la t (tiempo), donde t-1.
    
    # Esto es así porque para hacer los pasos N, hay que tener en cuenta que se contabiliza
    # desde el 0 hasta el T y se cuentan los "saltos".Ejm
    # linspace (0,10,11) => [ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.] => Son 11 elementos y 10 "saltos (dts)"
    
    U = zeros( (len(U_0), N+1)) # La longitud de U_0 para que sea generalista
    U[:, 0] = U_0 # definimos el valor inicial

    dt = t[2] - t[1]
    for i in range (N):
        
        U[:, i + 1] = ET(dt, U[:,i], F)
         
    return U  


