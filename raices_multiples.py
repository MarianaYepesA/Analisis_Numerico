
import numpy as np
def f(x):
    f=0 #acá se pone la función
    return f
def derx(x):
    derx=0 #acá se pone la primera derivada
    return derx
def der2x(x):
    der2x=0 #acá se pone la segunda derivada
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
    
