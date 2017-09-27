#Hapax
import string
import Functions
times={}
lista=[]
path="Texto.txt"
Functions.archivo_valido(path)
if Functions.archivo_valido(path)==True:
    archivo=open(path,'r')
    lines=archivo.readlines()
    for line in lines:
        line=line.strip()
        line=line.lower()
        lista=line.split(" ")
        for e in lista:
            if e in times:
                times[e]+=1
            else:
                times[e]=1
    for t in times:
        if times[t]==1:
            print(t)
