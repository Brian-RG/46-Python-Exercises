def int_lista(string_lista):
    lista=[]
    for w in string_lista:
        length=len(w)
        lista.append(length)
    return lista


words=[]
print("Introduce your words, write 'break' to finish.")
while True:
    word=input("Introduce the word: ")
    if word=="break":
        break
    else:
        words.append(word)
print(int_lista(words))
