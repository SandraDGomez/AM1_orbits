import matplotlib.pyplot as plt

def plot(U, N, t, ET):

    fig, AX = plt.subplots(figsize = (4,4))
    for i in range (len(dt)):
        
        AX.plot(U[ 0, : ], U[  1, : ], label = ET.__name__ + " dt =  " + str(dt[i]))
        
    AX.set_xlabel('x')
    AX.set_ylabel('y')
    AX.set_title('Euler')
    AX.legend()
    # plt.show()



