import Functions
lista=[]
palabras=[]
Acumulator=0
path="Ex38.txt"
if Functions.archivo_valido(path)==True:
    archivo=open(path,'r')
    lines=archivo.readlines()
    for line in lines:
        line=line.strip()
        palabras=line.split(" ")
        lista=lista+palabras
    for e in lista:
        Acumulator+=len(e)
    words=len(lista)
    Result=Acumulator/words
    print(lista)
    print(Acumulator)
    print(words)
    print(Result)
