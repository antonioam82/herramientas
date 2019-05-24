from PIL import Image
import numpy as np
import os

opciones=['R','G','B','P']

os.chdir(r'C:\Users\Antonio\Documents\AAM images')

while True:
    dato=input("Comm: ")
    if dato=="end":
        break
    else:
        if "." in dato:
            try:
                sep=dato.split(",")
                im=Image.open(sep[0]).convert(sep[1])
            except:
                print("Nope")
                continue
        else:
            if dato not in opciones:
                print("DATO NO VÁLIDO")
                continue
            if dato=="P":
                output=np.array(im.getpalette())
            elif dato=="R":
                output=np.array(im.getchannel(0))
                print("Done")
            elif dato=="G":
                output=np.array(im.getchannel(1))
            elif dato=="B":
                output=np.array(im.getchannel(2))
            print(output)
    
