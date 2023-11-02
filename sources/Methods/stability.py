from numpy import array, zeros, linspace, abs, transpose, float64
from Esquemas_Temporales_MS_1 import Euler, RK4, CN
import matplotlib.pyplot as plt
 
def Stability_Region (Esquemas_Temporales_MS_1, N, x0, xf, y0, yf)
    x = linspace(x0, xf, N)
    y = linspace(y0, yf, N)

    for i in range(N):
     for j in range(N):
        
        w = complex(x[i], y[j])
        r = Esquemas_Temporales_MS_1(1. 1., 0., lambda u, t:w*u)
        rho [i,j] = abs(r)
        
    return rho, x, y

def test_Stability_regions():
    schemes = [Euler, RK4, CN]
    from scheme 