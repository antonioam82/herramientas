from PIL import Image
from VALID import ns, OKI
import subprocess, os

while True:
    while True:
        inicial=input("Introduce inicial: ")
        if inicial!=(""):
            break
        
    dato_iz=OKI(input("Introduce dato izquierdo: "))
    dato_sup=OKI(input("Introduce dato superior: "))
    dato_der=OKI(input("Introduce dato derecho: "))
    dato_inf=OKI(input("Introduce dato inferior: "))
    
    box=(dato_iz, dato_sup, dato_der, dato_inf)

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




