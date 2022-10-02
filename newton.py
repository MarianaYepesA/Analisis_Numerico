import numpy as np


def f(x):
    #f=np.exp(2*x)-np.exp(x)-2
    f=np.exp(x-2)-np.log(x-1)-(x**2)+(4*x)-5
    return f

def g(x):
    f=2*np.exp(2*x)-np.exp(x)
    #f=-np.exp(-x)-1
    #f=np.exp(-x)
    return f

def newton(xi,tolerancia,iter):
    fx=f(xi)
    derx=g(xi)                       
    contador=0
    error=tolerancia+1               #definir un error estrictamente mayor a la tolerancia para empezar
    
    while error >tolerancia and fx!= 0 and derx!=0 and contador<iter:
        xn=xi-(fx/derx)              #formula para calcular un buen g(x) 
        fx=f(xn)
        print(abs(fx))
        derx=g(xn)
        error=abs(xn-xi)
        xi=xn
        contador+=1
        print(xi)
    if fx==0:
        print(xi," es raiz ")
    elif error<tolerancia:          #aproximación a una posible raíz de f(x)=0
        (xn, " es una aproximacion a una raíz con una tolerancia de: ",tolerancia)
    elif derx==0:                   #implica división por 0, método de newton falla.
        print(xn," es una posible raíz múltiple ")
    else:
        print("fracaso en", iter,"iteraciones")

def main():
    xi=float(input("X0 "))
    tolerancia=float(input("Tol "))
    nmax=int(input("iter "))
    newton(xi,tolerancia,nmax)

if __name__ == '__main__':
    main()
