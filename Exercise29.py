def words_longer(lista,n):
    words=list(filter(lambda word: len(word)>n,lista))
    return words
palabras=[]
while True:
    word=input("Introduce una palabra: ")
    if word=="break":
        break
    else:
        palabras.append(word)

num=int(input("Ahora introduce un numero: "))

print(words_longer(palabras,num))
