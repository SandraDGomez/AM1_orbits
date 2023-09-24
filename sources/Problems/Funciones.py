from numpy import array


##FUNCION DE KEPLER

def F_Kepler(U):
    
    x, y, vx, vy = U[0], U[1], U[2], U[3]
    mr = (x**2 + y**2 )**1.5
    
    return array( [vx, vy, -x/mr, -y/mr])
