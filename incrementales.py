import numpy as np



def f(x):
    #f=((x)**3)-(7.51*(x)**2)+(18.4239*(x))-14.8331
    f=(1/x)+(0.4)-(1.74*np.log(20*np.sqrt(x)))
#    f=90*(x+40)*(x+27)*(x+95)-50000000

    return f

def main():
    x0=float(input("Xi= "))
    delta=float(input("Delta de x= "))
    iter=int(input("Número de iteraciones= "))

    f0=f(x0)
    if f0 == 0:
        print(x0, "es raíz")

    else:
        x1=x0+delta
        contador=0
        f1=f(x1)
        while(f0*f1>0 and iter>contador):
            x0=x1
            f0=f1
            x1=x0+delta
            f1=f(x1)
            contador+=1

        if f1==0:
            print( x1,"raíz" )

        elif f0*f1<0:
            print(f"Entre",x0,x1,"hay raíz")

        else:
            print("fracasó en ",iter,"iteraciones")
if __name__=="__main__":
    main()
