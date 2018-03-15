import pickle
from VALID import ns, opt, OKI
import time
import subprocess

def conte(x):
    while True:
        nombre=input("Introduzca el nombre del archivo al que desea acceder: ")
        try:
            contenido=pickle.load(open(nombre,"rb"))
            break
        except:
            print("NO SE ENCONTRO EL ARCHIVO ",nombre)
    if x==("a"):
        return contenido
    else:
        return(nombre)

        
def dat(n):
    try:
        n=int(n)
    except:
        try:
            n=float(n)
        except:
            n=str(n)
    return n

while True:
    print("Escoja una opción.")
    print("A)CREAR NUEVO ARCHIVO.")
    print("B)VER UN ARCHIVO.")
    print("C)INTRODUCIR CAMBIOS EN UN ARCHIVO.")
    op=opt(input("Introduzca aquí su opción: "),["A","B","C"])
    if op==("A"):
        lista=[]
        contenido=input("introduzca dato/s separados por coma: ")
        un=("").join(contenido)
        sep=un.split(",")
        for i in sep:
            elem=dat(i)
            print(type(elem))
            lista.append(elem)
        print(lista)
        nombreA=input("nuevo archivo: ")
        pickle.dump(lista,open(nombreA,"wb"))
        print(lista)
        print("El archivo se creo correctamente")
        
    elif op==("B"):
        contenido=conte("a")
        print("")
        print(contenido)
        print("")
    elif op==("C"):
        nombreA=conte("b")
        nombre=pickle.load(open(nombreA,"rb"))
        print("¿Que tipo de cambio es el que desea realizar?")
        print("A)AÑADIR CAMPOS")
        print("B)ELIMINAR CAMPOS")
        print("C)CAMBIAR DATOS")
        numcam=(len(nombre))-1
        n=0
        op=opt(input("Introduzca aquí su opción: "),["A","B","C"])
        if op==("A"):
            numero_campos=OKI(input("Introduzca el número de campos que desea añadir: "))
            cam_nuevos=[]
            while n<numero_campos:#DUPLICADO
                nombre.append(0)
                numcam+=1
                cam_nuevos.append(numcam)
                n+=1
            print("")
            print("NUEVO ESTADO: ",nombre)
            print("CAMPOS AÑADIDOS: ",cam_nuevos)
            print("")
        elif op==("B"):
            numero_campos=OKI(input("Introduzca el número de campos a eliminar: "))
            while numero_campos>len(nombre):
                numero_campos=OKI(input("El número de campos introducido es superior al número de campos actual: "))
            cam_eliminad=[]
            while n<numero_campos:#DUPLICADO
                cam_eliminad.append(numcam)
                numcam-=1
                del nombre[-1]
                n+=1
            cam_eliminad.sort()
            print("")
            print("NUEVO ESTADO: ",nombre)
            print("CAMPOS ELIMINADOS: ",cam_eliminad)
            print("")
        elif op==("C"):
            camps_modif=input("Introduzca los campos a modificar separados por coma: ")
            for i in camps_modif.split(","):
                if int(i)>=len(nombre):
                    print("")
                    print("EL CAMPO",i,"NO ESTA DISPONIBLE",chr(7))
                    print("")
                else:
                    nombre[int(i)]=dat(input("Escriba nuevo dato para posición: "))
                    print(nombre)
            print("NUEVO ESTADO: ",nombre)
        pickle.dump(nombre,open(nombreA,"wb"))      
    conti=ns(input("¿Desea continuar?: "))
    if conti==("n"):
        break
    subprocess.call(["cmd.exe","/C","cls"])

