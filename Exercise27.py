lista_ap=[]
while True:
    word=input("Introduce a word: ")
    if word=="break":
        break
    else:
        lista_ap.append(word)

print(list(map(lambda words: len(words),lista_ap)))
