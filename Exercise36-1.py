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
        word=""
        line=line.strip()
        line=line.lower()
        for c in line:
            if c != " ":
                word+=c
            else:
                if word in times:
                    times[word]+=1
                else:
                    times[word]=1
                word=""
            if c==(len(line)-1):
                word+=c
                print(word)
                if word in times:
                    times[word]+=1
                else:
                    times[word]=1
                    word=""
    print(times)
    for t in times:
        if times[t]==1:
            print(t)
else:
    print("error")
