import numpy as np

def f(x):
    #f=np.exp(3*x-12)+x*np.cos(3*x)-x**2+4
    f=14.2*np.tan(x)-((6.4*((14.2)**2))/((2*(25.4)**2)*((np.cos(x))**2)))
    return f
    
iter = int(input("Iteraciones= "))
x0 = float(input("X0= "))
x1 = float(input("X1= "))
tolerancia = float(input("Tolerancia= "))

f0 = f(x0)
if f0 == 0:
    print(x0,"es raiz")
else:
    f1 =f(x1)
    contador = 0
    error = tolerancia + 1
    den = f1-f0                         
    
    while error>tolerancia and f1 != 0 and den != 0 and contador<iter:
        x2 = x1 - (f1*(x1 - x0)/(den))
        error=abs(x2 - x1)
        x0 = x1
        f0 = f1
        x1 = x2
        f1 = f(x1)
        den = f1-f0
        contador += 1

    if f1 == 0:
        print(x1 ,"es raiz")
    elif error < tolerancia:
        print(x1,"es una aproximación con tolerancia =",tolerancia)

    elif den == 0:
        print("hay una posible raíz múltiple")
    else:
        print("fracaso en ",iter,"iteraciones")