import numpy as np
def f(x):
#    f=((x)**3)-(7.51*(x)**2)+(18.4239*(x))-14.8331
#    f=90*(x+40)*(x+27)*(x+95)-50000000
    #f=(1/x)+(0.4)-(1.74*np.log(20*np.sqrt(x)))
    f=np.exp(3*x-12)+x*np.cos(3*x)-x**2+4
    return f


def main():
    iter=int(input("número de iteraciones max= "))
    xi=float(input("xi= "))
    xf=float(input("xf= "))
    tolerancia=float(input("tolerancia= "))

    fi=f(xi)
    ff=f(xf)
    if fi==0:                             #evaluar si existe una raiz en los extremos del intervalo
        print(xi,"es raíz")
    elif ff==0:
        print(xf,"es raíz")
        
    elif fi*ff<0:                       #los extremos deben tener signos opuestos   
        contador=1
        xm=(xi+xf)/2                    #dividir iterativamente los intervalos en subintervalos de igual tamaño
        fm=f(xm)
        contador=1
        error=tolerancia+1              #definir un error estrictamente mayor a la tolerancia para empezar
        
        while error>tolerancia and fm != 0 and contador<iter:
            if fi*fm<0:                #evaluar de que lado del xm se encuentra la raiz
                xf=xm                  #la raíz se encuentra antes del xm actual
                ff=fm
                print("error",error)
                print("ff = ",ff,"----- Derecha")
                print("xf = ",xi)
                print("   ")

            else:
                xi=xm                  #la raíz se encuentra después del xm actual
                fi=fm
                print("error",error)
                print("fi = ",fm,"------- izquierda")
                print("xi = ",xi)
                print("   ")

            xa=xm
            xm=(xi+xf)/2
            fm=f(xm)
            error=abs(xm-xa)
            contador+=1
        
        if fm==0:                          #encontró la raíz
            print(xm ,"es raíz")
        elif error<tolerancia:             #llegó a una aproximación válida de una raíz
            print(xm,"es una aproximacion con un error de =",error)
        else:
            print("fracaso en ",iter,"iteraciones")
    else:
        print("El intervalo es inadecuado")


if __name__=="__main__":
    main()
    
