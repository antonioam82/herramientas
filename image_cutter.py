from PIL import Image
from VALID import ns
import subprocess
import os

def long():
    while True:
        puntos=[]
        tup=input("Introduce medidas: ")
        pix=tup.split(",")
        if len(pix)==4:
            for i in pix:
                try:
                    puntos.append(int(i))
                except:
                    continue
            return puntos

while True:
    while True:
        inicial=input("Introduce inicial: ")
        if inicial!=(""):
            break

    puntos=long()
    print(puntos)
    
    box=(puntos[0],puntos[1],puntos[2],puntos[3])

    for file in os.listdir():
        if file.startswith(inicial):
            try:
                imagen = Image.open(file)
                ig=imagen
                n_imagen = imagen.crop(box)
                n_imagen.save(file)
                
            except:
                print("La operación no pudo completarse con éxito")
                ig.save(file)
                break
            
    conti=ns(input("¿Continuar?: "))

    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])




