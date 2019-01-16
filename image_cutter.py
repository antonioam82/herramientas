from PIL import Image
from VALID import ns
import subprocess
import os

while True:
    puntos=[]
    inicial=input("Introduce inicial: ")
    pixels=input("Introduce medidas: ")
    pix=pixels.split(",")
    for i in pix:
        puntos.append(int(i))
    box=(puntos[0],puntos[1],puntos[2],puntos[3])
    print(box)
    for file in os.listdir():
        if file.startswith(inicial):
            try:
                imagen = Image.open(file)
                n_imagen = imagen.crop(box)
                n_imagen.save(file)
            except:
                print("La operación no pudo completarse con éxito")
                pass
    conti=ns(input("¿Continuar?: "))

    if conti=="n":
        break
    subprocess.cal(["cmd.exe","/C","cls"])
