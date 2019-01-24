from PIL import Image
from VALID import ns
import subprocess
import os

def long():
    while True:
        tup=input("Introduce medidas: ")
        pix=tup.split(",")
        if len(pix)==4:
            break
    return pix

while True:
    cuenta=0
    puntos=[]
    inicial=input("Introduce inicial: ")
    
    pixels=long()
    
    for i in pixels:
        try:
            puntos.append(int(i))
        except:
            print("Introduzca números")
            break

    if len(puntos)==4:
        box=(puntos[0],puntos[1],puntos[2],puntos[3])
    else:
        continue

    for file in os.listdir():
        if file.startswith(inicial):
            try:
                imagen = Image.open(file)
                ig=imagen
                n_imagen = imagen.crop(box)
                n_imagen.save(file)
                cuenta+=1
            except:
                print("La operación no pudo completarse con éxito")
                ig.save(file)
                break
    if cuenta==0:
        print("No se encontrón ningun archivo que empiece por",inicial)
    conti=ns(input("¿Continuar?: "))

    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])


