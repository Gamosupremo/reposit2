import random

def dado(veces):
    result=[]
    for i in range(0,veces):
        result.append(random.randint(1, 10))
    for i in result:
        if i==10:
            result.append(random.randint(1, 10))
    return result
print (dado(5))