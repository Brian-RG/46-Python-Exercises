palabras=[]
path="prueba.txt"
archivo=open(path,'r')
lineas=archivo.readlines()
for line in lineas:
    line= line.strip()
    palabras.append(line)

for word in palabras:
    reverse= word[::-1]
    if reverse in palabras:
        print(word," and ",reverse)
