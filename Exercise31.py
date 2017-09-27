def reducir(lista1):
    v=0
    for v in lista1:
        s=v+1
        if lista1[v] > lista1[s]:
            return lista1[v]
        else:
            return lista1[s]

def mapp(lista2):
    nueva=[]
    for c in lista2:
        nueva.append(len(c))
    return nueva

def filtrar(lista3,n):
    new=[]
    for m in lista3:
        if len(m) >n:
            new.append(m)
    return new

prueba=[2,4,6,1,0]
palabras=["hola","amigo","perro","abrazo"]
num=4
print(reducir(prueba))
print(mapp(palabras))
print(filtrar(palabras,num))
