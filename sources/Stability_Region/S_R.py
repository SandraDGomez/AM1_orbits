from numpy import sqrt, linspace, zeros, absolute, array

def Stability_Region(ET):
    N = 100
    R = linspace(-5,5,N)
    I = linspace(-5,5,N)
    w = zeros([N, N], dtype = complex)
    for i in range(N):
        for j in range(N):
            w[j,i] = complex(R[i], I[j])

    if ET.__name__ == "LeapFrog":
        return absolute( ET(1,1,1, lambda U: w*U) )
    else:
        return absolute( ET(1,1, lambda U: w*U) )