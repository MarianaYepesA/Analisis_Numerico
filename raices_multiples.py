
import numpy as np
def f(x):
    f=np.exp(x-2)-np.log(x-1)-(x**2)+(4*x)-5
    return f
def derx(x):
    derx=np.exp(x-2)-(1/(x-1))-2*x+4
    return derx
def der2x(x):
    der2x=np.exp(x-2)+(1/((x+1)**2))-2
    return der2x

x0 = float(input("Aproximacion inicial x0: "))
tolerancia = float(input("Tolerancia: "))
iter = int(input("Numero de iteracciones maximas: "))


xa = x0
fa = f(xa)
error = tolerancia + 1                           
contador = 0

while(error > tolerancia and contador < iter):
    xn = xa - fa*derx(xa)/( ((derx(xa))**2) - fa*der2x(xa)) #método para hallar las raíces múltiples
    fn = f(xn)
    error = abs(xn - xa)
    contador += 1
    xa = xn
    fa =fn
    print(contador,xn,fn,error)
    
x = xn
iter = contador
err = error

print(f"Resutado -> {x} \nIteracio: {iter}\nError: {err}")
    
