import string
import Functions
def startswith(word,mayus):
    return word[0] in mayus

Titles=["Mr.","Mrs.","Dr.","Jr."]
minus=string.ascii_lowercase
mayus=string.ascii_uppercase
path="Ex42.txt"
archive=open(path,'r')
text=archive.read()
words=text.split()
respuesta=""
w=0
while w<len(words):
    respuesta+=words[w]+" "
    if w==len(words)-1:
        break
    if words[w] in Titles:
        pass
    else:
        if words[w].endswith((".","!","?")) and startswith(words[w+1],mayus):
            respuesta+="\n"
    w+=1
print(respuesta)
