#ESTA ES UNA VERSIÓN ALTERNATIVA DE "pickle_gestor.py" TAMBIÉN PRESENTE EN ESTE REPOSITORIO ("herramientas").
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

def opcion_marcada(o):
    if o==("A"):
        return "Introduzca el número de campos que desea añadir: "
    else:
        return "Introduzca el número de campos que desea eliminar: "
    
def op_mar(o):
    if o==("A"):
        return "POSICIONES AÑADIDAS: "
    else:
        return "POSICIONES ELIMINADAS: "


def depura_list(cadena):
    cad=[]
    for i in cadena:
        try:
            i=int(i)
            cad.append(i)
        except:
            print("SE HA INCLUIDO NUMEROS NO ENTEROS O CARACTERES NO VALIDOS QUE SERÁN IGNORADOS")
    return cad
        

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
        print("ESTADO ACTUAL: ",contenido)
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
        if op==("A") or op==("B"):
            texto_inp=opcion_marcada(op)
            numero_campos=OKI(input(texto_inp))
            cam_invol=[]
            while op==("B") and numero_campos>len(nombre):
                numero_campos=OKI(input("El número de campos introducido es superior al número de campos actual: "))
            while n<numero_campos:
                if op==("A"):
                    nombre.append(0)
                    numcam+=1
                    cam_invol.append(numcam)
                else:
                    cam_invol.append(numcam)
                    numcam-=1
                    del nombre[-1]
                    cam_invol.sort()
                n+=1
            print("")
            print("NUEVO ESTADO: ",nombre)
            print(op_mar(op),cam_invol)
            print("")
        else: #op==("C"):
            camps_modif=input("Introduzca los campos a modificar separados por coma: ")
            lista_defin=depura_list(camps_modif.split(","))
            for i in lista_defin:
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
