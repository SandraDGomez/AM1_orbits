
from numpy import array, zeros
import matplotlib.pyplot as plt

def F_Kepler(U):
    
    x, y, vx, vy = U[0], U[1], U[2], U[3]
    mr = (x**2 + y**2 )**1.5
    
    return array( [vx, vy, -x/mr, y/mr])

N = 10000 
U= array([1, 0, 0, 1])
print( type (U))

dt =0.01
x = zeros(N)
y = zeros(N) 
x[0]=U[0]
y[0]=U[0]


for i in range (0, N):
    
    F =F_Kepler ( U )
    #F = array ( [U[2], U[3], -U[0]/(U[0]**2 + U[1]**2)**1.5, -U[1]/(U[0]**2 + U[1]**2)**1.5] )
    U = U + dt * F
    x[i]=U[0]
    y[i]=U[1]
    
    # U = zeros( (4, N) )
    # U_0 = [1,0,0,1] 
    # U[:,0] = U_0 signfica que todas las filas (:) la primera columna, que en python empieza por 0, tomen de valor ese vector.
    # for i in range(N):
    #   U[:, i+1] = U[:,i] + dt * F_kepler(U[:,i])


plt.plot ( x, y )
plt.show()