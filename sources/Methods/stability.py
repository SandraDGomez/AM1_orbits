from numpy import array, zeros, linspace, abs, transpose, float64
from Esquemas_Temporales import Euler, RK4, CN
import matplotlib.pyplot as plt
 
def Stability_Region (esquemas, N, x0, xf, y0, yf):
    x = linspace(x0, xf, N)
    y = linspace(y0, yf, N)
    rho = zeros((N,N), dtype=float64)

    for i in range(N):
        for j in range(N):
        
            w = complex(x[i], y[j])
            r = esquemas (1., 1., 0., lambda u, t:w*u)
            rho [i,j] = abs(r)
              
    return rho, x, y

def test_Stability_regions():
    scheme = [Euler, RK4, CN]
    for esquemas in scheme:
        rho, x, y = Stability_Region(esquemas, 100, -4, 2, -4, 4)
        plt.contour(x, y, transpose(rho), linspace(0, 1, 11))
        plt.axis('equal')
        plt.grid()
    plt.show()


