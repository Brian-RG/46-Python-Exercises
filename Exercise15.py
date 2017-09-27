def longest_word(lista):
    longest=""
    for w in lista:
        if len(w) >= len(longest):
            longest=w
        else:
            pass

    return longest

lista=[]
print("Introduce the words, write 'break to finish' ")
while True:
    word=input("Introduce the word: ")
    if word=="break":
        break
    else:
        lista.append(word)
print(longest_word(lista))
