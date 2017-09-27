def Translate(text):
    #Dictionary
    Swedish={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"år"}
    word=""
    translated=""
    for w in text:
        if not w==" " and not w==",":
            word+=w
        else:
            translated+=w
            translated+=Swedish[word]
            word=""
    return translated

texto="merry christmas and happy new year"
print(Translate(texto))
