import subprocess
while True:
    a=OKI_R(input("Numero: "))
    if a=="R":
        subprocess.call(["cmd.exe","/C","cls"])
        continue
    b=OKI_R(input("Numero2: "))
    if b=="R":
        subprocess.call(["cmd.exe","/C","cls"])
        continue
    c=OKI_R(input("Numero3: "))
    if c=="R":
        subprocess.call(["cmd.exe","/C","cls"])
        continue
    d=OKI_R(input("Numero4: "))
    if d=="R":
        subprocess.call(["cmd.exe","/C","cls"])
        continue
    break
print("Nuevo paso")
print("otro paso")
re=a+b+c+d
print(re)
