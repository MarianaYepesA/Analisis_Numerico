import numpy as np
import math 

def g(x):
    f=0 #acá se pone la función
    return f

def puntofijo(x0,tolerancia,iter):
    xa=x0
    error=tolerancia + 1
    contador=0

    while (error>tolerancia and contador<=iter):
        xn=g(xa)              #hallar iterativamente nuevas aproximaciones a la raiz
        print(xn)
        varaux=error
        error=np.abs(xa-xn)
        xa=xn
        contador+=1
        print(contador,xn,error)
        

    if error>tolerancia:
        print("no pudimos llegar a esa tolerancia con ",contador,"iteraciones")
    else:
        print("hubo ",contador," iteraciones y la raiz se encuentra en ",xa," con un error de ", error)


def main():
    tolerancia=float(input("¿qué tolerancia necesitas? "))
    x0=float(input("¿en qué valor deseas iniciar? "))
    iter=int(input("¿cuál es el número máximo de iteraciones permitidas? "))
    puntofijo(x0,tolerancia,iter)

if __name__ == '__main__':
    main()
