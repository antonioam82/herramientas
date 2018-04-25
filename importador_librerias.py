import pip
from VALID import ns

while True:
    libreria=input("Escriba el nombre de la libreria que quiere importar: ")
    pip.main(["install",libreria])
    conti=ns(input("¿Desea continuar?: "))
    if conti==("s"):
        continue
    break
