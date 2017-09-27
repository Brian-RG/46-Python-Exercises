Swedish={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"år"}
def words(text):
    english=[]
    word=""
    for c in text:
        if c==" ":
            english.append(word)
            word=""
        else:
            word+=c
    return list(map(lambda trans: Swedish[trans],english))
texto=input("Introduce your text to translate to Swedish: ")
words(texto)
print(words(texto))
