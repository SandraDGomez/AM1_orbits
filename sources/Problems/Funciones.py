from numpy import array, reshape, shape, zeros
from numpy.linalg import norm


##FUNCION DE KEPLER

def F_Kepler(U):
    
    x, y, vx, vy = U[0], U[1], U[2], U[3]
    mr = (x**2 + y**2 )**1.5
    
    return array( [vx, vy, -x/mr, -y/mr])


##PROBLEMA DEL OSCILADOR

def Oscilador_Lineal(U):
    
    return array([U[1], -U[0]])

## FUNCION DE LOS N-CUERPOS

def split(U):
    Nc = 3
    Nb = int(shape(U)[1]/(2*Nc))
    N = shape(U)[0] -1 
    
    Us = reshape(U, (N+1, Nb, Nc, 2))
    
    return reshape(Us[:, :, :, 0], (N+1, Nb, Nc))

def join(r0, v0, Nc, Nb):
    U0 = zeros(2*Nc*Nb)
    U1 = reshape(U0, (Nb, Nc, 2))
    
    U1 [:, :, 0] = r0 # Aqui se coge todos los valores de la columna 0
    U1 [:, :, 1] = v0
    return U0

# Problema en sí mismo de los N-cuerpos       

def N_B(U):
    
    Nc = 3
    Nb = int(len(U) / (2*Nc))
    
    Us = reshape(U, (Nb, Nc, 2))  # El ultimo es un tensor de Nb, Nc(Posicion, velocidad)
    
    r = reshape( Us[:, :, 0], (Nb, Nc) )  # Matriz de posicion
    v = reshape( Us[:, :, 1], (Nb, Nc) )  # Matriz de velocidad
    
    F = zeros(len(U))    # len lo que hace es que te devuelve la longitud de un elemento
    Fs = reshape( F,(Nb, Nc,2) )  # Se reordena el tensor de las F
    
    drdt = reshape( Fs[:,:,0], (Nb,Nc) ) # Matriz velocidad
    dvdt = reshape( Fs[:,:,1], (Nb,Nc) ) # Matrix aceleracion
    
    dvdt[:,:] = 0  # inicializar variables
    
    for i in range(Nb):
        drdt[i,:] = v[i,:]
        for j in range(Nb):
            if j != i:
                d = r[j,:] - r[i,:]
                dvdt[i,:] +=  d[:]/( norm(d)**3)
  
    return F
    