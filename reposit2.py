import random

def tirada_dado(veces):
    resul=[]
    for i in range(veces):
        resul.append(random.randint(1, 10))
        diez=resul.count(10)
        unos=resul.count(1)
    print(f"exitos seguros={diez},pifias={unos}")
    return resul
print(tirada_dado(5))
