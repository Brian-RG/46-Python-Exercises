def filter_long_words(lista,n):
    longer=[]
    for w in lista:
        if len(w) > n:
            longer.append(w)
        else:
            pass
    return longer

words=[]
print("Introduce your words, write 'break' to finish")
while True:
    word=input("Introduce your word: ")
    if word=="break":
        break
    else:
        words.append(word)

num=int(input("Now introduce the number: "))

print(filter_long_words(words,num))
