#alternade
import urllib.request
lista=urllib.request.urlopen("http://www.puzzlers.org/pub/wordlists/unixdict.txt")
lineas=lista.readlines()
words=[]
for line in lineas:
    new_word=""
    line=line.strip()
    line=str(line)
    w=line.split("b'")
    i=len(w)-1
    word=w[i]
    word=word[:-1]
    if "'" in word:
        for c in word:
            if c=="\":
                word.replace(c,"")
            else:
                new_word+=c
                words.append(new_word)
    else:
        words.append(word)
print(words)
#linea=lista.readline()
#linea=linea.strip()
#linea=str(linea)
#i=linea.split("b'")
#o=i[1]
#o=o[:-1]
#print(linea)
#print(i)
#print(o)

#if "10th"==o:
#    print("holi")
#else:
#    print("ño")
