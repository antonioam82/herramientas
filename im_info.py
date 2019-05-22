from PIL import Image
import numpy as np
import os

os.chdir(r'')

while True:
    dato=input("Comm: ")
    if dato=="end":
        break
    else:
        if "." in dato:
            try:
                im=Image.open(dato)
            except:
                print("Nope")
        else:
            try:
                sep=dato.split(",")
                im.convert(sep[0])
            except:
                print("DATOS NO APTOS")
                continue
            if sep[1]=="R":
                output=np.array(im.getchannel(0))
            elif sep[1]=="G":
                output=np.array(im.getchannel(1))
            elif sep[1]=="B":
                output=np.array(im.getchannel(2))
            print(output)
    
