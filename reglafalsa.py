def f(x):
    f=((x)**3)-(7.51*(x)**2)+(18.4239*(x))-14.8331
#    f=90*(x+40)*(x+27)*(x+95)-50000000
    return f


def main():
    iter=int(input("Número de iteraciones= "))
    xi=float(input("xi= "))
    xf=float(input("xf= "))
    tolerancia=float(input("tolerancia= "))
    
    fi=f(xi)                             #mismas condiciones y características de bisección
    ff=f(xf)
    if fi==0:
        print(xi,"es raiz")
    elif ff==0:
        print(xf,"es raiz")
    elif fi*ff<0:
        xm=xi-(fi*(xf)/2)               #cambia el método para hallar el xm
        fm=f(xm)
        contador=1
        error=tolerancia+1
        while error >tolerancia and fm != 0 and contador<iter: 
            if fi*fm<0:
                xf=xm
                ff=fm
                print("ff = ",ff,"----- Derecha")
                print("xf = ",xi)
                print("   ")

            else:
                xi=xm
                fi=fm
                print("fi = ",fm,"------- izquierda")
                print("xi = ",xi)
                print("   ")
            xa=xm
            xm=(xi+xf)/2
            fm=f(xm)
            error=abs(xm-xa)
            contador+=1
        if fm==0:
            print("xm es raiz")
        elif error<tolerancia:
            print(xm,"es una aproximación con tolerancia =",tolerancia)
        else:
            print("fracasó en ",iter,"iteraciones")
    else:
        print("El intervalo es inadecuado")


if __name__=="__main__":
    main()
 
