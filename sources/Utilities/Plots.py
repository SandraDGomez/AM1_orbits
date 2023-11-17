import matplotlib.pyplot as plt
from numpy import sqrt, zeros, linspace

def Pintar_error(Er, t, ET):
     #Er_todos representara todos los errores numericos que se obtienen para los diferentes dt

    fig, (Er_x, Er_y, Er_n) = plt.subplots(3,1,figsize = (4,4)) # Creo el objeto desde la lista
    
    colors = ['r','b','g'] 

    for i, key in enumerate(t):
        
        dt = t[key][2] - t[key][1] # Se hace concatenacion. Es de la key en la que estés la posicion 2 -  1.
        Er_normal = sqrt(Er[key][0,:]**2 + Er[key][1,:]**2)
        Er_x.plot( t[key], Er[key][0,:],color = colors[i], label = f'dt = {dt}' ) # Entra a la key p y coge todas las columnas
        Er_y.plot( t[key], Er[key][1,:],color = colors[i], label = f'dt = {dt}' )
        Er_n.plot(t[key], Er_normal, color = colors[i], label = f'dt = {dt}')
        # poner en lable f'dt={} lo que hace la f es convertir a string todo lo que le metas. Lo que está entre corchetes es lo que quieres convertir
         
    Er_x.set_xlabel('t')
    Er_x.set_ylabel('x')
    Er_y.set_xlabel('t')
    Er_y.set_ylabel('y')
    Er_n.set_xlabel('t')
    Er_n.set_ylabel('modulo')
    Er_x.set_title(f'Error del esquema {ET}')
    Er_x.legend()
    Er_y.legend()
    Er_n.legend()
    

    plt.show()
    
def Pintar_Conver(x,y, regress,dt,ET):
    fig,Conver = plt.subplots(figsize =(4,4))
    colors = ['r','b','g'] 
    Conver.plot(x,y, color ='b', label = 'Resultados numericos')
    Conver.plot(x, regress.intercept + regress.slope*x, '--', color = 'r', label = 'Regresion')
    Conver.set_xlabel('Log_N')
    Conver.set_ylabel('Log_Er')
    Conver.set_title(f'{ET} con dt = {dt} ')
    Conver.legend()

def Pintar_Oscilador(OL, t, ET):
    
    colors = ['r','b','g'] 
    # pinturas = [f'{ET}_1',f'{ET}_2',f'{ET}_3']
    fig, OL_x = plt.subplots(figsize=(4,4))
    
    for i, key in enumerate(t): 
           
        
        dt = t[key][2]-t[key][1]
        OL_x.plot(t[key], OL[key][0,:], color =colors[i], label = f'dt = {dt}')
        OL_x.set_xlabel('t')
        OL_x.set_ylabel('x')
        OL_x.set_title(f'Valor del oscilador {ET}')
        OL_x.legend()

def Pintar_SR(r, t, ET):
    
    SR_pintar = plt.figure(figsize = (10, 10))
    if ET.__name__ == 'LeapFrog':
        Im = linspace(-1,1,100)
        Re = zeros(100)
        
        SR_pintar = plt.plot(Re, Im, color = '#0013ff')
        
    else:
        N = len(r)
        x = linspace(-5,5,N)
        y = linspace(-5,5,N)
        SR_pintar = plt.contour(x,y, r, levels = [0, 1], colors = ['#0013ff'])
        SR_pintar = plt.contourf(x,y, r, levels = [0, 1], colors =['#626262'])

    colors = ['r','orange','g']

    for i, key in enumerate(t):
        dt = t[key][2] - t[key][1] 
        plt.plot([0,0], [dt,-dt], 'o', color = colors[i], label = "Oscilator's Roots by dt " + str(dt))
    plt.ylabel("Im")
    plt.xlabel("Re")
    plt.title(f'Stability Region of {ET.__name__}')
    plt.legend()
    plt.grid()

      


