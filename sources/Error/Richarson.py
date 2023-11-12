from numpy import array, linspace, zeros, size, shape, log10
from numpy.linalg import norm
from alive_progress import alive_bar #to see the progress of the computations
from scipy.stats import linregress 

def Richarson(U0, t1, F, ET, problema, orden):
    # En las def unicamente importa mantener el orden, da igual que nombre le ponfas
    # en los parentesis, SOLO pon el orden correcto.
    #Orden: es el orden del ET
    
    N = size(t1) # El size unicamente coge la dimension del tiempo que le metas. Ejm 50 datos, 100 datos, etc.
    #size (numpy) sirve para matrices, len sirve para listas
    t2 = linspace(0, t1[-1],2*size(t1)) # Se coge en t1[-1] y lo qhe hace es coger el ultimo valor de t1
    Er = zeros((len(U0), N)) #creamos una matriz de ceros con la lista de U0 y N
    
    U1 = problema(U0, t1, F, ET)  # En realidad es meter el problema de Cauchy, manteniendo el orden de las variables
                                  # que luego se dirán quienes son el el archivo ppal donde lo usemos
    U2 = problema(U0, t2, F, ET)
    
    #Calcular el error para cada paso N
    for i in range(N): 
        
        Er[:,i] = (U2[:,2*i]-U1[:,i] ) / (1-1/2**orden)
        # Recorre todas las columnas hasta la ultima columna
    return Er

def Convergencia(U0, t1, F, ET, problema):
    
    m=10 #numero de puntos 
    Nt2 = size(t1)  # Se define de nuevo una nueva dimension del tiempo (otro nombre para evitar problemas con arriba)
    U1 = problema(U0, t1, F, ET)
    
    log_Er = zeros(m)
    log_N = zeros(m)
    
    U2 = zeros(shape(U1))
    for i in range(m):
        Nt2 = 2*Nt2
        t2 = linspace(0,t1[-1],Nt2)
        U2 = problema(U0,t2, F, ET)
        log_Er[i] = log10(norm(U2[:,-1] - U1[:,-1]))
        log_N[i] = log10(Nt2)
        t1 = t2
        U1 = U2
    return log_Er, log_N, linregress(log_N,log_Er)
        
      