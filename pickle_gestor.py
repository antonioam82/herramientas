import pickle
from VALID import ns, opt, OKI
import time
import subprocess
import os

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

def busca_ar(n):
    try:
        n=pickle.load(open(n,"rb"))
        sob=ns(input("Ya existe un archivo con ese nombre ¿Desea sobreescribirlo?: "))
        if sob==("s"):
            pickle.dump(lista,open(nombreA,"wb"))
        else:
            return False 
    except:
        pickle.dump(lista,open(n,"wb"))#nombreA
        

def depura_list(cadena,archi):
    cad=[]
    for i in cadena:
        try:
            i=int(i)
            if i<0:
                i=(archi)+(i)
            cad.append(i)
        except:
            print("SE HA INCLUIDO NUMEROS DECIMALES O CARACTERES NO VÁLIDOS QUE SERÁN IGNORADOS")
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
        datt=ns(input("¿Añadir datos ahora?: "))
        lista=[]
        if datt=="s":
            contenido=input("Introduzca dato/s separados por coma: ")
            un=("").join(contenido)
            sep=un.split(",")
            for i in sep:
                elem=dat(i)
                print(type(elem))
                lista.append(elem)
        #print(lista)
        nombreA=input("Nombre del nuevo archivo: ")
        busca=busca_ar(nombreA)
        if busca==False:
            subprocess.call(["cmd.exe","/C","cls"])
            continue
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
        print("")
        print("ESTADO ACTUAL: ",nombre)
        print("")
        print("¿Que tipo de cambio es el que desea realizar?")
        print("A)AÑADIR CAMPOS")
        print("B)ELIMINAR CAMPOS")
        print("C)MODIFICAR DATOS")
        print("D)RENOMBRAR ARCHIVO") #NUEVO
        numcam=(len(nombre))-1
        n=0
        op=opt(input("Introduzca aquí su opción: "),["A","B","C","D"])
        if (op=="B" or op=="C") and len(nombre)==0:
            if len(nombre)==0:
                print("EL ARCHIVO ESPECIFICADO ESTÁ VACÍO")
                conti=ns(input("¿Desea continuar?: "))
                if conti=="s":
                    try:
                        subprocess.call(["cmd.exe","/C","cls"])
                        continue
                    except:
                        continue
                else:
                    break
        if op==("A"):
            lista=[]
            cam_nuevos=[]
            contenido=input("Introduzca los nuevos datos que desea añadir, separados por coma: ")
            un=("").join(contenido)
            sep=un.split(",")
            for i in sep:
                elem=dat(i)
                print(type(elem))
                lista.append(elem)
                numcam+=1
                cam_nuevos.append(numcam)
            nombre=nombre+lista
            print("")
            print("NUEVO ESTADO: ",nombre)
            print("DATOS AÑADIDOS: ",lista)
            print("POSICIONES AÑADIDAS: ",cam_nuevos)
            print("")
            
        elif op==("B"):
            campos_a_eliminar=input("Introduzca las posiciones a eliminar separadas por coma: ")
            lista_defin=depura_list(campos_a_eliminar.split(","),len(nombre))
            camb=0
            if len(lista_defin)>0:
                n=max(lista_defin)
                m=min(lista_defin)
                while n>=m:
                   if n in lista_defin:
                       if n>=len(nombre) or n<0:
                           if n<0:
                               n=-1*((abs(n)+(len(nombre)+camb)))
                           print("La posición ",n,"está fuera de rango, por lo que será ignorada.")
                       else:
                           del nombre[n]
                           camb+=1
                   n-=1
            if camb>0:
                print("")
                print("NUEVO ESTADO: ",nombre)
                print("")

        elif op==("C"):
            camps_modif=input("Introduzca los campos a modificar separados por coma: ")
            lista_defin=depura_list(camps_modif.split(","),len(nombre))
            dats_added=0
            for i in lista_defin:
                if i<0:
                    i=-1*(abs(i)+len(nombre))#
                if int(i)>=len(nombre)or int(i)<0:
                    print("")
                    print("EL CAMPO",i,"NO ESTA DISPONIBLE",chr(7))
                    print("")
                else:
                    nombre[int(i)]=dat(input("Escriba nuevo dato para la posición "+str(i)+": "))
                    dats_added+=1
            if dats_added>=1:
                print("")
                print("NUEVO ESTADO: ",nombre)
                print("")
            #else:
                #print("NO SE PUDO COMPLETAR LA OPERACION (DATO/S INTRODUCIDO/S INCORRECTO/S)")#¿REALMENTE HACE FALTA?
                
        elif op=="D":############################################################
            nuevo_nombre=input("Intoduzca nuevo nombre para el archivo: ")##
            lista_ar=os.listdir()#LISTA DE ARCHIVOS EN EL DIRECTORIO DE PYTHON
            for i in lista_ar:
                os.renames(nombreA,nuevo_nombre)
                print("El archivo \'",nombreA,"\' es ahora \'",nuevo_nombre,"\'")
                break
                print("")
                print("Se cambio el nombre de",nombreA,"por el de",nuevo_nombre)
                print("")
                
        if op!="D":
            pickle.dump(nombre,open(nombreA,"wb"))      
    conti=ns(input("¿Desea continuar?: "))
    if conti==("n"):
        break
    try:
        subprocess.call(["cmd.exe","/C","cls"])
    except:
        continue
  
