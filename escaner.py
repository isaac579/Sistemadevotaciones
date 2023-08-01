import subprocess
i = 1 #intentos
ipDetect=[]
for ping in range(64,254):
    print("__inicio del ciclo__")
    adddres="192.168.1."+str(ping)
    res=subprocess.call(['ping','-c',str(i),adddres])
    print("---Comparativa---")
    if res == 0:
        print("ping de la direccion: ", adddres, "..ok")
        print("Almacenamiento")
        ipDetect.append(adddres)
    elif res == 2:
        print("No responde la direccion", adddres)
    else:
        print(adddres, "ping fallido!")
if ipDetect:
    print("Hizo ping en: ")
    print(ipDetect)